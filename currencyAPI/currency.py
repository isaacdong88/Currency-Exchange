import requests
import json


def convert(from_currency, to_currency, amount):
    url = "https://currency-converter-pro1.p.rapidapi.com/convert"

    from_currency = from_currency
    to_currency = to_currency
    amount = amount


    querystring = {"from": from_currency, "to": to_currency, "amount": amount}

    headers = {
        "x-rapidapi-key": "1b87ac329bmshf729da2c229352ep18128ejsn179d7c8d95db",
        "x-rapidapi-host": "currency-converter-pro1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = json.loads(response.text)
    converted_amount = "{:.2f}".format(data['result'])

    return converted_amount


