import requests
import json
from flask import Flask
import pandas as pd

app = Flask(__name__)

NBP_URL = 'http://api.nbp.pl/api/exchangerates'


# Function for getting an average exchange rate for a currency on a specified date
def get_avg_exchange_rate(currency: str, date: str):
    my_url = f'{NBP_URL}/rates/A/{currency}/{date}/'
    response = requests.get(my_url)
    if response.status_code == 200:
        rate_list = json.loads(response.text)
        my_rates = rate_list.get('rates')
        if my_rates:
            return {f"Average Currency Rate For {currency} in {date}": my_rates[0].get('mid', 0)}
        else:
            return {"message": "Rate was not found."}, 404
    else:
        return {"message": "NBP Not Found Error, Possible wrong inputs"}, 404


# Function for getting max and min average value for a currency in terms of number of last quotations
def get_historical_max_min_avg_rates(currency: str, N: str):
    my_url = f'{NBP_URL}/rates/A/{currency}/last/{N}/'
    response = requests.get(my_url)
    if response.status_code == 200:
        response = json.loads(response.text)
        my_rates = response.get('rates')
        if my_rates:
            minimum_value = pd.DataFrame(my_rates)['mid'].min()
            maximum_value = pd.DataFrame(my_rates)['mid'].max()
            return {
                f"Min Average Value For {currency}": minimum_value,
                f"Max Average Value For {currency}": maximum_value
            }
        else:
            return {"message": "Rate was not found."}, 404

    else:
        return {"message": "NBP Not Found Error, Possible wrong inputs"}, 404


# Function for getting major difference between buy and ask rate for a currency in terms of number of last quotations
def major_difference_between_buy_ask_rate(currency: str, N: str):
    my_url = f'{NBP_URL}/rates/C/{currency}/last/{N}/'
    response = requests.get(my_url)
    if response.status_code == 200:
        response = json.loads(response.text)
        my_rates = response.get('rates')
        if my_rates:
            bid_ask_data = pd.DataFrame(my_rates)
            bid_ask_data["bid_ask_diff"] = bid_ask_data["ask"] - bid_ask_data["bid"]
            maximum_difference = bid_ask_data["bid_ask_diff"].max()
            maximum_difference = round(maximum_difference, 6)
            return {f"Major Difference Between Buy and Ask Rate for {currency}": maximum_difference}
        else:
            return {"message": "Rate was not found."}, 404

    else:
        return {"message": "NBP Not Found Error, Possible wrong inputs"}, 404


# Returning currencies on the Narodowy Bank Polski's website on http://localhost:5000/get_top_currencies
@app.get("/get_top_currencies")
def get_top_currencies():
    return {"some currencies": {
        "USD": "dolar amerykański",
        "CAD": "dolar kanadyjski",
        "AUD": "dolar australijski",
        "EUR": "euro",
    }
    }


# Returning Average Currency Rate for a specified currency and date
# on http://localhost:5000/exchanges/usd/2023-01-02
@app.route('/exchanges/<currency>/<date>')
def av_exchange_rate(currency, date):
    response_message = get_avg_exchange_rate(currency, date)
    return response_message


# Returning Min and Max Average Value for a specified currency and N number(last quotations)
# on http://localhost:5000/max-min-average-value/usd/10
@app.route('/max-min-average-value/<currency>/<n>')
def max_min(currency, n):
    response_message = get_historical_max_min_avg_rates(currency, str(n))
    return response_message


# Returning Major difference between the buy and ask rate for a specified currency and N number(last quotations)
# on http://localhost:5000/major-difference-between-buy-ask/usd/10
@app.route('/major-difference-between-buy-ask/<currency>/<n>')
def major_difference(currency, n):
    response_message = major_difference_between_buy_ask_rate(currency, str(n))
    return response_message


if __name__ == '__main__':
    app.run()
