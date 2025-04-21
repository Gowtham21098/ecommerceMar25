def greet_decorator(func):
    def wrapper(*args, **kwargs):
        print('hello All')
        return func(*args, **kwargs)
    return wrapper


@greet_decorator
def greet():
    print('Hello World')


if __name__ == '__main__':
    greet()