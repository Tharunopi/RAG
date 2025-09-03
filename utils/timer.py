import time 

def timer(func):
    def wrapper():
        start_time = time.time()
        result = func()
        end_time = time.time()
        time_result = end_time - start_time
        return result, f"time taken to run {wrapper.__name__} function is: {round(time_result, 4)} seconds"
    return wrapper
        