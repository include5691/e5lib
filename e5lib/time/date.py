import time
from e5lib.utils import args_parser
from au_b24 import to_unix_time

args_parser.add_argument("-d", "--date", type=str, help="Date to start from")


def create_date(timestamp: int) -> str:
    """
    Create date from unix timestamp in %d.%m.%Y format

    :param timestamp: Unix timestamp
    """
    return time.strftime("%d.%m.%Y", time.localtime(timestamp))


def create_timestamp(date: str) -> int | None:
    """
    Create unix timestamp from date string in %d.%m.%Y or full date format (ISO 8601)
    """
    if "." in date and len(date) == 10:
        return int(time.mktime(time.strptime(date, "%d.%m.%Y")))
    return to_unix_time(date)


def get_today() -> str:
    "Create date from current time in %d.%m.%Y format"
    return time.strftime("%d.%m.%Y")


def get_yesterday(date: str = None) -> str:
    """
    Get yesterday's date from a given date or current time in %d.%m.%Y format
    """
    if date:
        timestamp = to_unix_time(date)
    else:
        timestamp = time.time()
    unix_time = timestamp - 86400
    return time.strftime("%d.%m.%Y", time.localtime(unix_time))


def get_tomorrow(date: str = None) -> str:
    """
    Get tomorrow's date from a given date or current time in %d.%m.%Y format
    """
    if date:
        timestamp = to_unix_time(date)
    else:
        timestamp = time.time()
    unix_time = timestamp + 86400
    return time.strftime("%d.%m.%Y", time.localtime(unix_time))


def get_date_from_args(single_use: bool = False) -> str | None:
    """
    Get date from command line arguments in %d.%m.%Y format

    :param single_use: If True, date returns only once
    """
    console_args = args_parser.parse_args()
    try:
        time.strptime(console_args.date, "%d.%m.%Y")
        date = console_args.date
        if single_use:
            console_args.date = None
        return date
    except (TypeError, ValueError):
        return None
