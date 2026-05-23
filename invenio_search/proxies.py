# SPDX-FileCopyrightText: 2015-2018 CERN.
# SPDX-License-Identifier: MIT

"""Proxy objects for easier access to application objects."""

from flask import current_app
from werkzeug.local import LocalProxy


def _get_current_search():
    """Return current state of the search extension."""
    return current_app.extensions["invenio-search"]


def _get_current_search_client():
    """Return current search client."""
    return _get_current_search().client


current_search = LocalProxy(_get_current_search)
current_search_client = LocalProxy(_get_current_search_client)
