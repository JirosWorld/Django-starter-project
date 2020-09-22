import logging
import os
from shutil import which
from subprocess import CalledProcessError, check_output

from django.conf import settings

logger = logging.getLogger(__name__)


def _get_version_from_file():
    """
    Returns a commit hash from the project's .git/ dir if it exists
    """
    heads_dir = os.path.join(settings.BASE_DIR, ".git", "refs", "heads")

    try:
        heads = os.listdir(heads_dir)
    except FileNotFoundError:
        logging.warning("Unable to read commit hash from git files")
        return ""

    for filename in ("master", "main", "develop"):
        if filename in heads:
            try:
                with open(os.path.join(heads_dir, filename)) as file:
                    return file.read().strip()
            except OSError:
                logging.warning("Unable to read commit hash from file")

    return ""


def _get_version_from_git():
    """
    Returns the current tag or commit hash supplied by git
    """
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

    return commit or ""


def get_current_version():
    if os.environ.get("VERSION_TAG"):
        return os.environ.get("VERSION_TAG")
    elif which("git"):
        return _get_version_from_git()

    return _get_version_from_file()
