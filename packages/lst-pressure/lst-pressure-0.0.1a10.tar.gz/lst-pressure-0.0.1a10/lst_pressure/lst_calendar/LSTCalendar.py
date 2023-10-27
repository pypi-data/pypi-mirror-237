"""
lst_calendar.LSTCalendar
"""
from datetime import timedelta, datetime
from typing import Union, List
from .ObservationBlock import ObservationBlock
from .LSTCalendarDate import LSTCalendarDate
from .Sun import Sun
from ..index.idx import Idx, Interval
from .helpers import calculate_intervals, calculate_OBSERVATION_WINDOW
from ..utils import (
    normalize_yyyymmdd_to_datetime,
    normalize_coordinates,
)


class LSTCalendar:
    """
    Calendar tailored for LST (Local Sidereal Time) related interval lookups.

    Attributes
    ----------
    start : datetime
        The beginning of the date range for the calendar.
    end : datetime
        The conclusion of the date range for the calendar.
    latitude : float
        The geographic latitude in decimal degrees. Defaults to 0.
    longitude : float
        The geographic longitude in decimal degrees. Defaults to 0.
    lst_calendar_index : Idx
        An index to manage intervals efficiently.
    dates : List[LSTCalendarDate]
        A list containing dates and corresponding sun statistics within the range.

    Methods
    -------
    __init__(start, end, latitude=0, longitude=0)
        Initialize the LSTCalendar object.
    _calculate_intervals(today_dt, today_sun, tomorrow_sun)
        Calculate intervals for a given date based on sun statistics.
    """

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __init__(
        self,
        start: Union[str, datetime],
        end: Union[str, datetime],
        latitude: Union[str, float] = 0,
        longitude: Union[str, float] = 0,
    ):
        """
        Initialize the LSTCalendar object.

        Parameters
        ----------
        start : Union[str, datetime]
            Start date of the calendar range.
        end : Union[str, datetime]
            End date of the calendar range.
        latitude : Union[str, float], optional
            Latitude for the location. Defaults to 0.
        longitude : Union[str, float], optional
            Longitude for the location. Defaults to 0.

        Raises
        ------
        ValueError
            If the start date is after the end date.
        """
        start = normalize_yyyymmdd_to_datetime(start)
        end = normalize_yyyymmdd_to_datetime(end)

        if start > end:
            raise ValueError("start day should be <= end day")

        latitude, longitude = normalize_coordinates(latitude, longitude)
        self.latitude = latitude
        self.longitude = longitude
        self.lst_calendar_index = Idx()
        self.lst_block_index = Idx()
        self._observation_blocks: List["ObservationBlock"] = []

        # For caching the 'tomorrow' sun, relative to current day
        # This allows for sun_stats(..) to be called once per day,
        # Instead of once for today/tomorrow for every day
        _sun = None

        self.dates: List["LSTCalendarDate"] = []
        for d in range(0, (end - start).days + 1):
            dt = start + timedelta(days=d)
            sun = Sun(self.latitude, self.longitude, dt)
            tomorrow_sun = (
                Sun(self.latitude, self.longitude, dt + timedelta(days=1)) if _sun is None else _sun
            )

            intervals = calculate_intervals(self.latitude, self.longitude, dt)
            for interval in intervals:
                self.lst_calendar_index.insert(interval.interval)

            self.dates.append(
                LSTCalendarDate(dt, dt + timedelta(days=1), sun, tomorrow_sun, intervals, self)
            )

    @property
    def observation_blocks(self) -> List["ObservationBlock"]:
        return self._observation_blocks

    @observation_blocks.setter
    def observation_blocks(self, blocks: List["ObservationBlock"] = None):
        if blocks is None:
            blocks = []
        self._observation_blocks = blocks
        for block in blocks:
            block.calendar = self
            self.lst_block_index.insert(
                Interval(
                    *calculate_OBSERVATION_WINDOW(block.lst_window_start, block.lst_window_end),
                    block,
                )
            )

    def pretty_intervals(self):
        return [
            (
                i.dt.strftime("%Y-%m-%d"),
                i.type.name,
                round(i.start, 1),
                round(i.end, 1),
                "DAWN: " + i.sun.dawn.strftime("%H:%M"),
                "SUNRISE: " + i.sun.sunrise.strftime("%H:%M"),
                "SUNSET: " + i.sun.sunset.strftime("%H:%M"),
                "DUSK: " + i.sun.dusk.strftime("%H:%M"),
            )
            for dt in self.dates
            for i in dt.intervals
        ]
