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
