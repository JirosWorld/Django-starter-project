from subprocess import CalledProcessError
from unittest import skip
from unittest.mock import patch

from django.conf import settings
from django.test import TestCase

from {{project_name|lower}}.conf.version import get_current_version


class VersionTestCase(TestCase):
    def setUp(self):
        patched_subprocess = patch("{{ project_name|lower }}.utils.misc.check_output")

        self.mocked_subprocess = patched_subprocess.start()

    def tearDown(self):
        patch.stopall()

    def test_tagged_commit(self):
        self.mocked_subprocess.return_value = "v1.2.4"

        self.assertEqual(get_current_version(), "v1.2.4")

    def test_multiple_tags(self):
        self.mocked_subprocess.return_value = "v5.1.1\nv3.4.1\nv0.2.2\n"

        self.assertEqual(get_current_version(), "v5.1.1")

    def test_tag_error(self):
        self.mocked_subprocess.side_effect = (
            CalledProcessError(1, "/bin/false"),
            "c4a364ccce8b99105b8d371100918645559174b1",
        )

        self.assertEqual(
            get_current_version(), "c4a364ccce8b99105b8d371100918645559174b1"
        )

    def test_tag_and_commit_error(self):
        self.mocked_subprocess.side_effect = (
            CalledProcessError(1, "/bin/false"),
            CalledProcessError(1, "/bin/false"),
        )

        self.assertEqual(get_current_version(), "")

    def test_commit_hash(self):
        self.mocked_subprocess.side_effect = (
            "",
            "c4a364ccce8b99105b8d371100918645559174b1",
        )

        self.assertEqual(
            get_current_version(), "c4a364ccce8b99105b8d371100918645559174b1"
        )

    def test_no_tag_or_commit(self):
        self.mocked_subprocess.side_effect = (
            "",
            "",
        )

        self.assertEqual(get_current_version(), "")

    @patch("{{ project_name|lower }}.utils.misc.which")
    def test_no_git_installed(self, mocked_which):
        mocked_which.return_value = False

        self.assertEqual(get_current_version(), "")
