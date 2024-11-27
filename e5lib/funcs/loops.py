import time
from threading import Event, Thread

def working_loop(func):
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
                    thread : Thread = Thread(target=func, args=args, kwargs=kwargs)
                    thread.start()
            else:
                if not event.is_set():
                    event.set()
                    thread.join()
            time.sleep(60)
    return wrapper
