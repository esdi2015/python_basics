import sys
import requests

from datetime import datetime
from decimal import Decimal


def get_currency_rates_api(url):
    api_data = requests.get(url)
    api_data = api_data.content.decode(api_data.encoding)
    return api_data


def currency_rates_to_dict(raw_data):
    raw_data = raw_data.split('><')
    raw_data.pop(0)
    date_tag = raw_data.pop(0)
    rates_date = date_tag[14:24]

    currencies = {}
    currency = {}
    for rd in raw_data:
        rd = rd.split('>')
        if len(rd) == 1:
            if len(currency) > 0:
                currencies[currency['CharCode']] = currency
            currency = {}
        else:
            currency[rd[0]] = rd[1].split('</')[0]

    currencies['rates_date'] = rates_date
    return currencies


def currency_rates(in_currency):
    api_url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    raw_currency_rates = get_currency_rates_api(api_url)
    currency_rates_dict = currency_rates_to_dict(raw_currency_rates)
    out_currency = currency_rates_dict[in_currency.upper()]['Value']
    rates_date = currency_rates_dict['rates_date']
    return round(float(out_currency.replace(',', '.')), 2), (datetime.strptime(rates_date, '%d.%m.%Y')).date()


def currency_rates_decimal(in_currency):
    api_url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    raw_currency_rates = get_currency_rates_api(api_url)
    currency_rates_dict = currency_rates_to_dict(raw_currency_rates)
    out_currency = currency_rates_dict[in_currency.upper()]['Value']
    rates_date = currency_rates_dict['rates_date']
    return round(Decimal(out_currency.replace(',', '.')), 4), (datetime.strptime(rates_date, '%d.%m.%Y')).date()


if __name__ == '__main__':
    currency_in = sys.argv[1]

    result = currency_rates(currency_in)
    print(result[0], result[1])
    print(type(result[0]), type(result[1]))

    result_decimal = currency_rates_decimal(currency_in)
    print(result_decimal[0], result_decimal[1])
    print(type(result_decimal[0]), type(result_decimal[1]))
