"""
lst_calendar.LSTCalendarDate
"""
from typing import List, Dict, Union
from intervaltree import Interval
from ..lst_calendar import LSTCalendar, ObservationBlock


class LSTCalendarDate:
    def __init__(self, dt, tomorrow_dt, sun, tomorrow_sun, intervals, cal) -> None:
        self.dt = dt
        self.tomorrow_dt = tomorrow_dt
        self.sun = sun
        self.tomorrow_sun = tomorrow_sun
        self.intervals = intervals
        self.calendar: "LSTCalendar" = cal

    def observable_blocks(self) -> List[Dict[str, Union["Interval", "ObservationBlock"]]]:
        results = []
        lst_block_index = self.calendar.lst_block_index
        for interval in self.intervals:
            block_intervals = lst_block_index.get_intervals_contained_by(interval)
            if block_intervals:
                results.append(
                    {
                        "interval": interval,
                        "blocks": [
                            b[2]
                            for b in block_intervals
                            if not b[2].utc_constraints
                            or interval[2].get("type") in b[2].utc_constraints
                        ],
                    }
                )

        return results

    def pretty(self) -> List[any]:
        return [
            "Date",
            self.dt.strftime("%Y-%m-%d"),
            self.sun.get("dawn").strftime("%H:%M"),
            self.sun.get("sunrise").strftime("%H:%M"),
            self.sun.get("sunset").strftime("%H:%M"),
            self.sun.get("dusk").strftime("%H:%M"),
            self.tomorrow_sun.get("dawn").strftime("%H:%M"),
            self.tomorrow_sun.get("sunrise").strftime("%H:%M"),
            self.tomorrow_sun.get("sunset").strftime("%H:%M"),
            self.tomorrow_sun.get("dusk").strftime("%H:%M"),
        ]
