
test_list = [57.8, 46.51, 97, 8.84, 86.94, 56.05, 41, 38.01, 75, 61.58, 3, 65.33]

prices_list = []

for price in test_list:
    price_str = str(price)
    if len(price_str.split('.')) == 1:
        prices_list.append('{} руб 00 коп'.format(price_str.split('.')[0]))
    else:
        prices_list.append('{} руб {} коп'.format(price_str.split('.')[0], price_str.split('.')[1].zfill(2)))

prices_list_str = ', '.join(prices_list)

print("Отформатированные цены:")
print(prices_list_str)
print("\r")

print("Исходный список:")
print(test_list)
print('id - {}'.format(id(test_list)))
print("\r")

test_list.sort()

print("Список отсортированный по возрастанию:")
print(test_list)
print('id - {}'.format(id(test_list)))
print("\r")

test_list_desc = test_list[::-1]

print("Новыйй список отсортированный по убыванию:")
print(test_list_desc)
print('id - {}'.format(id(test_list_desc)))
print("\r")

top5_expensive = ((test_list[::-1])[:5])[::-1]

print("Цены пяти самых дорогих товаров:")
print(top5_expensive)

