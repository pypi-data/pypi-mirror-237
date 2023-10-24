import pytest
from lst_pressure.lst_calendar import LSTCalendar, LSTInterval, ObservationBlock
from lst_pressure.idx import pretty


tests = [
    {
        "latlng": ["-30:42:39.8", "21:26:38.0"],
        "calendar": ["20231001", "20231002"],
        "observation_blocks": [
            ObservationBlock(
                id=block.get("id"),
                lst_window_start=block.get("lst_window_start"),
                lst_window_end=block.get("lst_window_end"),
                utc_constraints=block.get("utc_constraints"),
            )
            for block in [
                {
                    "id": "obs-1",
                    "lst_window_start": 6.5,
                    "lst_window_end": 19.2,
                    "utc_constraints": [LSTInterval.NIGHT_ONLY],
                },
                {
                    "id": "obs-2",
                    "lst_window_start": 6.5,
                    "lst_window_end": 7.2,
                    "utc_constraints": [LSTInterval.AVOID_SUNRISE_SUNSET],
                },
                {
                    "id": "obs-3",
                    "lst_window_start": 10,
                    "lst_window_end": 14,
                    "utc_constraints": [LSTInterval.AVOID_SUNRISE_SUNSET],
                },
            ]
        ],
    }
]


@pytest.mark.parametrize("test", tests)
def test_observations(test):
    start, end = test.get("calendar")
    latitude, longitude = test.get("latlng")

    with LSTCalendar(start, end, latitude, longitude) as cal:
        cal.observation_blocks = test.get("observation_blocks")

        # Get intervals that a block can be scheduled on
        # Intervals have dates, can't get the date directly
        # since we only want date.intervals for loaded observation
        # blocks
        print()
        print("Dates for selected blocks")
        for block in cal.observation_blocks:
            intervals = block.observable_dates()
            for interval in intervals:
                print(block.pretty(), "::", pretty(interval))

        # Get all blocks that can be observed on a date
        print()
        print("Blocks for selected dates")
        for date in cal.dates:
            intervals = date.observable_blocks()
            for interval in intervals:
                for block in interval.get("blocks"):
                    print(
                        date.pretty(),
                        "::",
                        interval.get("interval")[2].get("type").name,
                        "::",
                        block.pretty(),
                    )
