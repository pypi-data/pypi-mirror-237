import pytest
from ....lst_calendar.helpers.calculate_intervals import (
    calculate_intervals,
    calculate_NIGHT_ONLY,
    calculate_AVOID_SUNRISE_SUNSET,
    calculate_AVOID_SUNSET_SUNRISE,
    calculate_OBSERVATION_WINDOW
)
from ....utils import normalize_yyyymmdd_to_datetime
from ....utils import utc_to_lst

@pytest.mark.parametrize(
    "start, end, expected",
    [
        (7, 13, (7, 13)),
        (22, 7, (22, 31)),
        (1, 6, (1, 6)),
        (18, 2, (18, 26)),
    ],
)
def test_calculate_OBSERVATION_WINDOW(start, end, expected):
    result = calculate_OBSERVATION_WINDOW(start, end)
    assert result == expected


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (7, 13, (7, 13)),
        (22, 7, (22, 31)),
        (1, 6, (1, 6)),
        (18, 2, (18, 26)),
    ],
)
def test_calculate_AVOID_SUNRISE_SUNSET(start, end, expected):
    result = calculate_AVOID_SUNRISE_SUNSET(start, end)
    assert result == expected


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (7, 13, (7, 13)),
        (22, 7, (22, 31)),
        (1, 6, (1, 6)),
        (18, 2, (18, 26)),
    ],
)
def test_calculate_AVOID_SUNSET_SUNRISE(start, end, expected):
    result = calculate_AVOID_SUNSET_SUNRISE(start, end)
    assert result == expected


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (22, 7, (22, 31)),
        (1, 6, (1, 6)),
        (18, 2, (18, 26)),
    ],
)
def test_calculate_NIGHT_ONLY(start, end, expected):
    result = calculate_NIGHT_ONLY(start, end)
    assert result == expected


@pytest.mark.parametrize(
    "latitude,longitude,today_dt",
    [
        ("-30:42:39.8", "21:26:38.0", "20231026"),
     ],
)
def test_calculate_intervals(latitude, longitude, today_dt):
    today = normalize_yyyymmdd_to_datetime(today_dt)
    intervals = calculate_intervals(latitude, longitude, today)
    print('\n')
    for i in intervals:
        print(
            i.type.name,
            round(i.start, 1),
            round(i.end, 1),
            '|',
            f"DAWN (UTC {i.sun.dawn.strftime("%H:%M")} LST {round(utc_to_lst(i.sun.dawn, latitude, longitude), 1)})",
            f"SUNRISE (UTC {i.sun.sunrise.strftime("%H:%M")} LST {round(utc_to_lst(i.sun.sunrise, latitude, longitude), 1)})",
            f"SUNSET {i.sun.sunset.strftime("%H:%M")}",
            f"DUSK {i.sun.dusk.strftime("%H:%M")}",
        )
