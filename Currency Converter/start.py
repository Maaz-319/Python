import requests

currency_to_convert_name = input("Enter Currency name to convert(eg 'PKR'): ")
target_currency_name = input("Enter target currency name: ")
currency_to_convert = float(input("Enter Currency to convert: "))
url = str("https://v6.exchangerate-api.com/v6/dce6e47f488da12b9afbabf6 /latest/" + currency_to_convert_name + '/' + target_currency_name + '/' + str(currency_to_convert))
currency_data = requests.get(url)
currency_data = currency_data.json()
print(currency_data)
data = currency_data["conversion_result"][0]
ipnut(data)