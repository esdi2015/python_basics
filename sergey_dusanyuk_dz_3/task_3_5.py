from random import choice


def get_jokes(num: int, repeat=True) -> list:
    """
    Returns num random jokes

    :param num: int, number of jokes to return
    :param repeat: boolean, repeat words in the jokes or not
    :return: list of jokes
    """
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
    print('Jokes with words repeat')
    print(get_jokes(10, True))
    print("\r")

    print('Jokes without words repeat')
    print(get_jokes(10, False))
