import requests 
from datetime import datetime

user_api = '525f23fab081c992c630b46e3988b268'
location = input("Enter your city name: ")
complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api

api_link = requests.get(complete_api_link)
api_data =api_link.json()
# print(api_data)

if api_data['cod'] == '404':
    print("Invalid city:{}, Please check you City name".format(location))
else:
    temp_city = ((api_data['main']['temp'])- 273.15)
    weather_desc = api_data['weather'][0]['description']
    wind_spd = api_data['wind']['speed']
    hmdt = api_data['main']['humidity']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
    print("-------------------------------------------------------")
    print("Weather Stats for - {} | {}".format(location.upper(),date_time))
    print("-------------------------------------------------------")
    
    print("Current temperature is :{:2f} deg C".format(temp_city))
    print("Current weather desc   :",weather_desc)
    print("Current Wind Speed     :",wind_spd)
    print("Current Humidity       :",hmdt)