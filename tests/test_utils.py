# SPDX-FileCopyrightText: 2018-2022 CERN.
# SPDX-FileCopyrightText: 2022 TU Wien.
# SPDX-License-Identifier: MIT

import pytest

from invenio_search.utils import build_index_name


@pytest.mark.parametrize(
    ("parts", "prefix", "suffix", "expected"),
    [
        (["records"], "", "", "records"),
        (["records"], "foo-", "", "foo-records"),
        (["records", "record"], "foo-", "", "foo-records-record"),
        (["records", "record"], "", "-new", "records-record-new"),
        (["test", "recs", "rec"], "foo-", "-old", "foo-test-recs-rec-old"),
    ],
)
def test_build_suffix_index_name(app, parts, prefix, suffix, expected):
    app.config.update(SEARCH_INDEX_PREFIX=prefix)
    assert build_index_name(parts, suffix=suffix, app=app) == expected
