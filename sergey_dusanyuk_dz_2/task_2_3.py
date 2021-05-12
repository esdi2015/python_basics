
test_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

nums = tuple([str(i) for i in range(10)])
special_symbols = ('+',)
nums_idx = []

print('Исходный список: {}, id: {}'.format(test_list, id(test_list)))

for idx, test_word in enumerate(test_list):
    if (nums.count(test_word[0]) > 0 or special_symbols.count(test_word[0])) and nums.count(test_word[-1]) > 0:
        nums_idx.append(idx)
        if special_symbols.count(test_word[0]) > 0:
            if test_word.index(test_word[-1]) == 1:
                test_list[idx] = '{}0{}'.format(test_word[0], test_word[-1])
            else:
                test_list[idx] = '{}'.format(test_word)
        else:
            if test_word.index(test_word[-1]) == 0:
                test_list[idx] = '0{}'.format(test_word)
            else:
                test_list[idx] = '{}'.format(test_word)

print('Числа дополнены нулями: {}, id: {}'.format(test_list, id(test_list)))

for idx in nums_idx[::-1]:
    test_list.insert(idx, '"')
    test_list.insert(idx + 2, '"')

print('Числа обособлены кавычками: {}, id: {}'.format(test_list, id(test_list)))

result_string = ' '.join(test_list)

print('Список преобразован строку: {}'.format(result_string))

result_string = list(result_string)
i = 1

for idx, _char in enumerate(result_string):
    if _char == '"' and i % 2 == 1:
        result_string.pop(idx+1)
        i += 1
    elif _char == '"' and i % 2 == 0:
        result_string.pop(idx - 1)
        i += 1

print('Убраны лишние пробелы вокруг чисел: {}'.format(''.join(result_string)))

