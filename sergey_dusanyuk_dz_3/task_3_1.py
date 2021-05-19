
WORDS = {'one': 'один',
         'two': 'два',
         'three': 'три',
         'four': 'четыре',
         'five': 'пять',
         'six': 'шесть',
         'seven': 'семь',
         'eight': 'восемь',
         'nine': 'девять',
         'ten': 'десять'}


def num_translate(eng_word, words_dict):
    return words_dict.get(eng_word)


def num_translate_adv(eng_word, words_dict):
    if eng_word == eng_word.title():
        rus_word = words_dict.get(eng_word.lower())
        if rus_word:
            rus_word = rus_word.title()
    else:
        rus_word = words_dict.get(eng_word)
    return rus_word


if __name__ == '__main__':
    input_word = input('input word - numerals from 0 to 10 ("two" for example): ')
    print(num_translate_adv(input_word.strip(), WORDS))
