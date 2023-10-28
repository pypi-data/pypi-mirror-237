import argparse, os, shutil, subprocess, sys, yaml

BUILD_DIR_NAME = "prairiebuild"
BUILD_FILE_NAME = "prairiebuild.yml"


def find_source(name: str, path: str):
    """Locate the full path of a source file by walking up the tree."""

    build_path = os.path.join(path, BUILD_DIR_NAME)
    assert os.path.exists(build_path) and os.path.isdir(build_path), f"could not locate file \"{name}\" in prairiebuild directory"

    file_path = os.path.join(build_path, name)
    if not os.path.exists(file_path):
        return find_source(name, os.path.dirname(path))

    return file_path


def build_target(name: str, data: dict, path: str):
    """Builds a single target (file or directory) by copying it from its source."""

    path = os.path.join(path, name)
    print(f"Building target {path}...", file=sys.stderr)

    # if the target is a directory, recreate it
    if "files" in data:
        if os.path.exists(path):
            shutil.rmtree(path)
        os.makedirs(path)
        build_targets(data["files"], path)

    else:
        # copy the target from source
        source = data["source"] if "source" in data else name
        source_path = find_source(source, current_dir)
        if os.path.isdir(source_path):
            shutil.copytree(source_path, path)
        else:
            shutil.copy2(source_path, path)

    if "build" in data:
        assert type(data["build"]) is str, f"build: expected str, got {type(data['build']).__name__}"
        os.chdir(path)
        result = subprocess.run(data["build"], shell=True, executable="/bin/bash")
        assert result.returncode == 0, f"build command \"{data['build']}\" encountered an error"
        os.chdir(current_dir)

    if "clean" in data:
        clean_targets(data["clean"], path)


def build_targets(targets: list, path: str = ""):
    """Builds a list of targets."""

    assert type(targets) is list, f"files: expected list, got {type(targets).__name__}"
    for target in targets:
        if type(target) is dict:
            assert len(target) == 1, f"files: invalid target (expected single key, found multiple): {list(target)}"
            build_target(
                name = next(iter(target)),
                data = next(iter(target.values())),
                path = path)
        elif type(target) is str:  # target file
            build_target(
                name = target,
                data = {},
                path = path)
        else:
            assert False, f"files: invalid target: {target}"


def clean_targets(targets: list, path: str = ""):
    """Removes a list of targets."""

    assert type(targets) is list, f"clean: expected list, got {type(targets).__name__}"
    for target in targets:
        if type(target) is dict:
            assert len(target) == 1, f"clean: invalid target (expected single key, found multiple): {list(target)}"
            target = next(iter(target))
        assert type(target) is str, f"clean {target}: expected str, got {type(target).__name__}"
        if os.path.exists(os.path.join(path, target)):
            if os.path.isdir(os.path.join(path, target)):
                shutil.rmtree(os.path.join(path, target))
            else:
                os.remove(os.path.join(path, target))


def main():
    global current_dir

    # parse command-line arguments
    parser = argparse.ArgumentParser(
        description="Command-line tool for building PrairieLearn questions"
    )
    parser.add_argument('--clean', '-c', action='store_true', help="Clean up generated files")
    args = parser.parse_args()

    # look for prairiebuild.yaml file in current directory
    current_dir = os.getcwd()
    if os.path.isfile(os.path.join(current_dir, BUILD_FILE_NAME)):
        with open(os.path.join(current_dir, BUILD_FILE_NAME), 'r') as build_file:
            data = yaml.load(build_file, Loader=yaml.FullLoader)
    else:
        print("unable to locate prairiebuild.yml", file=sys.stderr)

    if args.clean:
        clean_targets(data)
    else:
        build_targets(data)
