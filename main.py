import requests
import json

#   THIS IS A DRAFT. I JUST HAVE TO ORGINIZE THE OUTPUT, AND DO SOME CONVERSIONS.

#gets zipcode
zipcode = input("Please enter your zipcode: ")

#list of parameters that will be printed
params = "name", "humidity"

#The URL the GET request is sent to
APIURL = "http://api.openweathermap.org/data/2.5/weather?zip=" + zipcode + ",us&appid=4c47438000d79d365701157e7e97e691"

#GET request with zipcode.
zipGET = requests.get(APIURL)

#Checks status code. Used for troubleshooting if the call fails
if zipGET.status_code != 200:
    print("Woops, something went wrong. Status code %d..." %
          (zipGET.status_code))

#Places the JSON
rawResults = zipGET.content
#processes JSON into a Python dict
results = json.loads(rawResults)

#Prints the selected values from the dictionary
print("\nCity: " + str(results["name"]))
print("Current: " + str(results["main"]["temp"]))
#print Wind, Weather, Min and MAx temp, humidity, sunrise and sunset
