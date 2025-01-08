import time

def create_date(timestamp: int) -> str:
    """
    Create date from unix timestamp in %d.%m.%Y format

    :param timestamp: Unix timestamp
    """
    return time.strftime('%d.%m.%Y', time.localtime(timestamp))

def get_today() -> str:
    "Create date from current time in %d.%m.%Y format"
    return time.strftime("%d.%m.%Y")

def get_yesterday() -> str:
    "Create date from yesterday in %d.%m.%Y format"
    return time.strftime("%d.%m.%Y", time.localtime(time.time() - 86400))