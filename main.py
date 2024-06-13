### --- IMPORTS --- ###

#we want to import requests for getting our data
import requests
#we want dot env and os for env variables
from dotenv import load_dotenv
import os
#we want twilio to send sms messages
from twilio.rest import Client
import time

### --- CONSTANTS / VARIABLES / ENDPOINTS --- ###

#we are making this here so that the user can change the amount of difference they want before they will be notified
DIFF_AMOUNT = 1

#stock name for this course project is going to be tesla
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

### --- ENV VARIABLES --- ###

load_dotenv()

stock_api = os.getenv("ALPHA_API_KEY")
news_api = os.getenv("NEWS_API_KEY")

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

sending = os.getenv("SENDING_NUMBER")
receiving = os.getenv("RECEIVING_NUMBER")


### --- GETTING THE ABS DIFFERENCE --- ###

#first we want to get yesterdays closing stock price we have the endpoint just need params
#Time series daily is ray daily data (date, daily open, daily high, daily low, daily close, daily volume)
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": stock_api,
}

time.sleep(1)
#get our response and format it
stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
data = stock_response.json()["Time Series (Daily)"]

#we want to use list comprehension to make this easier to read and pull data from
data_list = [value for (key, value) in data.items()]

#we need to compare yesterdays data to the day before yesterdays data we can get these by:
y = data_list[0]

#we now get the closing price by grabbing the value from the close key, we round it to 2 and float it as decimal
y_closing_price = round(float(y["4. close"]),2)
#we can now do the same and get the day before yesterdays prices
dby = data_list[1]
dby_closing_price = round(float(dby["4. close"]),2)
#now we can get the difference, we want to use an absolute function so it doesn't give us a negative number
difference = abs(y_closing_price - dby_closing_price)
#using an if statement we can give a visual indication of positive/ negative stock fluctuations
fluctuation = None

#if the fluctuation is above 0 that means stock went up else it went down
if difference > 0:
    fluctuation = "🔺"
else: 
    fluctuation = "🔻"

#we also want % difference for our if statement
percentage_diff = round((difference / y_closing_price) * 100)

# ### --- GET THE NEWS --- ### 

#if the % difference is above 5% we want to  get the news articles for that particular company
if percentage_diff > DIFF_AMOUNT:
    #we setup our news params
    news_params = {
        "apikey": news_api,
        #we want to feed it the company name for the title query
        "qInTitle": COMPANY_NAME,
    }
    #now we request our news articles
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    #we now need to get only three of these using the slice operater
    three_articles = articles[:3]
#     ### --- SEND THE SMS --- ###

    #now we use more list comprehension to get the articles titles / messages
    article_content = [f"{STOCK_NAME}: {fluctuation}{percentage_diff}% \nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    
    # finally we want to setup a for loop and send each article via twilio
    for article in article_content:
        client = Client(account_sid, auth_token)
        message = client.messages \
                    .create(
                        body=article,
                        from_=sending,
                        to=receiving
                    )
    
        print(message.sid)


else:
    print("No Significant Change")

