import email
import os
import asyncio
from re import S
import python_weather
import email
import time 
import smtplib, ssl


#TODO
# write function to send email everyday at 7AM

async def get_weather():
    async with python_weather.Client(format=python_weather.IMPERIAL) as client:
        weather = await client.get("Portland")
        print(weather.current.temperature)

        for forcast in weather.forecasts:
            print(forcast.date, forcast.astronomy)

            for hourly in forcast.hourly:
                print(f'--> {hourly!r}')
def send_email():
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    password = 'Boobear@2017'
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
        server.login("dettiannan@gmail.com", password)
        
    pass
# if __name__ == "__main__":
#     if os.name == "nt":
#         asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# asyncio.run(get_weather())