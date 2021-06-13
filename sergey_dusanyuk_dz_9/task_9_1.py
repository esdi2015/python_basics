import time


class ColorError(Exception):
    pass


class ColorOrderError(Exception):
    pass


class TrafficLight:
    _run_scheme = {'red': 7, 'yellow': 2, 'green': 5}

    def __init__(self):
        self.__color = None

    def running(self, color: str):
        color = color.lower()
        TrafficLight._is_correct_color(color)
        self.__check_run_order(color)
        self.__color = color
        print('TrafficLight is "{}"'.format(self.__color))
        time.sleep(TrafficLight._run_scheme[self.__color])

    @classmethod
    def _is_correct_color(cls, color):
        if color not in cls._run_scheme.keys():
            raise ColorError("invalid color. color=['red', 'yellow', 'green']")

    def __check_run_order(self, color):
        if self.__color is not None:
            if self.__color == 'red' and color != 'yellow':
                raise ColorOrderError('after red should be yellow color')
            if self.__color == 'yellow' and color != 'green':
                raise ColorOrderError('after yellow should be green color')
            if self.__color == 'green' and color != 'red':
                raise ColorOrderError('after green should be red color')


if __name__ == '__main__':
    traffic_light = TrafficLight()

    try:
        traffic_light.running('red')
        traffic_light.running('yellow')
        traffic_light.running('green')
    except ColorError as e:
        print(e.__repr__())
        exit(1)
    except ColorOrderError as e:
        print(e.__repr__())
        exit(2)

    try:
        traffic_light.running('red')
        traffic_light.running('green')
    except ColorError as e:
        print(e.__repr__())
        exit(1)
    except ColorOrderError as e:
        print(e.__repr__())
        exit(2)

