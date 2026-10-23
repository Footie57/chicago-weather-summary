import requests
from datetime import date, timedelta
import anthropic
client = anthropic.Anthropic()

r = requests.get("https://api.weather.gov/zones/public/ILZ104/forecast")
data = r.json()


days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def getforecast(json):
       d = date.today()
       text = ""
       for x in json["properties"]["periods"]:
              base = x["name"].replace(" Night", "")    # "Friday Night" -> "Friday"

              if base in days:
                     while d.weekday() != days.index(base):
                            d += timedelta(days=1)            # step forward until the weekday matches

              text += str(x["name"] + " (" + d.strftime("%m/%d") + "):")
              text += "\n"
              text += str(x["detailedForecast"])
              text += "\n"
              text += "\n"
       return text


message = client.messages.create(
    model="claude-sonnet-5-5",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "Summarize the following in plain text, paragraph form, \
            include the calendar dates when referring to the day of the week, \
            keep each line to around 80 characters,\
            and use 100 words or less:" + getforecast(data) 
            
        }
    ],
)
for block in message.content:
    if block.type == "text":
        print(block.text)

