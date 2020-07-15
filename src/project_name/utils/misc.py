import logging
from shutil import which
from subprocess import CalledProcessError, check_output

logger = logging.getLogger(__name__)


def get_current_version():
    if not which("git"):
        return ""

    try:
        tags = check_output(
            ["git", "tag", "--points-at", "HEAD"], universal_newlines=True
        )
    except CalledProcessError:
        logger.warning("Unable to list tags")
        tags = None

    if tags:
        return next(version for version in tags.splitlines())

    try:
        commit = check_output(["git", "rev-parse", "HEAD"], universal_newlines=True)
    except CalledProcessError:
        logger.warning("Unable to list current commit hash")
        commit = None

    return commit if commit else ""


VERSION = get_current_version()
