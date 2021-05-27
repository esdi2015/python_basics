
num = 15


def odd_nums_gen(max_num):
    for i in range(1, max_num, 2):
        yield i


odd_nums = odd_nums_gen(num)

print(type(odd_nums))
print(*odd_nums, sep=', ')

try:
    print(next(odd_nums))
except StopIteration as e:
    print(e.__repr__())

