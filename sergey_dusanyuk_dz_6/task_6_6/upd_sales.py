import sys


def upd_file_data(file, line_pos=None, new_val=None):
    with open(file, 'r+', encoding='utf-8') as f:
        line_counter = 1
        while line_counter < line_pos:
            line_counter += 1
            f.readline()
            curr_pos = f.tell()

    with open(file, 'r+', encoding='utf-8') as f:
        f.seek(curr_pos)
        f.write('{}\n'.format(new_val))


if __name__ == '__main__':
    sales_file = 'bakery.csv'

    try:
        upd_pos = sys.argv[1]
        upd_pos = int(upd_pos)
    except IndexError:
        upd_pos = None

    try:
        upd_val = sys.argv[2]
        upd_val = upd_val
    except IndexError:
        upd_val = None

    if upd_pos is not None and upd_val is not None:
        upd_file_data(sales_file, upd_pos, upd_val)
    else:
        print('Incorrect args')
        exit(1)

