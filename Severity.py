from enum import Enum

import GenericElement


class Severity(Enum, GenericElement.GenericElement):
    """
    Severity of the Log.
    """
    TRACE = 1
    DEBUG = 2
    INFO = 3
    ERROR = 4
    CRITICAL = 5
