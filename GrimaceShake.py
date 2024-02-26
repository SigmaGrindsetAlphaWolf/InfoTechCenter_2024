print("\n***************************************************\n")

print("Weather Branch\n")

#import Libraries Here
import random
from time import sleep

#Create a function that randomely chooses the weather from a list
def weather():
    weatherForecast = ["snowy", "blizzard", "raining", "foggy", "windy", "icy", "sunny"]
    weatherConditions = random.choice(weatherForecast)
    return weatherConditions

# Variable to call the weather() once VRS(Vehicle Response System) is determined
weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert == "snowy":
        print("\nNational Weather Service has updated our alarm by 30 minutes because of the forecast of",weatherAlert,
            "weather conditions.")
        print("VRS has been engaged only allowing you to drive 50mph")
    elif weatherAlert == "blizzard":
        print("\nNational Weather Service has updated our alarm by 45 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        print("VRS has been engaged only allowing you to drive 40mph")
    elif weatherAlert == "raining":
        print("\nNational Weather Service has updated our alarm by 10 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        print("VRS has been engaged only allowing you to drive 60mph")




vehicleResponseSystem()