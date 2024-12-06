import time

def create_date(timestamp: int) -> str:
    """
    Create date from unix timestamp in %d.%m.%Y format

    :param timestamp: Unix timestamp
    """
    return time.strftime('%d.%m.%Y', time.localtime(timestamp))