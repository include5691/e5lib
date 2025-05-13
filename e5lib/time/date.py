import time
from e5lib.utils import args_parser

args_parser.add_argument("-d", "--date", type=str, help="Date to start from")


def create_date(timestamp: int) -> str:
    """
    Create date from unix timestamp in %d.%m.%Y format

    :param timestamp: Unix timestamp
    """
    return time.strftime("%d.%m.%Y", time.localtime(timestamp))


def get_today() -> str:
    "Create date from current time in %d.%m.%Y format"
    return time.strftime("%d.%m.%Y")


def get_yesterday() -> str:
    "Create date from yesterday in %d.%m.%Y format"
    return time.strftime("%d.%m.%Y", time.localtime(time.time() - 86400))


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
