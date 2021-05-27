
num = 20


def odd_nums_gen_2(max_num):
    return (i for i in range(1, max_num, 2))


odd_nums_2 = odd_nums_gen_2(num)

print(type(odd_nums_2))
print(*odd_nums_2, sep=', ')

try:
    print(next(odd_nums_2))
except StopIteration as e:
    print(e.__repr__())

