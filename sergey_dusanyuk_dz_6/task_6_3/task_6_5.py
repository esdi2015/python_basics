import os
import sys


def parse_line(line):
    return line.strip()


def file_data_gen(file):
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            if line:
                parsed_line = parse_line(line)
                yield parsed_line


def get_next_hobby(hobby_gen):
    try:
        return next(hobby_gen)
    except StopIteration:
        return None


def write_result_file(result_file, file_data):
    with open(result_file, 'a', encoding='utf-8') as f:
        for row in file_data:
            f.write('{}: {}\n'.format(row[0], row[1]))


if __name__ == '__main__':

    try:
        users_file = sys.argv[1]
        hobby_file = sys.argv[2]
        users_hobby_file = sys.argv[3]
    except IndexError:
        print('Incorrect args')
        exit(1)

    if not os.path.exists(users_file):
        print('Incorrect users_file')
        exit(1)

    if not os.path.exists(hobby_file):
        print('Incorrect hobby_file')
        exit(1)

    users_data_gen_len = file_data_gen(users_file)
    hobby_data_gen_len = file_data_gen(hobby_file)

    users_data_len = len(list(users_data_gen_len))
    hobby_data_len = len(list(hobby_data_gen_len))

    if users_data_len < hobby_data_len:
        print('Incorrect hobby file')
        exit(1)

    users_data_gen = file_data_gen(users_file)
    hobby_data_gen = file_data_gen(hobby_file)

    res_data = ((next(users_data_gen), get_next_hobby(hobby_data_gen)) for i in range(0, users_data_len))

    write_result_file(users_hobby_file, res_data)




