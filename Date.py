import GenericElement

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
        date_string = date_string.split()
        date_string = date_string[0].split('-')
        self.year = int(date_string[0])
        self.month = int(date_string[1])
        self.day = int(date_string[2])
        date_string = date_string[0].split(':')
        self.hour = int(date_string[0])
        self.minute = int(date_string[1])
        self.second = int(date_string[2])
        date_string = date_string[0].split('.')
        self.microsecond = int(date_string[0])

    def get_date_string(self):
        """Return date as string"""
        return f"{self.year}-{self.month}-{self.day} {self.hour}:{self.minute}:{self.second}.{self.microsecond}"

    def get_date_string_without_time(self):
        """Return date as string without time"""
        return f"{self.year}-{self.month}-{self.day}"

    def get_date_string_without_microseconds(self):
        """Return date as string without time and microseconds"""
        return f"{self.year}-{self.month}-{self.day} {self.hour}:{self.minute}:{self.second}"
        