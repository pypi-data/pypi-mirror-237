import os
import zipfile


def _compress_path(_path: str, zip_file: zipfile.ZipFile):
    for subpath in os.listdir(_path):
        if os.path.isdir(f"{_path}/{subpath}"):
            if subpath not in [f"__pycache__", f"experiments", f"instances"]:
                _compress_path(f"{_path}/{subpath}", zip_file)
        else:
            zip_file.write(os.path.join(_path, subpath))


def compress_project(_root: str, out_dir: str):
    zip_file = zipfile.ZipFile(f"{out_dir}/project.zip", "w")
    _compress_path(_root, zip_file)
    zip_file.close()
