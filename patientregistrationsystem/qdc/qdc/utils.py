import os

PASSWORD_MIN_LEN = 8
PASSWORD_MAX_LEN = 127
PASSWORD_REGEX = r"^(?=.*\d)(?=.*[a-z]).{8,127}$"

FIRSTNAME_REGEX = r"^[a-zA-Z]+((\s|\-)[a-zA-Z]+)?$"
LASTNAME_REGEX = r"^[a-zA-Z]+((\s|\-)[a-zA-Z]+)?$"
FULLNAME_REGEX = r"^[A-Z][a-zA-Z']{1,}(?: [a-zA-Z0-9']+){0,5}$"

PHONE_REGEX = r"^[ \(\)\-\d]+"

EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

DATE_REGEX = r"\d{4}-\d{2}-\d{2}"

USERNAME_REGEX = r"^[A-Za-z][A-Za-z0-9_.]{4,29}$"


def validate_path(base_path: str, filename: str) -> str:
    fullpath = os.path.normpath(os.path.join(base_path, filename))
    if not fullpath.startswith(base_path):
        raise OSError("Not allowed")

    return fullpath
