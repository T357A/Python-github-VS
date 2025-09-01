import requests
from pprint import pprint

openweather_api_key ="8a5475eced4e0e9a90ef1e2894cb31b7"
location = input("Enter the location you wou;d like the weather for: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + openweather_api_key+"&q="+location+"&units=metric" 
