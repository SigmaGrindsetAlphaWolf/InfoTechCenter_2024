#Import Libraries Here
import time
import sys
import random
from time import sleep

#WELCOME BRANCH STARTS HERE CUH
timeToSleep = 1

print("\n\nWelcome to InfoTech Center V1.0\n")
time.sleep(timeToSleep)

#Code to have the ellipsis add a dot every .5 seconds
x = 20
ellipsis = 0

while x != 20:
    x += 1
    message = ("Infotech Center Operating System Loading" + "." * ellipsis)
    ellipsis = ellipsis + 1
    sys.stdout.write("\r" + message) #\r prints a carriage return first
    time.sleep(.5)
    if ellipsis == 4:
        ellipsis = 0
    if x == 20:
        print("\n\n0perating System Successfully Booted Up - Retina Scanned - Access Granted!\n")


# GASOLINE BRANCH STARTS HERE CUH
print("*******************************************\n")
print("Gasoline Branch\n\n")

#Function that lists Gas Levels, randomly choosing one and returning its value
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

#Function that lists Gas Stations,m randomly choosing one and returning its value
def listOfGasStations():
    gasStations = ["Shell", "Speedway", "Marathon", "Buc-ee's", "Mobile", "Costco", "Meijer", "7Eleven", ]
    gasStationsNearby = random.choice(gasStations)
    return gasStationsNearby

#Function will call the gasLevelGuage to determine our gas level and then find a close gas station
#bt calling the ListOfGasStations function if we are on low or quarter tank
def  gasLevelAlert():
    milesToGasStationLow = round(random.uniform(1,25),1)
    milesToGasStationsQuarterTank = round(random.uniform(25.1, 50),1)
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator == "Empty":
        print("***WARNING - YOU ARE ON EMPTY***")
        sleep(2.5)
        print("Calling Triple AAA")
    elif gasLevelIndicator == "Low":
        print("Your gas tank is extremely low, checking Google Maps for the closest gas station. . .")
        sleep(2.5)
        print("The closest gas station is is",listOfGasStations(),"which is",milesToGasStationLow,"Miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("Your gas tank is on a quarter tank, refueling is advised.")
        sleep(2.5)
        print("The closest gas station is is",listOfGasStations(),"which is",milesToGasStationLow,"Miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank is half empty, no refueling is necessary. ")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is 3/4ths full.")
    else:
        print("Your gas tank is full, good job.")

gasLevelAlert()



print("\n**********************************************\n")

print("Weather Branch")

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
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 50mph")
    elif weatherAlert == "blizzard":
        print("\nNational Weather Service has updated our alarm by 45 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 40mph")
    elif weatherAlert == "raining":
        print("\nNational Weather Service has updated our alarm by 10 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 60mph")
    elif weatherAlert == "foggy":
        print("\nNational Weather Service has updated our alarm by 10 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 60mph")
    elif weatherAlert == "windy":
        print("\nNational Weather Service has updated our alarm by 10 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 70mph")
    elif weatherAlert == "icy":
        print("\nNational Weather Service has updated our alarm by 10 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 30mph")
    else:
        print("\nNational Weather Service hasforecast of", weatherAlert, "weather conditions.")
        sleep(1.5)
        print("VRS has been disengaged!  Drive at your own risk.")

vehicleResponseSystem()

