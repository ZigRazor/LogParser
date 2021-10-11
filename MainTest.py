from DateFormat import DateFormat
import LogParser
import Date
import Severity
import re


def main():
    log_parser = LogParser.LogParser()
    log_parser.add_file("./test1.txt")

    date = Date.Date()
    date.set_element_name("date")
    date.set_format(r'\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])')
    print(date.get_date_format())
    date.set_date_format(DateFormat.YEAR_MONTH_DAY)
    print(date.get_date_format())
    log_parser.add_element("Date", date)
    log_parser.add_key("Date")

    severity = Severity.Severity()
    severity.set_element_name("severity")
    log_parser.add_element("Severity", severity)
    log_parser.add_key("Severity")

    a = log_parser.parse_log()

    print(a)


if __name__ == "__main__":
    main()
