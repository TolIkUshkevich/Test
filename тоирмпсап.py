import datetime as dt
import json

import requests
import xmltodict


def geting_current_time():
    return dt.datetime.today().strftime('%d/%m/%Y')

def geting_url():
    url = f"https://www.cbr.ru/scripts/XML_daily.asp?date_req={geting_current_time()}"
    response = requests.get(url)
    data = xmltodict.parse(requests.get(url).content)['ValCurs']['Valute']
    data.append({"@ID": "1",
                "NumCode": "1",
                "CharCode": "RUB",
                "Nominal": "1",
                "Name": "Российский рубль",
                "Value": "1"})
    return data

def geting_excange_rate(valute):
    exchangeRate = valute['Value']
    exchangeRate = exchangeRate.replace(',', '.')
    exchangeRate = float(exchangeRate)
    nominal = int(valute['Nominal'])
    return exchangeRate / nominal

code = input()
ValuteCount = int(input())
Valute_Count_Code = input()
first_course = 1
second_course = 1

for valute in geting_url():
    if code in geting_url() and Valute_Count_Code in geting_url():
        if valute['CharCode'] == code:
            first_course = geting_excange_rate(valute)
        if valute['CharCode'] == Valute_Count_Code:
            second_course = geting_excange_rate(valute)
    else:
        print('Invalid query')
        break


print((first_course / second_course) * ValuteCount)
