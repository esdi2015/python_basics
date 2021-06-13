
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate(self, material_weight_for_one_point, height_of_material):
        result = self._length * self._width * material_weight_for_one_point * height_of_material
        return result


if __name__ == '__main__':
    road = Road(20, 5000)
    calculate_result = road.calculate(25, 5)
    print(calculate_result)
