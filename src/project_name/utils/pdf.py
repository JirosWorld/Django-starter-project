"""
Utilities for PDF rendering from HTML using WeasyPrint.

Note that you need to add https://pypi.org/project/weasyprint/ to your dependencies
if you want to make use of HTML-to-PDF rendering. This is not included by default as
it's quite heavy and requires OS-level dependencies.

This module exposes the public function :func:`render_to_pdf` which renders a template
with a context into a PDF document (bytes output). You can use "external" stylesheets
in these templates, and they will be resolved through django's staticfiles machinery
by the custom :class:`UrlFetcher`.
"""
import logging
import mimetypes
from io import BytesIO
from pathlib import PurePosixPath
from typing import Tuple
from urllib.parse import urljoin, urlparse

from django.conf import settings
from django.contrib.staticfiles import finders
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string

import weasyprint

logger = logging.getLogger(__name__)

__all__ = ["render_to_pdf"]


def get_base_url() -> str:
    """
    Get the base URL where the project is served.

    You should tweak this after starting the project with a solution fitting
    your project, as we cannot guess your set-up or where your project is hosted.

    The base URL is required to be able to download/resolve custom fonts and/or any
    image URLs included in the document to render.
    """
    # some hints:
    # * define a setting `BASE_URL` in your settings matching the canonical domain where
    #   your project is deployed
    # * if you only need to serve static assets (=no user-uploaded content), you can use
    #   a dummy URL like "https://{{ project_name|lower  }}.dev"
    raise NotImplementedError("You must implement 'get_base_url'.")


class UrlFetcher:

    """
    URL fetcher that skips the network for /static/* files.
    """

    def __init__(self):
        static_url = settings.STATIC_URL
        if not urlparse(static_url).netloc:
            static_url = urljoin(get_base_url(), settings.STATIC_URL)
        self.static_url = urlparse(static_url)
        self.local_storage = issubclass(
            staticfiles_storage.__class__, FileSystemStorage
        )

    def __call__(self, url: str) -> dict:
        orig_url = url
        url = urlparse(url)
        same_base = (self.static_url.scheme, self.static_url.netloc) == (
            url.scheme,
            url.netloc,
        )
        if (
            self.local_storage
            and same_base
            and url.path.startswith(self.static_url.path)
        ):
            path = PurePosixPath(url.path).relative_to(self.static_url.path)

            absolute_path = None
            if staticfiles_storage.exists(path):
                absolute_path = staticfiles_storage.path(path)
            elif settings.DEBUG:
                # use finders so that it works in dev too, we already check that it's
                # using filesystem storage earlier
                absolute_path = finders.find(str(path))

            if absolute_path is None:
                logger.error("Could not resolve path '%s'", path)
                return weasyprint.default_url_fetcher(orig_url)

            content_type, encoding = mimetypes.guess_type(absolute_path)
            result = dict(
                mime_type=content_type,
                encoding=encoding,
                redirected_url=orig_url,
                filename=path.parts[-1],
            )
            with open(absolute_path, "rb") as f:
                result["file_obj"] = BytesIO(f.read())
            return result
        return weasyprint.default_url_fetcher(orig_url)


def render_to_pdf(template_name: str, context: dict) -> Tuple[str, bytes]:
    """
    Render a (HTML) template to PDF with the given context.
    """
    rendered_html = render_to_string(template_name, context=context)
    html_object = weasyprint.HTML(
        string=rendered_html,
        url_fetcher=UrlFetcher(),
        base_url=get_base_url(),
    )
    pdf: bytes = html_object.write_pdf()
    return rendered_html, pdf
