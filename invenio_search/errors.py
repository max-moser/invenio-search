# SPDX-FileCopyrightText: 2019 CERN.
# SPDX-License-Identifier: MIT

"""Invenio search errors."""


class IndexAlreadyExistsError(Exception):
    """Raised when an index or alias already exists during index creation."""


class NotAllowedMappingUpdate(Exception):
    """Raised when attempted mapping update is not allowed."""
