import time
import functools

def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = (end_time - start_time) * 1000  # Convert to milliseconds
        
        module_name = func.__module__
        
        print(f"Running solution for {module_name}")
        print(f"SOLUTION: {result}")
        print(f"Solution took {duration:.2f}ms")
        return result
    return wrapper