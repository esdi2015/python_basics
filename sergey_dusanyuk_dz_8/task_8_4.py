
def val_checker(callback):
    def _val_checker(func):
        def wrapper(*args, **kwargs):
            if callback(*args, **kwargs):
                result = func(*args, **kwargs)
            else:
                msg = 'wrong val: {}'.format(*args, **kwargs)
                raise ValueError(msg)
            return result

        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x, *args, **kwargs):
    return x ** 3


@val_checker(lambda x: isinstance(x, int))
def calc_cube_2(x, *args, **kwargs):
    return x ** 3


if __name__ == '__main__':
    a = calc_cube(5)
    print(a)

    a = calc_cube_2(5)
    print(a)

    try:
        a = calc_cube_2('8')
    except ValueError as e:
        print(e.__repr__())

    try:
        a = calc_cube(-8)
    except ValueError as e:
        print(e.__repr__())




