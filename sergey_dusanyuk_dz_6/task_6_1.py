import os
import sys
from itertools import islice


def parse_line(line):
    line_ip = line.split('- -')
    line_method_url = line_ip[1].strip().split('"')[1]
    return line_ip[0].strip(), line_method_url.split(' ')[0].strip(), line_method_url.split(' ')[1].strip()


def log_data_gen(log_file):
    with open(log_file, 'r', encoding='utf-8') as f:
        for line in f:
            if line:
                parsed_line = parse_line(line)
                yield parsed_line


if __name__ == '__main__':
    logs_file = 'nginx_logs.txt'
    print('{} MB'.format(round(os.stat(logs_file).st_size / 1024 / 1024, 4)))

    result = log_data_gen(logs_file)

    print(type(result))
    print(sys.getsizeof(result))
    print(list(islice(result, 10)))
    # print(list(result))
