import sys

from utils import currency_rates, currencies_codes


if __name__ == '__main__':
    print(*currency_rates('UAH'), sep=', ')
    print(*currency_rates('MDL'), sep=', ')
    print(*currency_rates('CNY'), sep=', ')
    print(*currency_rates('BRL'), sep=', ')
    print(*currency_rates('USD'), sep=', ')

    print('\n\r')

    if len(sys.argv) > 1:
        currency_in = sys.argv[1]
        if currency_in == 'list':
            print(*currencies_codes(), sep=', ')
        else:
            try:
                result = currency_rates(currency_in)
                if not result[0]:
                    print('Please select value (or type "list" to view al codes):')
                    print(*currencies_codes(), sep=', ')
                else:
                    print(*result, sep=', ')
                    print(type(result[0]), type(result[1]))
            except KeyError as e:
                print(e.__repr__())
                print('Please select value (or type "list" to view al codes):')
                print(*currencies_codes(), sep=', ')
    else:
        print(type([*sorted(currencies_codes())]))
        print(*currencies_codes(), sep=', ')
