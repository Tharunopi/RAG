import time 

def timer(func):
    def wrapper():
        start_time = time.time()
        result = func()
        end_time = time.time()
        