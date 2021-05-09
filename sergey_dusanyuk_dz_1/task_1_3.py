def gb_task_1_3(percent_num):
    def get_correct_string(num):
        base_word = 'процент'
        word_suffixes = ['а', 'ов']
        base_string = '{} {}'.format(num, base_word)
        if 1 < num < 5:
            return '{}{}'.format(base_string, word_suffixes[0])
        elif 4 < num < 21:
            return '{}{}'.format(base_string, word_suffixes[1])
        else:
            return base_string

    percent_string = get_correct_string(percent_num)

    percent_list = []
    for i in range(1, 21):
        _percent_string = get_correct_string(i)
        percent_list.append(_percent_string)

    return percent_string, percent_list


if __name__ == '__main__':
    print('task 1-3')

    input_num = input('Input number from 1 to 20: ')
    correct_percent_string, correct_percent_list = gb_task_1_3(int(input_num))

    print(correct_percent_string)
    print('\n\r')

    for correct_percent in correct_percent_list:
        print(correct_percent)