import datetime
import json
import math
import pprint
import time
import urllib.request


# ======================================================================================================================
# Functions


def dates_within_range():
    req_dates.clear()
    # CURRENT TIME SINCE EPOCH IN SECONDS
    seconds = math.trunc(time.time())
    # print("Epoch Time =", seconds)

    # EPOCH TIME 35 DAYS and 50 DAYS FROM CURRENT
    low_range = seconds + 3024000
    high_range = seconds + 4320000

    # LOOP TO FIND EPOCH TIME WITHIN RANGE
    dates = data['optionChain']['result'][0]['expirationDates']
    # print(dates)
    for i in dates:
        if low_range <= i <= high_range:
            req_dates.append(i)
    # print(req_dates)


def put_options_data():

    # CONDITION CHECKING OF DATE AND PRINTING TRUE VALUES
    def put_options_for_req_dates(date):
        info = data_2['optionChain']['result'][0]['options'][0]['puts']
        counter = 0

        # PRINTING OPTION DATA FOR THE RESPECTIVE DATES
        for k in info:
            expiration = data_2['optionChain']['result'][0]['options'][0]['puts'][counter]['expiration']
            # pprint.pprint(k)
            # print(expiration)
            if expiration == date:
                pprint.pprint(k)
            counter += 1
            print("----------------------------------------------------")

    # PRINTING DATE FOR WHICH VALUES ARE BEING FETCHED FOR
    for x in range(len(req_dates)):
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


# ======================================================================================================================
req_dates = []
stocks = ['aapl', 'tsla', 'kodk', 'amzn']

for stock in stocks:
    print(stock.upper())

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
    print("#######################################################################################")
    print()
