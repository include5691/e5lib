import time
from threading import Event, Thread

def working_loop(func):
    """
    Decorator that runs a function in a loop between a start and end time using a thread and event control
    
    :param func: Function to run in a loop
    :param start: Start time in hours, 9 by default
    :param end: End time in hours, 20 by default
    """
    def wrapper(*args, **kwargs):
        start = kwargs.get('start', 9)
        end = kwargs.get('end', 20)
        event = Event()
        event.set()
        while True:
            if start <= int(time.strftime("%H")) <= end:
                if event.is_set():
                    event.clear()
                    kwargs["event"] = event
                    thread = Thread(target=func, args=args, kwargs=kwargs)
                    thread.start()
            else:
                if not event.is_set():
                    event.set()
                    thread.join()
            time.sleep(60)
    return wrapper

def daily_loop(start_time: str, update_now: bool = False):
    """
    Decorator that runs a function once in a day at a specific time

    :param func: Function to run in a loop
    :param start_time: start time in format HH:MM
    """
    try:
        start_hour, start_minute = start_time.split(':')
        start_hour = int(start_hour)
        start_minute = int(start_minute)
    except ValueError:
        raise ValueError("Invalid time format")
    def decorator(func):
        def wrapper(*args, **kwargs):
            nonlocal update_now
            is_executed = False
            while True:
                current_hour = int(time.strftime("%H"))
                current_minute = int(time.strftime("%M"))
                if current_hour == start_hour and current_minute == start_minute or update_now:
                    update_now = False
                    if not is_executed:
                        is_executed = True
                        func(*args, **kwargs)
                else:
                    is_executed = False
                time.sleep(5)
        return wrapper
    return decorator