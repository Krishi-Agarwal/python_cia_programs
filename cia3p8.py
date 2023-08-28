def log_decorator(func):
    def wrapper(*args):
        print(f"Calling function {func.__name__} with arguments {args}")
        result = func(*args)
        print(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

add(1, 2)
