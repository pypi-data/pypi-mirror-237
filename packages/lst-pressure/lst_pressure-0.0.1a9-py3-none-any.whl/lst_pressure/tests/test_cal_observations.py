import pytest
from lst_pressure.lst_calendar import LSTCalendar, LSTIntervalType, ObservationBlock


tests = [
    {
        "latlng": ["-30:42:39.8", "21:26:38.0"],
        "calendar": ["20231001", "20231015"],
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
                    "lst_window_end": 10.2,
                    "utc_constraints": [LSTIntervalType.ALL_DAY],
                },
                {
                    "id": "obs-2",
                    "lst_window_start": 21.5,
                    "lst_window_end": 2,
                    "utc_constraints": [LSTIntervalType.NIGHT_ONLY],
                },
                {
                    "id": "obs-3",
                    "lst_window_start": 22,
                    "lst_window_end": 23,
                    "utc_constraints": [LSTIntervalType.NIGHT_ONLY],
                },
            ]
        ],
    }
]


# @pytest.mark.skip(reason="")
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
                print(block.pretty(), "::", interval)
                None

        # Get all blocks that can be observed on a date
        print()
        print("Blocks for selected dates")
        for date in cal.dates:
            intervals = date.observable_blocks()
            for i in intervals:
                for block in i.get("blocks"):
                    print(
                        date.pretty(),
                        "::",
                        i.get("interval").type.name,
                        "::",
                        block.pretty(),
                    )
