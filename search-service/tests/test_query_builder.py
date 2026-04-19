"""Tests for the search query builder module."""

from search.query_builder import fetch_paginated_results


def test_fetch_paginated_results_includes_active_filter():
    filters = [{"order_status": "pending"}]

    result = fetch_paginated_results(page=1, page_size=20, filters=filters)

    assert result["query"]["filters"] == [{"order_status": "pending"}, {"active": True}]
    assert result["query"]["offset"] == 0
    assert result["query"]["limit"] == 20


def test_fetch_paginated_results_does_not_leak_filters_between_calls():
    first = fetch_paginated_results(page=1, page_size=10)
    second = fetch_paginated_results(page=2, page_size=10)

    assert first["query"]["filters"] == [{"active": True}]
    assert second["query"]["filters"] == [{"active": True}]
