import pytest
from ...lst_calendar import LSTCalendar


@pytest.mark.parametrize(
    "start, end, expected",
    [
        ("20230404", "20230404", ["20230404"]),
        ("20230404", "20230405", ["20230404", "20230405"]),
        ("20220101", "20220105", ["20220101", "20220102", "20220103", "20220104", "20220105"]),
        (
            "20231025",
            "20231031",
            ["20231025", "20231026", "20231027", "20231028", "20231029", "20231030", "20231031"],
        ),
    ],
)
def test_Calendar(start, end, expected):
    """
    The calendar should convert start/end params into the correct range
    """
    assert expected == [d.dt.strftime("%Y%m%d") for d in LSTCalendar(start, end).dates]


# Invalid start/end should NOT work
@pytest.mark.parametrize(
    "start, end",
    [("invalidStart", "20220105"), ("20220101", "invalidEnd"), ("20220105", "20220101")],
)
def test_calendar_raises_exception_for_invalid_dates(start, end):
    with pytest.raises(ValueError):
        LSTCalendar(start, end)


def test_observations():
    start, end = ["20231001", "20231001"]
    latitude, longitude = ["-30:42:39.8", "21:26:38.0"]

    with LSTCalendar(start, end, latitude, longitude) as cal:
        print("\nIntervals")
        for row in cal.pretty_intervals():
            print(row)
