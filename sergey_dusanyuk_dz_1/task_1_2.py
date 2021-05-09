def gb_task_1_2(max_value=1000, div_value=7, shift_value=17):
    odd3_list = [i ** 3 for i in range(1, max_value, 2)]
    sum_div7 = 0
    sum_div7_shifted = 0

    for idx, odd3 in enumerate(odd3_list):
        num_sum = odd3 % 10
        while odd3 // 10 > 0:
            odd3 = odd3 // 10
            num_sum += odd3 % 10

        if num_sum % div_value == 0:
            sum_div7 += odd3_list[idx]

    for idx, odd3 in enumerate(odd3_list):
        odd3_list[idx] = odd3 + shift_value

    for idx, odd3 in enumerate(odd3_list):
        num_sum = odd3 % 10
        while odd3 // 10 > 0:
            odd3 = odd3 // 10
            num_sum += odd3 % 10

        if num_sum % div_value == 0:
            sum_div7_shifted += odd3_list[idx]
    return sum_div7, sum_div7_shifted


if __name__ == '__main__':
    print('task 1-2')

    sum_7, sum_7_shifted = gb_task_1_2()

    print(sum_7)
    print(sum_7_shifted)