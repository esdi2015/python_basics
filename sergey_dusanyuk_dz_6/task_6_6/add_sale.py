import sys


if __name__ == '__main__':

    try:
        sale_val = sys.argv[1]
    except IndexError:
        sale_val = None

    if sale_val:
        with open('bakery.csv', 'a', encoding='utf-8') as f:
            f.write('{}\n'.format(sale_val))
