from abc import ABC, abstractmethod


class AbstractClothes(ABC):
    @abstractmethod
    def _calculate_cloth(self):
        pass


class Coat(AbstractClothes):
    def __init__(self, size):
        self.name = 'coat size {}'.format(size)
        self.size = size
        self._type = 'coat'
        self.cloth = self._calculate_cloth()

    def _calculate_cloth(self):
        return self.size/6.5 + 0.5


class Suit(AbstractClothes):
    def __init__(self, height):
        self.name = 'suit height {}'.format(height)
        self.height = height
        self._type = 'suit'
        self.cloth = self._calculate_cloth()

    def _calculate_cloth(self):
        return 2*self.height + 0.3


class ClothesProducer:
    def __init__(self):
        self.clothes_list = []

    def add_clothes(self, clothes):
        self.clothes_list.append(clothes)

    @property
    def total_clothes_amount(self):
        return round(sum([c.cloth for c in self.clothes_list]), 2)


if __name__ == '__main__':
    coat_1 = Coat(6.5)
    coat_2 = Coat(13)
    suit_1 = Suit(1)
    suit_2 = Suit(2)

    clothes_list = [coat_1, coat_2, suit_1, suit_2]

    clothes_producer = ClothesProducer()
    for c in clothes_list:
        clothes_producer.add_clothes(c)

    print('Total clothes amount is {}'.format(clothes_producer.total_clothes_amount))
