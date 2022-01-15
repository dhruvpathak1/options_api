# options_api
This individual project aims to use Yahoo Finance API and filter out the required PUT Options that fit a validation criteria.
A scheduler is added that will execute the code periodically after every hour and sends a desktop notification.

## A detailed explanation of Options Trading and this project can be found at :
#### - https://dhruvpathak.netlify.app/blogs/options

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

## Program steps and general flow :

1. Yahoo Finance API is called and the url containing JSON data is read.

2. Epoch Time between the range of 35-50 days from the current epoch time is calculated.

3. All the expiration dates withing the range is stored in a list to be used in the 2nd API call.

4. Second API call is made using the the epoch values satisfying the required condition.

4. URL data read is travesered to PUT options, with unwanted data is popped.

5. PUT Options Strike Prices that are within the 70% - 110% range with respect to the current price are pretty printed.

6. Printed data contains Strike Price, Bid, Ask, Expiration Date, Stock Name, Current Stock Price and the respective date whoes PUT Options are being declared.

7. After the data is printed, a desktop notification is sent.

8. API calls can be made for any number of stocks that will be displayed in a neat format.

9. A scheduler will run the code every 1hr to update the data.

