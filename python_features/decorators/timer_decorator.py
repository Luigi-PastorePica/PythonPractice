from time import time, sleep

def timer(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"{func.__name__} took {end - start:.2f} seconds")
        return result
    return wrapper

@timer
def example_function(repetitions: int, time_per_rep: int = 0.5):
    for _ in range(repetitions):
        sleep(time_per_rep)

def main():
    example_function(3)
    example_function(4, 0.7)

if __name__ == '__main__':
    main()