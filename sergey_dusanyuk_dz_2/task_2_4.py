print('task 2-4')

test_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор '
                                                                                                        'аэлита']

for employee in test_list:
    correct_name = '{}{}'.format(employee.split(' ')[-1][0].upper(), employee.split(' ')[-1][1:].lower())
    print('Привет, {}!'.format(correct_name))

