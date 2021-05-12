
test_list = [57.8, 46.51, 97, 8.84, 86.94, 56.05, 41, 38.01, 75, 61.58, 3, 65.33]


for price in test_list:
    if len(str(price).split('.')) == 1:
        print('{} руб 00 коп'.format(str(price).split('.')[0]))
    else:
        print('{} руб {} коп'.format(str(price).split('.')[0], str(price).split('.')[1].zfill(2)))


print(test_list)
print(id(test_list))

test_list.sort()

print(test_list)
print(id(test_list))

test_list_1 = test_list[::-1]

print(test_list_1)
print(id(test_list_1))


print((test_list_1[:5])[::-1])

print(((test_list[::-1])[:5])[::-1])

