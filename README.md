# options_api
PUT OPTIONS call from Yahoo Finance API.

# Project Description
The aim of this project was to call the Yahoo Finance API for multiple stocks and seperate the required data.
1. First, epoch time is calculated for the current time. 
2. Then we find the epoch value for a range of 35-50 days ahead of the current epoch time.
3. Next, making the API call, the values that fit the time range is extracted.
4. 2nd API call is make to fetch data of only the particular dates.
5. This data is then run through and is pretty printed.
6. Hold process is run multiple times for different stocks.
