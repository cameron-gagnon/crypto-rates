#!/usr/bin/env python3

import requests

currencies = ['BTC', 'ETH', 'LTC', 'BCH']

def main():
    for currency in currencies:
        exchange_rate = requests.get(f'https://api.coinbase.com/v2/exchange-rates?currency={currency}').json()
        usd_exchange_rate = get_usd_rate(exchange_rate['data'])
        print(f'{currency},{usd_exchange_rate}')

def get_usd_rate(exchange_rate):
    return get_rate(exchange_rate, 'USD')

def get_rate(exchange_rate, currency):
    return exchange_rate['rates'][currency.upper()]

main()
