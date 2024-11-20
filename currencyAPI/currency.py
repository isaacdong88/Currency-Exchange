import requests

url = "https://currency-converter-pro1.p.rapidapi.com/convert"

querystring = {"from": "USD", "to": "EUR", "amount": "100"}

headers = {
    "x-rapidapi-key": "1b87ac329bmshf729da2c229352ep18128ejsn179d7c8d95db",
    "x-rapidapi-host": "currency-converter-pro1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
