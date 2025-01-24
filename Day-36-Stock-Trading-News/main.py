import requests
from datetime import datetime, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCKS_API = ""
NEWS_API = ""
weekdays = [0, 1, 2, 3, 4]

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCKS_API,
}
url = "https://www.alphavantage.co/query"

response = requests.get(url, params=parameters)
response.raise_for_status()
data = response.json()
data = data["Time Series (Daily)"]

print(data)
my_time = datetime.now()
my_year = my_time.year
my_month = f"{my_time.month:02}"
my_day = f"{my_time.day:02}"
my_weekday = my_time.weekday()
print(my_time)
print(my_weekday)
print(timedelta(days=my_weekday-1))


today = f"{my_year}-{my_month}-{my_day}"

if my_weekday == 0:
    last_friday = f"{my_year}-{my_month}-{int(my_day) - 3}"
    last_thursday = f"{my_year}-{my_month}-{int(my_day) - 4}"
elif my_weekday == 1:
    last_friday = f"{my_year}-{my_month}-{int(my_day) - 1}"
    last_thursday = f"{my_year}-{my_month}-{int(my_day) - 4}"
else:
    last_friday = f"{my_year}-{my_month}-{int(my_day) - 1}"
    last_thursday = f"{my_year}-{my_month}-{int(my_day) - 5}"

last_friday_close = data[last_friday]["4. close"]
last_thursday_close = data[last_thursday]["4. close"]
print(last_friday_close)
print(last_thursday_close)

last_thursday_close_perc = float(last_thursday_close) * 0.05
print(last_thursday_close_perc)

if float(last_friday_close) > (float(last_thursday_close) + last_thursday_close_perc) or float(last_friday_close) < (
        float(last_thursday_close) - last_thursday_close_perc):
    print("Get News")

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
##Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

    news_parameters = {
        "q": COMPANY_NAME,
        "searchIn": "title,description",
        "apiKey": NEWS_API,
        "language": "en",
        "excludeDomains": "yahoo.com",
    }

    news_response = requests.get(f"https://newsapi.org/v2/everything", params=news_parameters)
    news_response.raise_for_status()
    news_response = news_response.json()
    print(news_response['articles'])
    print(news_response['articles'][0])
    print(news_response['articles'][1])
    print(news_response['articles'][2])


