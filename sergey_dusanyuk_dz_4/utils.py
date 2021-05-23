from datetime import datetime

import requests


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


def prepare_currency_rates_dict():
    api_url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    raw_currency_rates = get_currency_rates_api(api_url)
    dict_ = currency_rates_to_dict(raw_currency_rates)
    return dict_


def currencies_codes():
    currency_rates_dict = prepare_currency_rates_dict()
    currency_codes = [*sorted(currency_rates_dict.keys())]
    currency_codes.pop()
    return currency_codes


def currency_rates(in_currency):
    currency_rates_dict = prepare_currency_rates_dict()
    out_currency = currency_rates_dict[in_currency.upper()]['Value']
    rates_date = currency_rates_dict['rates_date']
    return round(float(out_currency.replace(',', '.')), 2), (datetime.strptime(rates_date, '%d.%m.%Y')).date()
