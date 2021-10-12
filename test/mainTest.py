import sys
sys.path.insert(1, '')

from src.dateFormat import DateFormat
from src.logParser import LogParser
from src.date import Date
from src.severity import Severity
from src.filename import Filename


def main():
    log_parser = LogParser()
    log_parser.add_file("./test1.txt")

    date = Date()
    date.set_element_name("date")
    date.set_format(r'\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])')
    print(date.get_date_format())
    date.set_date_format(DateFormat.YEAR_MONTH_DAY)
    print(date.get_date_format())
    log_parser.add_element("Date", date)
    log_parser.add_key("Date")

    severity = Severity()
    severity.set_element_name("severity")
    log_parser.add_element("Severity", severity)
    log_parser.add_key("Severity")

    filename = Filename()
    filename.set_element_name("filename")
    log_parser.add_element("Filename", filename)
    log_parser.add_key("Filename")
    

    a = log_parser.parse_log()

    print(a)


if __name__ == "__main__":
    main()
