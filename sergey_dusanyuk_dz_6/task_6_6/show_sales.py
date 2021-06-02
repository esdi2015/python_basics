import sys


def file_data_gen(file, start_pos=None, end_pos=None):
    with open(file, 'r', encoding='utf-8') as f:
        line_counter = 0
        for line in f:
            line_counter += 1
            if start_pos is None and end_pos is None:
                yield line.strip()
            elif start_pos is not None and end_pos is None:
                if line_counter >= start_pos:
                    yield line.strip()
            elif start_pos is not None and end_pos is not None:
                if start_pos <= line_counter <= end_pos:
                    yield line.strip()


if __name__ == '__main__':
    sales_file = 'bakery.csv'

    try:
        from_pos = sys.argv[1]
        from_pos = int(from_pos)
    except IndexError:
        from_pos = None

    try:
        to_pos = sys.argv[2]
        to_pos = int(to_pos)
    except IndexError:
        to_pos = None

    sales_data = file_data_gen(sales_file, from_pos, to_pos)

    print(*sales_data, sep='\n')

    print(type(sales_data))
    print(sales_data)
