def gb_task_1_1(duration):
    seconds_in_period = [60*60*24*365, 60*60*24*30, 60*60*24, 60*60, 60, 1]
    period_labels = ['г', 'мес', 'дн', 'час', 'мин', 'сек']
    periods_count = 0
    human_readable_time = []

    for idx, seconds in enumerate(seconds_in_period):
        period_duration = duration // seconds
        duration = duration % seconds
        periods_count += period_duration

        if periods_count > 0:
            human_readable_time.append('{} {}'.format(period_duration, period_labels[idx]))

    human_readable_time = ' '.join(human_readable_time)
    return human_readable_time


if __name__ == '__main__':
    print('task 1-1')

    input_duration = input('Input integer value in seconds: ')
    readable_time = gb_task_1_1(int(input_duration))

    print(readable_time)