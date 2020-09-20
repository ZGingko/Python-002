import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        begin = time.time()
        result = func(*args, ** kwargs)
        end = time.time()
        print(f'{func.__name__} executed in {end - begin} ms')
        return result
    return wrapper

@timer
def test1():
    time.sleep(0.012)
    return

@timer
def test2():
    time.sleep(1.2)
    return

@timer
def test3(n):
    while(n > 0):
        print(n)
        n -= 1
    print(n)
    return


if __name__ == "__main__":
    test1()
    test2()
    test3(100000)