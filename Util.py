from datetime import datetime
import functools
import time


def timer_sec(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time

        with open("time_log.txt", "a") as f:
            final_time = f'\nFinished {func.__name__!r} in {run_time:.4f} secs ; time_stamp: {datetime.now()}'
            f.write(final_time)
            print(f'\nFinished {func.__name__!r} in {run_time:.4f} secs ; time_stamp: {datetime.now()}')

        return value
    return wrapper_timer