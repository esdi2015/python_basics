from random import choice
from random import randrange


def get_jokes(num, repeat=True):
    jokes = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    for i in range(num):
        if (len(nouns) > 0) and (len(adverbs) > 0) and (len(adjectives) > 0):
            noun = choice(nouns)
            adverb = choice(adverbs)
            adjective = choice(adjectives)
            if not repeat:
                nouns.pop(nouns.index(noun))
                adverbs.pop(adverbs.index(adverb))
                adjectives.pop(adjectives.index(adjective))
            jokes.append('{} {} {}'.format(noun, adverb, adjective))
    return jokes


if __name__ == '__main__':
    print(get_jokes(10, True))
    print(get_jokes(10, False))
