import os


def validate_path(base_path: str, filename: str) -> str:
    fullpath = os.path.normpath(os.path.join(base_path, filename))
    if not fullpath.startswith(base_path):
        raise OSError("Not allowed")

    return fullpath
