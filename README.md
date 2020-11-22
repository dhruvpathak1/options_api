# options_api
This individual project aims to use Yahoo Finance API and filter out the required PUT Options that fit the validation criteria.

## Programming Language: Python

## Installation Check List
Required libraries in your Python Interpreter:

    - [ ] pprint
    
    - [ ] datetime
    
    - [ ] json
    
    - [ ] math
    
    - [ ] time
        
    - [ ] schedule
    
    - [ ] urllib.request
    
    - [ ] ToastNotifier from win10toast 

1. Yahoo Finance API is called and the url containing JSON data is read.
2. Epoch Time between the range of 35-50 days from the current epoch time is stored.
3. Second API call is made using the the above stored epoch time.
4. URL data read is travesered to PUT options where unwanted data is popped.
5. PUT options that are within the 70% - 110% mark with respect to the current price is stored.
6. This data is then, containing Strike Price, bid, Ask, Expiration Date, Stock Name etc.
7. After the data is printed, a desktop notification is sent.
8. API call can be made for any number of stocks.
