from typing import Callable
import time

def time_a_function(func:Callable):
    def wrapper():
        print("function has started")
        start_time=time.perf_counter()
        func()
        print("function has ended")
        end_time=time.perf_counter()
        print(f"Function took {end_time-start_time}")
    return wrapper
    

@time_a_function
def say_hello():
    print("Hello World")
    
    
if __name__=="__main__":
    say_hello()    