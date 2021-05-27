
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А' , '10Б', '9А'
]


def tutors_klasses_gen(tutors, klasses):
    for key,  tutor in enumerate(tutors):
        yield tutor, None if (key + 1) > len(klasses) else klasses[key]


gen = tutors_klasses_gen(tutors, klasses)

print(type(gen))

print(type(next(gen)))

print(*gen)

print(next(gen))

