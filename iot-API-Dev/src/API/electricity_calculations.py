import datetime
from datetime import timedelta, date, time
from random import randint

import numpy
import numpy as np
# returns a list of electricity usage calculations for each day jan 1 - april 30

dates = []
string_dates = []


class ElectricityCalculator:
    # Return values will be return kilowatts * usage time(hours), returns kWh
    def __init__(self):
        self.electricityPrice=0.12

    def cost(self, kWh):
        return self.electricityPrice*kWh

    def microwave(self, dt):
        if dt.weekday()<=4: # Monday=0, Friday=4
            return 1.1*(20/60)
        else:
            return 1.1*0.5

    def stove(self, dt):
        if dt.weekday()<=4: # Monday=0, Friday=4
            return 3.5*0.25
        else:
            return 3.5*0.5

    def oven(self, dt):
        if dt.weekday()<=4: # Monday=0, Friday=4
            return 4*0.75
        else:
            return 4

    def fridge(self, dt):
        return 0.15*24

    def dishwasher(self, dt, loads=4):
        return 1.8*0.75*loads

    def clothesWasher(self, dt, loads=4):
        return 0.5*0.5*loads

    def clothesDryer(self, dt, loads=4):
        return 3*0.5*loads

    def livingRoomTV(self, dt):
        if dt.weekday()<=4: # Monday=0, Friday=4
            return 0.636*4
        else:
            return 0.636*8

    def bedroomTV(self, dt):
        if dt.weekday()<=4: # Monday=0, Friday=4
            return 0.1*2
        else:
            return 0.1*4

    def lightBulb(self, dt):
        return 0.06*24 # Placeholder until I know how long lightbulbs are used for

    def bathExhaust(self, dt):
        return 0.03*24 # Same as lightbolb

    def hotWaterHeater(self, dt, gal):
        return 4.5*(4/60)*gal

    def hvac(self, dt, desiredTemp): # hvac is a bit of a toughie to figure out
        def operationUsage(hours):
            return 3.5*hours
        if dt.weekday()<=4: # Monday=0, Friday=4
            exitEnterEvents=16
            kidEvents
        else:
            exitEnterEvents=32
        return 0 # Placeholder until I've finished it



def daterange():
    start_dt = date(2021, 1, 1)  # jan 1st
    end_dt = date(2021, 4, 30)  # april 30th

    for n in range(int((end_dt - start_dt).days)+1):
        yield start_dt + timedelta(n)


def create_dates():
    for dt in daterange():
        date = dt  # date objects to use in calculating weekdays
        string_date = dt.strftime("%Y-%m-%d")  # string of dates to use in final list
        dates.append(date)
        string_dates.append(string_date)
    return dates, string_dates

def calculate_eletricity_usage(hotGal, numLights, desiredTemp=68):
    ec=ElectricityCalculator()
    dailyElectricityCosts=[]
    for dt in daterange():
        tempDic={"date":dt, "kWh":0, "cost":0}
        # Breaking these up just for readability
        tempDic["kWh"]+=ec.microwave(dt)+ec.stove(dt)+ec.oven(dt)+ec.fridge(dt)
        tempDic["kWh"]+=ec.dishwasher(dt)+ec.clothesWasher(dt)+ec.clothesDryer(dt)
        tempDic["kWh"]+=ec.livingRoomTV(dt)+ec.bedroomTV(dt)+ec.lightBulb(dt)*numLights+ec.bathExhaust(dt)
        tempDic["kWh"]+=ec.hvac(dt, desiredTemp)+ec.hotWaterHeater(dt, hotGal)
        tempDic["kWh"]=round(tempDic["kWh"], 2) # For some reason, the floats were going crazy so I'm just rounding it
        tempDic["cost"]=str(round(ec.cost(tempDic["kWh"]), 2))
        tempDic["kWh"]=str(tempDic["kWh"])
        dailyElectricityCosts.append(tempDic)
    return dailyElectricityCosts

    # Not sure how all this works, so not deleting it just yet
    # total_gallons = [a + b + c + d for a, b, c, d in zip(shower_gal, bath_gal, dishes_gal, laundry_gal)]
    # total_gallons_daily = [list(e) for e in zip(string_dates, total_gallons)]
    #
    # total_hot = [w + x + y + z for w, x, y, z in zip(shower_hot_gal, bath_hot_gal, dishes_hot_gal, laundry_hot_gal)]  # gives total gallons of hot water used
    # total_hot_daily = [list(e) for e in zip(string_dates, total_hot)]
    #
    # total_water_records =  [tuple(e) for e in zip (string_dates, total_gallons, total_hot)]

    #Note From Will: You can get rid of the lines below if you want, this is just for my testing/thinking purposes.
    # print("\n.....................................................................................")
    # print(f"Timestamp of this run: {datetime.datetime.now()}")
    # print("\n.....................................................................................")
    # print("\n")
    #
    # print("TODO (if needed) include some sort of diagnostic print stuff to test calculate_electricity_usage()")
