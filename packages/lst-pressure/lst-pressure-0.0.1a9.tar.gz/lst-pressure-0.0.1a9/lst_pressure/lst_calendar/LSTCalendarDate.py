"""
lst_calendar.LSTCalendarDate
"""
from typing import List, Dict, Union
from .LSTInterval import LSTInterval
from ..lst_calendar import LSTCalendar, ObservationBlock


class LSTCalendarDate:
    def __init__(self, dt, tomorrow_dt, sun, tomorrow_sun, intervals, cal) -> None:
        self.dt = dt
        self.tomorrow_dt = tomorrow_dt
        self.sun = sun
        self.tomorrow_sun = tomorrow_sun
        self.intervals: "LSTInterval" = intervals
        self.calendar: "LSTCalendar" = cal

    def observable_blocks(self) -> List[Dict[str, Union["LSTInterval", "ObservationBlock"]]]:
        results = []
        lst_block_index = self.calendar.lst_block_index
        for calInterval in self.intervals:
            block_intervals = lst_block_index.get_intervals_contained_by(calInterval.interval)
            if block_intervals:
                results.append(
                    {
                        "interval": calInterval,
                        "blocks": [
                            b[2]
                            for b in block_intervals
                            if not b[2].utc_constraints or calInterval.type in b[2].utc_constraints
                        ],
                    }
                )

        return results

    def pretty(self) -> List[any]:
        return [
            "Date",
            self.dt.strftime("%Y-%m-%d"),
            # self.sun.dawn.strftime("%H:%M"),
            # self.sun.sunrise.strftime("%H:%M"),
            self.sun.sunset.strftime("%H:%M"),
            # self.sun.dusk.strftime("%H:%M"),
            # self.tomorrow_sun.dawn.strftime("%H:%M"),
            self.tomorrow_sun.sunrise.strftime("%H:%M"),
            # self.tomorrow_sun.sunset.strftime("%H:%M"),
            # self.tomorrow_sun.dusk.strftime("%H:%M"),
        ]
