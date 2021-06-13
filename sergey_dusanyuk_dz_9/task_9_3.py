
class Worker:
    def __init__(self, name: str, surname: str, position: str, wage: float, bonus: float):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return 'Full name: {} {}'.format(self.name, self.surname)

    def get_total_income(self):
        _total_income = self._income.get('wage', 0) + self._income.get('bonus', 0)
        return 'Total income: {}'.format(_total_income)


if __name__ == '__main__':
    position_1 = Position('Peter', 'Ivanov', 'director', 12000, 455.5)
    full_name_1 = position_1.get_full_name()
    total_income_1 = position_1.get_total_income()

    print(position_1)
    print(full_name_1)
    print(total_income_1)

    print(position_1.name)
    print(position_1.surname)
    print(position_1.position)
    print(position_1._income)
