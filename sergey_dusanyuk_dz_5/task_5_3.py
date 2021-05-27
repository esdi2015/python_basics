
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


tutors_1 = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses_1 = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'
]


def tutors_klasses_gen(tutors, klasses):
    for key,  tutor in enumerate(tutors):
        yield tutor, None if (key + 1) > len(klasses) else klasses[key]


gen = tutors_klasses_gen(tutors, klasses)

print(type(gen))
print(*gen)

try:
    print(next(gen))
except StopIteration as e:
    print(e.__repr__())


gen_1 = tutors_klasses_gen(tutors_1, klasses_1)

print(type(gen_1))
print(*gen_1)

try:
    print(next(gen_1))
except StopIteration as e:
    print(e.__repr__())

