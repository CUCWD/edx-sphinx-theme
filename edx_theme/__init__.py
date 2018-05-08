"""
A Sphinx theme for Open edX documentation.
"""

from __future__ import absolute_import, print_function, unicode_literals

import os

import six
from six.moves.urllib.parse import quote

# When you change this, also update the CHANGELOG.rst file, thanks.
__version__ = '1.3.0'

# Use these constants in the conf.py for Sphinx in your repository
AUTHOR = 'EducateWorkforce'
COPYRIGHT = '2017, EducateWorkforce'

FEEDBACK_FORM_FMT = "https://docs.google.com/forms/d/e/1FAIpQLSe6_MOxFaa_wDt7PObo4-v9UZ7-mEhNF7h6lIPSQqaZ1ykc4Q/" \
                    "viewform?entry.1699859017&entry.147198744={pageid}"


def get_html_theme_path():
    """
    Get the absolute path of the directory containing the theme files.
    """
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def feedback_form_url(project, page):
    """
    Create a URL for feedback on a particular page in a project.
    """
    return FEEDBACK_FORM_FMT.format(pageid=quote("{}: {}".format(project, page)))


def update_context(app, pagename, templatename, context, doctree):  # pylint: disable=unused-argument
    """
    Update the page rendering context to include ``feedback_form_url``.
    """
    context['feedback_form_url'] = feedback_form_url(app.config.project, pagename)


def setup(app):
    """
    Sphinx extension to update the rendering context with the feedback form URL.

    Arguments:
        app (Sphinx): Application object for the Sphinx process

    Returns:
        a dictionary of metadata (http://www.sphinx-doc.org/en/stable/extdev/#extension-metadata)
    """
    event = 'html-page-context' if six.PY3 else b'html-page-context'
    app.connect(event, update_context)

    return {
        'parallel_read_safe': True,
        'parallel_write_safe': True,
        'version': __version__,
    }
