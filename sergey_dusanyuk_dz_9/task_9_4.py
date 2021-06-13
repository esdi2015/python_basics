
class Car:
    def __init__(self, color: str, name: str, is_police: bool):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print('The car is running')

    def stop(self):
        self.speed = 0
        print('The car is stopped')

    def turn(self, direction):
        print('The car turns {}'.format(direction))

    def show_speed(self):
        print('Current speed is: {}'.format(self.speed))


class TownCar(Car):
    max_speed = 60

    def __init__(self, color: str, name: str):
        super().__init__(color, name, False)

    def show_speed(self):
        print('Current speed is: {}'.format(self.speed))
        if self.speed > TownCar.max_speed:
            print('Alert: speed {} is too high'.format(self.speed))


class SportCar(Car):
    def __init__(self, color: str, name: str):
        super().__init__(color, name, False)


class WorkCar(Car):
    max_speed = 40

    def __init__(self, color: str, name: str):
        super().__init__(color, name, False)

    def show_speed(self):
        print('Current speed is: {}'.format(self.speed))
        if self.speed > WorkCar.max_speed:
            print('Alert: speed {} is too high'.format(self.speed))


class PoliceCar(Car):
    def __init__(self, color: str, name: str):
        super().__init__(color, name, True)


if __name__ == '__main__':
    print('Town Car')

    town_car = TownCar('name town car', 'color town car')
    print(town_car.is_police)
    print(town_car.name)
    print(town_car.color)

    town_car.go(50)
    town_car.show_speed()

    town_car.go(70)
    town_car.show_speed()

    print('\n')
    print('Police Car')

    police_car = PoliceCar('name police car', 'color police car')
    print(police_car.is_police)
    print(police_car.name)
    print(police_car.color)

    police_car.go(50)
    police_car.show_speed()

    police_car.go(70)
    police_car.show_speed()
