from enum import Enum

import GenericElement


class SeverityEnum(Enum):
    """
    Severity Enum of the Log.
    """
    TRACE = 1
    DEBUG = 2
    INFO = 3
    ERROR = 4
    CRITICAL = 5


class Severity(GenericElement.GenericElement):
    """
    Severity of the Log.
    """

    def __init__(self):
        """ Constructor of Severity Class"""
        super().__init__()
        # super().set_format("/trace|debug|info|error|critical/gi")
        super().set_format('(?i)trace|debug|info|error|critical')
        self.severity = SeverityEnum.INFO

    def set_severity(self, severity):
        """
        Set the severity of the log.
        :param severity: Severity_Enum
        :return: None
        """
        self.severity = severity

    def get_severity(self):
        """
        Get the severity of the log.
        :return: Severity_Enum
        """
        return self.severity

    def __str__(self):
        """
        Return the string representation of the severity.
        :return: str
        """
        return str(self.severity)

    def __repr__(self):
        """
        Return the representation of the severity.
        :return: str
        """
        return str(self.severity)

    def __eq__(self, other):
        """
        Compare the severity with another severity.
        :param other: Severity_Enum
        :return: bool
        """
        return self.severity == other.severity

    def __ne__(self, other):
        """
        Compare the severity with another severity.
        :param other: Severity_Enum
        :return: bool
        """
        return self.severity != other.severity

    def __lt__(self, other):
        """
        Compare the severity with another severity.
        :param other: Severity_Enum
        :return: bool
        """
        return self.severity < other.severity

    def __le__(self, other):
        """
        Compare the severity with another severity.
        :param other: Severity_Enum
        :return: bool
        """
        return self.severity <= other.severity

    def __gt__(self, other):
        """
        Compare the severity with another severity.
        :param other: Severity_Enum
        :return: bool
        """
        return self.severity > other.severity

    def __ge__(self, other):
        """
        Compare the severity with another severity.
        :param other: Severity_Enum
        :return: bool
        """
        return self.severity >= other.severity

    def __hash__(self):
        """
        Return the hash of the severity.
        :return: int
        """
        return hash(self.severity)

    def __getstate__(self):
        """
        Return the state of the severity.
        :return: dict
        """
        return self.__dict__

    def __setstate__(self, state):
        """
        Set the state of the severity.
        :param state: dict
        :return: None
        """
        self.__dict__ = state

    def set_severity_from_string(self, severity_string: str):
        """
        Set the severity from a string.
        :param severity_string: str
        :return: None
        """

        severity_string.upper()
        if severity_string == "TRACE":
            self.severity = SeverityEnum.TRACE
        elif severity_string == "DEBUG":
            self.severity = SeverityEnum.DEBUG
        elif severity_string == "INFO":
            self.severity = SeverityEnum.INFO
        elif severity_string == "ERROR":
            self.severity = SeverityEnum.ERROR
        elif severity_string == "CRITICAL":
            self.severity = SeverityEnum.CRITICAL
        else:
            raise ValueError("Invalid Severity String")
