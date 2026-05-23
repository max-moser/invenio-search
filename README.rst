..
    SPDX-FileCopyrightText: 2015-2018 CERN.
    SPDX-License-Identifier: MIT

================
 Invenio-Search
================

.. image:: https://img.shields.io/github/license/inveniosoftware/invenio-search.svg
        :target: https://github.com/inveniosoftware/invenio-search/blob/master/LICENSE

.. image:: https://github.com/inveniosoftware/invenio-search/workflows/CI/badge.svg
        :target: https://github.com/inveniosoftware/invenio-search/actions?query=workflow%3ACI

.. image:: https://img.shields.io/coveralls/inveniosoftware/invenio-search.svg
        :target: https://coveralls.io/r/inveniosoftware/invenio-search

.. image:: https://img.shields.io/pypi/v/invenio-search.svg
        :target: https://pypi.org/pypi/invenio-search


Search management for Invenio (for Elasticsearch and OpenSearch).

Features:

- Allows Invenio modules to register indexes, aliases and index templates.
- Manages the creation and deletion of indices, aliases and templates.
- API for providing stable searches (e.g. prevents bouncing of search results).
- Maps JSONSchema URLs to Elasticsearch/OpenSearch indexes.
- Supports Elasticsearch v7 and OpenSearch v1.

Further documentation is available at https://invenio-search.readthedocs.io/.
