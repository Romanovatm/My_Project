import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "state,expected",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        ("FAILED", []),
    ],
)
def test_filter_by_state(list_of_dicts, state, expected):
    assert filter_by_state(list_of_dicts, state) == expected


@pytest.mark.parametrize(
    "state,expected",
    [
        (
            "EXECUTED",
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
    ],
)
def test_filter_by_state_without_state(list_of_dicts_without_state, state, expected):
    assert filter_by_state(list_of_dicts_without_state, state) == expected


@pytest.mark.parametrize(
    "is_reversed, expected",
    [
        (
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
    ],
)
def test_sort_by_date(list_of_dicts, is_reversed, expected):
    assert sort_by_date(list_of_dicts, is_reversed) == expected


def test_sort_by_date_same_dates_is_reversed_true(list_of_dicts_same_date):
    assert sort_by_date(list_of_dicts_same_date, True) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 123456789, "state": "FAILED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_same_dates_is_reversed_false(list_of_dicts_same_date):
    assert sort_by_date(list_of_dicts_same_date, False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 123456789, "state": "FAILED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.mark.parametrize(
    "is_reversed,expected",
    [
        (
            True,
            [
                {"id": 123456789, "state": "FAILED", "date": "31 мая 2026 г."},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 939719570, "state": "EXECUTED", "date": "2005-11-11"},
                {"id": 41428829, "state": "EXECUTED", "date": "10/02/1994"},
                {"id": 594226727, "state": "CANCELED", "date": ""},
            ],
        )
    ],
)
def test_sort_by_different_date(list_of_dicts_different_date, is_reversed, expected):
    assert sort_by_date(list_of_dicts_different_date, True) == expected
