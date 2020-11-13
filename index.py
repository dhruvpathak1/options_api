import pprint
import datetime
import json
import math
import time
import schedule
import urllib.request
from win10toast import ToastNotifier


# ======================================================================================================================
# Functions

def options_api():
    def dates_within_range():
        req_dates.clear()
        # CURRENT TIME SINCE EPOCH IN SECONDS
        seconds = math.trunc(time.time())
        # print("Epoch Time =", seconds)

        # EPOCH TIME 30 DAYS and 50 DAYS FROM CURRENT
        low_range = seconds + 2592000
        high_range = seconds + 4320000

        # LOOP TO FIND EPOCH TIME WITHIN RANGE
        dates = data['optionChain']['result'][0]['expirationDates']
        # print(dates)
        for i in dates:
            if low_range <= i <= high_range:
                req_dates.append(i)
        req_dates.reverse()
        # print(req_dates)

    def put_options_data():

        # CONDITION CHECKING OF DATE AND PRINTING TRUE VALUES
        def put_options_for_req_dates(date):
            info = data_2['optionChain']['result'][0]['options'][0]['puts']
            # pprint.pprint(info)

            # FETCHING CURRENT PRICE FROM quote->fiftyDayAverage
            current_price = data_2['optionChain']['result'][0]['quote']['fiftyDayAverage']
            # print(current_price)

            counter = 0

            # PRINTING OPTION DATA FOR THE RESPECTIVE DATES
            for k in info:
                expiration = data_2['optionChain']['result'][0]['options'][0]['puts'][counter]['expiration']
                strike = data_2['optionChain']['result'][0]['options'][0]['puts'][counter]['strike']
                lower_range = current_price - (current_price * 0.30)
                upper_range = current_price + (current_price * 0.10)

                # pprint.pprint(k)
                # print(expiration)
                if expiration == date and (lower_range <= strike <= upper_range):
                    k.pop('contractSymbol', None)
                    k.pop('currency', None)
                    k.pop('lastPrice', None)
                    k.pop('change', None)
                    k.pop('contractSize', None)
                    k.pop('lastTradeDate', None)
                    k.pop('inTheMoney', None)
                    k.pop('percentChange', None)
                    k.pop('volume', None)
                    k.pop('openInterest', None)
                    k.pop('expiration', None)

                    # STORING VALUES IN A LIST TO PRINT CLEANER
                    z = list(k.values())

                    # print('< Strike: ', z[0], ' | Bid: ', '%.2f' % z[1], ' | Ask: ', '%.2f' % z[2], end=' ')
                    # print('| Implied Volatility: ', '%.4f' % z[3], end=' >')
                    print(k, end=' ')
                    print()
                counter += 1

        # PRINTING DATE FOR WHICH VALUES ARE BEING FETCHED FOR
        for x in range(len(req_dates)):
            print("\n")
            print(datetime.datetime.fromtimestamp(req_dates[x]))
            print("___________________________________________")
            print()

            # 2ND URL CALL WITH REQUIRED DATA W.R.T DATES
            time.sleep(2)
            url_with_date = "https://query2.finance.yahoo.com/v7/finance/options/{}?date={}".format(stock, req_dates[x])
            with urllib.request.urlopen(url_with_date) as url1:
                data_2 = json.loads(url1.read().decode())

            # CALLING PUT OPTIONS FUNCTION
            put_options_for_req_dates(req_dates[x])

    req_dates = []
    stocks = ['jnj']

    for stock in stocks:
        print(stock.upper(), end=' ')

        # ADDING STOCK NAME TO URL
        json_url = "https://query2.finance.yahoo.com/v7/finance/options/"
        json_url += stock

        time.sleep(2)
        # FETCHING URL DATA IN JSON FORMAT
        with urllib.request.urlopen(json_url) as url:
            data = json.loads(url.read().decode())
            # pprint.pprint(data)

        # FUNCTION TO CALCULATE EPOCH 35-50 FROM CURRENT DATE
        dates_within_range()

        # FETCHING PUT OPTIONS FOR REQUIRED DATES
        put_options_data()
        print()
        print("$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$")


# ======================================================================================================================

options_api()

# NOTIFICATION ALERT CODE
toast = ToastNotifier()
toast.show_toast("Py_Options", "Execution Completed. Check Info", duration=10, icon_path="bull.ico")

# schedule.every(30).seconds.do(options_api)
# while True:
#     schedule.run_pending()
#     time.sleep(1)
