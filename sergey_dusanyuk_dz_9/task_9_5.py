
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Drawing of Stationery class is running. {}'.format(self.__repr__()))


class Pen(Stationery):
    def draw(self):
        print('Drawing of Pen class is running. {}'.format(self.__repr__()))


class Pencil(Stationery):
    def draw(self):
        print('Drawing of Pencil class is running. {}'.format(self.__repr__()))


class Handle(Stationery):
    def draw(self):
        print('Drawing of Handle class is running. {}'.format(self.__repr__()))


if __name__ == '__main__':
    stationery = Stationery('stationery')
    stationery.draw()

    pen = Pen('pen')
    pen.draw()

    pencil = Pencil('pencil')
    pencil.draw()

    handle = Handle('handle')
    handle.draw()
