print("*******************************************")
print("Gasoline Branch\n\n")

#Import Libraries Here
import random

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



print(gasLevelGauge())
print(listOfGasStations())
