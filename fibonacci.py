from functools import lru_cache

@lru_cache(maxsize=None)
def fib(num:int)->int:
    if num<=1:
        return num
    else:
        return fib(num-1) + fib(num-2)
    
if __name__ == "__main__":
    print(fib(5))    