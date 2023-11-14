from django.conf import settings
from git.repo import Repo


def check_upgrade() -> bool:
    repo = Repo(settings.PROJECT_REPO)
    for remote in repo.remotes:
        remote.fetch()

    tags = sorted(repo.tags, key=lambda t: t.commit.committed_datetime)

    remote_version = str(tags[-1]).rsplit("-", 1)[-1]
    current_version = settings.VERSION.split(".")

    print(f"Current version: {current_version} -> Remote version: {remote_version}")

    if int(remote_version[0]) > int(current_version[0]):
        return True

    elif int(remote_version[0]) == int(current_version[0]):
        if int(remote_version[1]) > int(current_version[1]):
            return True

        elif int(remote_version[1]) == int(current_version[1]):
            if int(remote_version[2]) > int(current_version[2]):
                return True

        return False

    return False
