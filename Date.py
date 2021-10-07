import GenericElement
import DateFormat
import re


class Date(GenericElement.GenericElement):
    """Date Class"""

    def __init__(self):
        """Initialize Date Class"""
        self.year = 0
        self.month = 0
        self.day = 0
        self.hour = 0
        self.minute = 0
        self.second = 0
        self.microsecond = 0
        self.date_format = DateFormat.DateFormat.YEAR_MONTH_DAY_HOUR_MINUTE_SECOND_MICROSECOND

    def __str__(self):
        """Return string representation of date"""
        return f"{self.year}-{self.month}-{self.day} {self.hour}:{self.minute}:{self.second}.{self.microsecond}"

    def __repr__(self):
        """Return string representation of date"""
        return f"{self.year}-{self.month}-{self.day} {self.hour}:{self.minute}:{self.second}.{self.microsecond}"

    def __eq__(self, other):
        """Return True if dates are equal"""
        return self.year == other.year and self.month == other.month and self.day == other.day and self.hour == other.hour and self.minute == other.minute and self.second == other.second and self.microsecond == other.microsecond

    def __lt__(self, other):
        """Return True if self is less than other"""
        return self.year < other.year or self.month < other.month or self.day < other.day or self.hour < other.hour or self.minute < other.minute or self.second < other.second or self.microsecond < other.microsecond

    def __le__(self, other):
        """Return True if self is less than or equal to other"""
        return self.year <= other.year or self.month <= other.month or self.day <= other.day or self.hour <= other.hour or self.minute <= other.minute or self.second <= other.second or self.microsecond <= other.microsecond

    def __gt__(self, other):
        """Return True if self is greater than other"""
        return self.year > other.year or self.month > other.month or self.day > other.day or self.hour > other.hour or self.minute > other.minute or self.second > other.second or self.microsecond > other.microsecond

    def __ge__(self, other):
        """Return True if self is greater than or equal to other"""
        return self.year >= other.year or self.month >= other.month or self.day >= other.day or self.hour >= other.hour or self.minute >= other.minute or self.second >= other.second or self.microsecond >= other.microsecond

    def __ne__(self, other):
        """Return True if self is not equal to other"""
        return not self == other

    def get_year(self):
        """Return year"""
        return self.year

    def get_month(self):
        """Return month"""
        return self.month

    def get_day(self):
        """Return day"""
        return self.day

    def get_hour(self):
        """Return hour"""
        return self.hour

    def get_minute(self):
        """Return minute"""
        return self.minute

    def get_second(self):
        """Return second"""
        return self.second

    def get_microsecond(self):
        """Return microsecond"""
        return self.microsecond

    def set_year(self, year):
        """Set year"""
        self.year = year

    def set_month(self, month):
        """Set month"""
        self.month = month

    def set_day(self, day):
        """Set day"""
        self.day = day

    def set_hour(self, hour):
        """Set hour"""
        self.hour = hour

    def set_minute(self, minute):
        """Set minute"""
        self.minute = minute

    def set_second(self, second):
        """Set second"""
        self.second = second

    def set_microsecond(self, microsecond):
        """Set microsecond"""
        self.microsecond = microsecond

    def set_date_format(self, date_format: DateFormat.DateFormat):
        """Set date format"""
        self.date_format = date_format

    def get_date_format(self):
        """Return date format"""
        return self.date_format

    def set_date(self, year, month, day, hour, minute, second, microsecond):
        """Set date"""
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        self.microsecond = microsecond

    def set_date_from_string(self, date_string):
        """Set date from string"""
        #date_string = date_string.split()
        #date_string = date_string[0].split('-')
        print(date_string)
        date_string = re.split(r' |\-|\:|\.', date_string)
        print(date_string)
        date_string_len = len(date_string)
        index = 0
        if index < date_string_len and date_string[index].isdigit():
            if self._first_digit_year():
                self.year = int(date_string[index])
                index += 1
            elif self._first_digit_day():
                self.day = int(date_string[index])
                index += 1
            elif self._first_digit_month():
                self.month = int(date_string[index])
                index += 1
            else:
                raise Exception("Date format not supported")

        else:
            return
        if index < date_string_len and date_string[index].isdigit():
            if self._second_digit_month():
                self.month = int(date_string[index])
                index += 1
            elif self._second_digit_day():
                self.day = int(date_string[index])
                index += 1
            elif self._second_digit_year():
                self.year = int(date_string[index])
                index += 1
            else:
                raise Exception("Date format not supported")
        else:
            return
        if index < date_string_len and date_string[index].isdigit():
            if self._third_digit_day():
                self.day = int(date_string[index])
                index += 1
            elif self._third_digit_year():
                self.year = int(date_string[index])
                index += 1
            elif self._third_digit_month():
                self.month = int(date_string[index])
                index += 1
            else:
                raise Exception("Date format not supported")
        else:
            return
        if index < date_string_len and date_string[index].isdigit():
            if self._has_hour():
                self.hour = int(date_string[index])
                index += 1
            else:
                self.hour = 0
                return
        else:
            return
        if index < date_string_len and date_string[index].isdigit():
            if self._has_minute():
                self.minute = int(date_string[index])
                index += 1
            else:
                self.minute = 0
                return
        else:
            return
        if index < date_string_len and date_string[index].isdigit():
            if self._has_second():
                self.second = int(date_string[index])
                index += 1
            else:
                self.second = 0
                return
        else:
            return
        if index < date_string_len and date_string[index].isdigit():
            if self._has_microsecond():
                self.microsecond = int(date_string[index])
                index += 1
            else:
                self.microsecond = 0
                return
        return

    def _has_microsecond(self):
        return self.date_format in (DateFormat.DateFormat.YEAR_DAY_MONTH_HOUR_MINUTE_SECOND_MICROSECOND, DateFormat.DateFormat.YEAR_MONTH_DAY_HOUR_MINUTE_SECOND_MICROSECOND, DateFormat.DateFormat.DAY_YEAR_MONTH_HOUR_MINUTE_SECOND_MICROSECOND, DateFormat.DateFormat.DAY_MONTH_YEAR_HOUR_MINUTE_SECOND_MICROSECOND, DateFormat.DateFormat.MONTH_DAY_YEAR_HOUR_MINUTE_SECOND_MICROSECOND, DateFormat.DateFormat.MONTH_YEAR_DAY_HOUR_MINUTE_SECOND_MICROSECOND)

    def _has_second(self):
        return self.date_format in (DateFormat.DateFormat.YEAR_DAY_MONTH_HOUR_MINUTE_SECOND_MICROSECOND, DateFormat.DateFormat.YEAR_DAY_MONTH_HOUR_MINUTE_SECOND, DateFormat.DateFormat.YEAR_MONTH_DAY_HOUR_MINUTE_SECOND_MICROSECOND, DateFormat.DateFormat.YEAR_MONTH_DAY_HOUR_MINUTE_SECOND, DateFormat.DateFormat.DAY_YEAR_MONTH_HOUR_MINUTE_SECOND_MICROSECOND, DateFormat.DateFormat.DAY_YEAR_MONTH_HOUR_MINUTE_SECOND, DateFormat.DateFormat.DAY_MONTH_YEAR_HOUR_MINUTE_SECOND_MICROSECOND, DateFormat.DateFormat.DAY_MONTH_YEAR_HOUR_MINUTE_SECOND, DateFormat.DateFormat.MONTH_DAY_YEAR_HOUR_MINUTE_SECOND_MICROSECOND, DateFormat.DateFormat.MONTH_DAY_YEAR_HOUR_MINUTE_SECOND, DateFormat.DateFormat.MONTH_YEAR_DAY_HOUR_MINUTE_SECOND_MICROSECOND, DateFormat.DateFormat.MONTH_YEAR_DAY_HOUR_MINUTE_SECOND)

    def _has_minute(self):
        return self.date_format in (DateFormat.DateFormat.YEAR_DAY_MONTH_HOUR_MINUTE_SECOND_MICROSECOND, DateFormat.DateFormat.YEAR_DAY_MONTH_HOUR_MINUTE_SECOND, DateFormat.DateFormat.YEAR_DAY_MONTH_HOUR_MINUTE, DateFormat.DateFormat.YEAR_MONTH_DAY_HOUR_MINUTE_SECOND_MICROSECOND, DateFormat.DateFormat.YEAR_MONTH_DAY_HOUR_MINUTE_SECOND, DateFormat.DateFormat.YEAR_MONTH_DAY_HOUR_MINUTE, DateFormat.DateFormat.DAY_YEAR_MONTH_HOUR_MINUTE_SECOND_MICROSECOND, DateFormat.DateFormat.DAY_YEAR_MONTH_HOUR_MINUTE_SECOND, DateFormat.DateFormat.DAY_YEAR_MONTH_HOUR_MINUTE, DateFormat.DateFormat.DAY_MONTH_YEAR_HOUR_MINUTE_SECOND_MICROSECOND, DateFormat.DateFormat.DAY_MONTH_YEAR_HOUR_MINUTE_SECOND, DateFormat.DateFormat.DAY_MONTH_YEAR_HOUR_MINUTE, DateFormat.DateFormat.MONTH_DAY_YEAR_HOUR_MINUTE_SECOND_MICROSECOND, DateFormat.DateFormat.MONTH_DAY_YEAR_HOUR_MINUTE_SECOND, DateFormat.DateFormat.MONTH_DAY_YEAR_HOUR_MINUTE, DateFormat.DateFormat.MONTH_YEAR_DAY_HOUR_MINUTE_SECOND_MICROSECOND, DateFormat.DateFormat.MONTH_YEAR_DAY_HOUR_MINUTE_SECOND, DateFormat.DateFormat.MONTH_YEAR_DAY_HOUR_MINUTE)

    def _has_hour(self):
        return self.date_format in (DateFormat.DateFormat.YEAR_DAY_MONTH_HOUR_MINUTE_SECOND_MICROSECOND, DateFormat.DateFormat.YEAR_DAY_MONTH_HOUR_MINUTE_SECOND, DateFormat.DateFormat.YEAR_DAY_MONTH_HOUR_MINUTE, DateFormat.DateFormat.YEAR_DAY_MONTH_HOUR, DateFormat.DateFormat.YEAR_MONTH_DAY_HOUR_MINUTE_SECOND_MICROSECOND, DateFormat.DateFormat.YEAR_MONTH_DAY_HOUR_MINUTE_SECOND, DateFormat.DateFormat.YEAR_MONTH_DAY_HOUR_MINUTE, DateFormat.DateFormat.YEAR_MONTH_DAY_HOUR, DateFormat.DateFormat.DAY_YEAR_MONTH_HOUR_MINUTE_SECOND_MICROSECOND, DateFormat.DateFormat.DAY_YEAR_MONTH_HOUR_MINUTE_SECOND, DateFormat.DateFormat.DAY_YEAR_MONTH_HOUR_MINUTE, DateFormat.DateFormat.DAY_YEAR_MONTH_HOUR, DateFormat.DateFormat.DAY_MONTH_YEAR_HOUR_MINUTE_SECOND_MICROSECOND, DateFormat.DateFormat.DAY_MONTH_YEAR_HOUR_MINUTE_SECOND, DateFormat.DateFormat.DAY_MONTH_YEAR_HOUR_MINUTE, DateFormat.DateFormat.DAY_MONTH_YEAR_HOUR, DateFormat.DateFormat.MONTH_DAY_YEAR_HOUR_MINUTE_SECOND_MICROSECOND, DateFormat.DateFormat.MONTH_DAY_YEAR_HOUR_MINUTE_SECOND, DateFormat.DateFormat.MONTH_DAY_YEAR_HOUR_MINUTE, DateFormat.DateFormat.MONTH_DAY_YEAR_HOUR, DateFormat.DateFormat.MONTH_YEAR_DAY_HOUR_MINUTE_SECOND_MICROSECOND, DateFormat.DateFormat.MONTH_YEAR_DAY_HOUR_MINUTE_SECOND, DateFormat.DateFormat.MONTH_YEAR_DAY_HOUR_MINUTE, DateFormat.DateFormat.MONTH_YEAR_DAY_HOUR)

    def _third_digit_month(self):
        return self.date_format in (DateFormat.DateFormat.YEAR_DAY_MONTH_HOUR_MINUTE_SECOND_MICROSECOND, DateFormat.DateFormat.YEAR_DAY_MONTH_HOUR_MINUTE_SECOND, DateFormat.DateFormat.YEAR_DAY_MONTH_HOUR_MINUTE, DateFormat.DateFormat.YEAR_DAY_MONTH_HOUR, DateFormat.DateFormat.YEAR_DAY_MONTH, DateFormat.DateFormat.DAY_YEAR_MONTH_HOUR_MINUTE_SECOND_MICROSECOND, DateFormat.DateFormat.DAY_YEAR_MONTH_HOUR_MINUTE_SECOND, DateFormat.DateFormat.DAY_YEAR_MONTH_HOUR_MINUTE, DateFormat.DateFormat.DAY_YEAR_MONTH_HOUR, DateFormat.DateFormat.DAY_YEAR_MONTH)

    def _third_digit_year(self):
        return self.date_format in (DateFormat.DateFormat.DAY_MONTH_YEAR_HOUR_MINUTE_SECOND_MICROSECOND, DateFormat.DateFormat.DAY_MONTH_YEAR_HOUR_MINUTE_SECOND, DateFormat.DateFormat.DAY_MONTH_YEAR_HOUR_MINUTE, DateFormat.DateFormat.DAY_MONTH_YEAR_HOUR, DateFormat.DateFormat.DAY_MONTH_YEAR, DateFormat.DateFormat.MONTH_DAY_YEAR_HOUR_MINUTE_SECOND_MICROSECOND, DateFormat.DateFormat.MONTH_DAY_YEAR_HOUR_MINUTE_SECOND, DateFormat.DateFormat.MONTH_DAY_YEAR_HOUR_MINUTE, DateFormat.DateFormat.MONTH_DAY_YEAR_HOUR, DateFormat.DateFormat.MONTH_DAY_YEAR)

    def _third_digit_day(self):
        return self.date_format in (DateFormat.DateFormat.YEAR_MONTH_DAY_HOUR_MINUTE_SECOND_MICROSECOND, DateFormat.DateFormat.YEAR_MONTH_DAY_HOUR_MINUTE_SECOND, DateFormat.DateFormat.YEAR_MONTH_DAY_HOUR_MINUTE, DateFormat.DateFormat.YEAR_MONTH_DAY_HOUR, DateFormat.DateFormat.YEAR_MONTH_DAY, DateFormat.DateFormat.MONTH_YEAR_DAY_HOUR_MINUTE_SECOND_MICROSECOND, DateFormat.DateFormat.MONTH_YEAR_DAY_HOUR_MINUTE_SECOND, DateFormat.DateFormat.MONTH_YEAR_DAY_HOUR_MINUTE, DateFormat.DateFormat.MONTH_YEAR_DAY_HOUR, DateFormat.DateFormat.MONTH_YEAR_DAY)

    def _second_digit_year(self):
        return self.date_format in (DateFormat.DateFormat.MONTH_YEAR_DAY_HOUR_MINUTE_SECOND_MICROSECOND, DateFormat.DateFormat.MONTH_YEAR_DAY_HOUR_MINUTE_SECOND, DateFormat.DateFormat.MONTH_YEAR_DAY_HOUR_MINUTE, DateFormat.DateFormat.MONTH_YEAR_DAY_HOUR, DateFormat.DateFormat.MONTH_YEAR_DAY, DateFormat.DateFormat.DAY_YEAR_MONTH_HOUR_MINUTE_SECOND_MICROSECOND, DateFormat.DateFormat.DAY_YEAR_MONTH_HOUR_MINUTE_SECOND, DateFormat.DateFormat.DAY_YEAR_MONTH_HOUR_MINUTE, DateFormat.DateFormat.DAY_YEAR_MONTH_HOUR, DateFormat.DateFormat.DAY_YEAR_MONTH)

    def _second_digit_day(self):
        return self.date_format in (DateFormat.DateFormat.YEAR_DAY_MONTH_HOUR_MINUTE_SECOND_MICROSECOND, DateFormat.DateFormat.YEAR_DAY_MONTH_HOUR_MINUTE_SECOND, DateFormat.DateFormat.YEAR_DAY_MONTH_HOUR_MINUTE, DateFormat.DateFormat.YEAR_DAY_MONTH_HOUR, DateFormat.DateFormat.YEAR_DAY_MONTH, DateFormat.DateFormat.MONTH_DAY_YEAR_HOUR_MINUTE_SECOND_MICROSECOND, DateFormat.DateFormat.MONTH_DAY_YEAR_HOUR_MINUTE_SECOND, DateFormat.DateFormat.MONTH_DAY_YEAR_HOUR_MINUTE, DateFormat.DateFormat.MONTH_DAY_YEAR_HOUR, DateFormat.DateFormat.MONTH_DAY_YEAR)

    def _second_digit_month(self):
        return self.date_format in (DateFormat.DateFormat.YEAR_MONTH_DAY_HOUR_MINUTE_SECOND_MICROSECOND, DateFormat.DateFormat.YEAR_MONTH_DAY_HOUR_MINUTE_SECOND, DateFormat.DateFormat.YEAR_MONTH_DAY_HOUR_MINUTE, DateFormat.DateFormat.YEAR_MONTH_DAY_HOUR, DateFormat.DateFormat.YEAR_MONTH_DAY, DateFormat.DateFormat.DAY_MONTH_YEAR_HOUR_MINUTE_SECOND_MICROSECOND, DateFormat.DateFormat.DAY_MONTH_YEAR_HOUR_MINUTE_SECOND, DateFormat.DateFormat.DAY_MONTH_YEAR_HOUR_MINUTE, DateFormat.DateFormat.DAY_MONTH_YEAR_HOUR, DateFormat.DateFormat.DAY_MONTH_YEAR)

    def _first_digit_month(self):
        return self.date_format in (DateFormat.DateFormat.MONTH_DAY_YEAR_HOUR_MINUTE_SECOND_MICROSECOND, DateFormat.DateFormat.MONTH_DAY_YEAR_HOUR_MINUTE_SECOND, DateFormat.DateFormat.MONTH_DAY_YEAR_HOUR_MINUTE, DateFormat.DateFormat.MONTH_DAY_YEAR_HOUR, DateFormat.DateFormat.MONTH_DAY_YEAR, DateFormat.DateFormat.MONTH_YEAR_DAY_HOUR_MINUTE_SECOND_MICROSECOND, DateFormat.DateFormat.MONTH_YEAR_DAY_HOUR_MINUTE_SECOND, DateFormat.DateFormat.MONTH_YEAR_DAY_HOUR_MINUTE, DateFormat.DateFormat.MONTH_YEAR_DAY_HOUR, DateFormat.DateFormat.MONTH_YEAR_DAY)

    def _first_digit_day(self):
        return self.date_format in (DateFormat.DateFormat.DAY_MONTH_YEAR_HOUR_MINUTE_SECOND_MICROSECOND, DateFormat.DateFormat.DAY_MONTH_YEAR_HOUR_MINUTE_SECOND, DateFormat.DateFormat.DAY_MONTH_YEAR_HOUR_MINUTE, DateFormat.DateFormat.DAY_MONTH_YEAR_HOUR, DateFormat.DateFormat.DAY_MONTH_YEAR, DateFormat.DateFormat.DAY_YEAR_MONTH_HOUR_MINUTE_SECOND_MICROSECOND, DateFormat.DateFormat.DAY_YEAR_MONTH_HOUR_MINUTE_SECOND, DateFormat.DateFormat.DAY_YEAR_MONTH_HOUR_MINUTE, DateFormat.DateFormat.DAY_YEAR_MONTH_HOUR, DateFormat.DateFormat.DAY_YEAR_MONTH)

    def _first_digit_year(self):
        return self.date_format in (DateFormat.DateFormat.YEAR_MONTH_DAY_HOUR_MINUTE_SECOND_MICROSECOND, DateFormat.DateFormat.YEAR_MONTH_DAY_HOUR_MINUTE_SECOND, DateFormat.DateFormat.YEAR_MONTH_DAY_HOUR_MINUTE, DateFormat.DateFormat.YEAR_MONTH_DAY_HOUR, DateFormat.DateFormat.YEAR_MONTH_DAY, DateFormat.DateFormat.YEAR_DAY_MONTH_HOUR_MINUTE_SECOND_MICROSECOND, DateFormat.DateFormat.YEAR_DAY_MONTH_HOUR_MINUTE_SECOND, DateFormat.DateFormat.YEAR_DAY_MONTH_HOUR_MINUTE, DateFormat.DateFormat.YEAR_DAY_MONTH_HOUR, DateFormat.DateFormat.YEAR_DAY_MONTH)

    def get_date_string(self):
        """Return date as string"""
        return f"{self.year}-{self.month}-{self.day} {self.hour}:{self.minute}:{self.second}.{self.microsecond}"

    def get_date_string_without_time(self):
        """Return date as string without time"""
        return f"{self.year}-{self.month}-{self.day}"

    def get_date_string_without_microseconds(self):
        """Return date as string without time and microseconds"""
        return f"{self.year}-{self.month}-{self.day} {self.hour}:{self.minute}:{self.second}"
