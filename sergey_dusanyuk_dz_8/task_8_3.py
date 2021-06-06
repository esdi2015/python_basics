from functools import wraps


def type_logger(func):
    @wraps(func)
    def args_wrapper(*args, **kwargs):
        print('args:')
        print(*map(type, args), sep=',')
        print('kwargs:')
        print(*map(type, kwargs.values()), sep=',')
        res = func(*args, **kwargs)
        print('function result type:')
        print(type(res))
        print('function name:')
        print(func.__name__)
        return res

    return args_wrapper


@type_logger
def calc_cube(x, *args, **kwargs):
    return x ** 3


if __name__ == '__main__':
    a = calc_cube(5, 34.6, kw1='1', kw2=24)
    print(a)


