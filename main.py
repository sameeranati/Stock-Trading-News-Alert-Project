STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
import csv
import requests
import os
from twilio.rest import Client
from datetime import date,timedelta
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
import requests
import pandas
import math

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=TSLA&outputsize=compact&apikey=OK8ZAOENBHQ57QR6'
r = requests.get(url)
data = r.json()
today=date.today()
yesterday=today-timedelta(days=1)

# new_data=[data['Time Series (Daily)'][today]['4. close'] for (key, value) in data.items()]

new_today=today.strftime("%Y-%m-%d")

new_yesterday=yesterday.strftime("%Y-%m-%d")


closing_ys=float(data['Time Series (Daily)'][new_today]['4. close'])
closing_dbys=float(data['Time Series (Daily)'][new_yesterday]['4. close'])
percent=((closing_ys-closing_dbys)/closing_dbys)*100
if percent>5:
    print(f"stock grew by {percent}")
    url = 'https://newsapi.org/v2/everything?q=%27tesla%27&from=2022-12-06&sortBy=recent&apiKey=f26b6fbc52124bafb4f914717997f2d7'
    r = requests.get(url)
    news=r.json()
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    news_title=[]
    for i in range(3):
        news_title.append(news['articles'][i]['title'])
    
    news_description=[]
    for i in range(3):
        news_description.append(news['articles'][i]['description'])
    
    for i in range(3):
        message = client.messages \
                        .create(
                            body=f"TSLA: 🔺{math.ceil(percent)}\n HEADLINE:{news_title[i]}\nDESCRIPTION:{news_description[i]}",
                            from_="+19403704292",
                            to="+16142560712"
                        )


        print(message.status)
else:
    print(f"stock grew by {percent}")
    url = 'https://newsapi.org/v2/everything?q=%27tesla%27&from=2022-12-06&sortBy=recent&apiKey=f26b6fbc52124bafb4f914717997f2d7'
    r = requests.get(url)
    news=r.json()
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    news_title=[]
    for i in range(3):
        news_title.append(news['articles'][i]['title'])
    
    news_description=[]
    for i in range(3):
        news_description.append(news['articles'][i]['description'])
    
    for i in range(3):
        message = client.messages \
                        .create(
                            body=f"TSLA: 🔻{math.ceil(percent)}\n HEADLINE:{news_title[i]}\nDESCRIPTION:{news_description[i]}",
                            from_="+19403704292",
                            to="+16142560712"
                        )


        print(message.status)


    # articles_description=[news['articles'][0]['description']:news['articles'][2]['description']]
    



# #TODO 2. - Get the day before yesterday's closing stock price

# #TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

# #TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

# #TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

#     ## STEP 2: https://newsapi.org/ 
#     # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 






#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

