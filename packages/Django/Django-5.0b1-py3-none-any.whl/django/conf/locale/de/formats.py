# This file is distributed under the same license as the Django package.
#
# The *_FORMAT strings use the Django date format syntax,
# see https://docs.djangoproject.com/en/dev/ref/templates/builtins/#date
DATE_FORMAT = "j. F Y"
TIME_FORMAT = "H:i"
DATETIME_FORMAT = "j. F Y H:i"
YEAR_MONTH_FORMAT = "F Y"
MONTH_DAY_FORMAT = "j. F"
SHORT_DATE_FORMAT = "d.m.Y"
SHORT_DATETIME_FORMAT = "d.m.Y H:i"
FIRST_DAY_OF_WEEK = 1  # Monday

# The *_INPUT_FORMATS strings use the Python strftime format syntax,
# see https://docs.python.org/library/datetime.html#strftime-strptime-behavior
DATE_INPUT_FORMATS = [
    "%d.%m.%Y",  # '25.10.2006'
    "%d.%m.%y",  # '25.10.06'
    # "%d. %B %Y",  # '25. October 2006'
    # "%d. %b. %Y",  # '25. Oct. 2006'
]
DATETIME_INPUT_FORMATS = [
    "%d.%m.%Y %H:%M:%S",  # '25.10.2006 14:30:59'
    "%d.%m.%Y %H:%M:%S.%f",  # '25.10.2006 14:30:59.000200'
    "%d.%m.%Y %H:%M",  # '25.10.2006 14:30'
]
DECIMAL_SEPARATOR = ","
THOUSAND_SEPARATOR = "."
NUMBER_GROUPING = 3
