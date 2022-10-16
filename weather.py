import email
import os
import asyncio
import python_weather
import email


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

# if __name__ == "__main__":
#     if os.name == "nt":
#         asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# asyncio.run(get_weather())