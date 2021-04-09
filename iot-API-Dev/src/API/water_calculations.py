
import datetime
from datetime import timedelta, date, time

import numpy
import numpy as np
import random
# returns lists of water usage calculations for each day jan 1 - april 30

# lists to be used across functions
dates = []
string_dates = []

shower_gal = []
bath_gal = []
shower_hot_gal = []
bath_hot_gal = []

dishes_gal = []
dishes_hot_gal = []
laundry_gal = []
laundry_hot_gal = []

daily_cost = []
total_hot = []

heat_times = []
water_kw_per_day = []


# values to be used across functions
rand_day = random.sample(range(1, 7), 4)

gal_per_dishes = 6
hot_per_dishes = 6

gal_per_laundry = 20
hot_per_laundry = 17

gal_per_shower = 25
hot_per_shower = 16.25

gal_per_bath = 30
hot_per_bath = 19.5

water_cost_per_gallon = .00336898395

# Carter, date_range and create_date is super useful for getting a list of each day to match your calculations up with
def date_range():

    start_dt = date(2021, 1, 1)  # jan 1st
    end_dt = date(2021, 4, 30)  # april 30th

    for n in range(int((end_dt - start_dt).days)+1):
        yield start_dt + timedelta(n)


def create_dates():

    for dt in date_range():
        date = dt  # date objects to use in calculating weekdays
        string_date = dt.strftime("%Y-%m-%d")  # string of dates to use in final list
        dates.append(date)
        string_dates.append(string_date)
    return dates, string_dates

'''
returns the total gallons used and total hot gallons used per day by baths and showers
'''
def shower_and_bath():

    date_range()
    create_dates()

    for i in dates:
        if i.weekday() <= 4:  # weekdays
            total_shower_gallons = (gal_per_shower*3)
            total_shower_hot = (hot_per_shower*3)

            total_bath_gallons = (gal_per_bath*3)
            total_bath_hot = (hot_per_bath * 3)

            shower_gal.append(total_shower_gallons)
            shower_hot_gal.append(total_shower_hot)
            bath_gal.append(total_bath_gallons)
            bath_hot_gal.append(total_bath_hot)


        if i.weekday() > 4:  # weekends
            total_shower_gallons = (gal_per_shower*2)
            total_shower_hot = (hot_per_shower*2)

            total_bath_gallons = (gal_per_bath*2)
            total_bath_hot = (hot_per_bath * 2)

            shower_gal.append(total_shower_gallons)
            shower_hot_gal.append(total_shower_hot)
            bath_gal.append(total_bath_gallons)
            bath_hot_gal.append(total_bath_hot)

    '''
    TODO: 
    when shower event happens: add gal_per_shower to value for that date and hot_per_shower to value 
    for that date (or maybe this should be done in the API)

    This also needs to be done for all other events as well
    '''

    return (shower_gal, shower_hot_gal, bath_gal, bath_hot_gal)


'''
returns the total gallons used and total hot gallons used per day by dishwasher and washing machine
'''
def dishes_and_laundry():

    # happen 4 times a week - randomly decided per day
    date_range()
    create_dates()

    for i in dates:
        
        if i.weekday() in rand_day:
    
            total_dishes_gallons = (gal_per_dishes)
            total_dishes_hot = (hot_per_dishes)

            total_laundry_gallons = (gal_per_laundry)
            total_laundry_hot = (hot_per_laundry)

            dishes_gal.append(total_dishes_gallons)
            dishes_hot_gal.append(total_dishes_hot)
            laundry_gal.append(total_laundry_gallons)
            laundry_hot_gal.append(total_laundry_hot)

        else:
            total_dishes_gallons = 0
            total_dishes_hot = 0

            total_laundry_gallons = 0
            total_laundry_hot = 0

            dishes_gal.append(total_dishes_gallons)
            dishes_hot_gal.append(total_dishes_hot)
            laundry_gal.append(total_laundry_gallons)
            laundry_hot_gal.append(total_laundry_hot)


    return (dishes_gal, dishes_hot_gal, laundry_gal, laundry_hot_gal)

'''
 returns 3 lists
 1. list of date string, totals gallons of water used, and total gallons of hot water used for each day - total_water_records
 2. list of totals gallons of water used each day - total_gallons
 3. list of total gallons of hot water used each day - total_hot

 The last 2 are returned so they can be used in other functions for cost and energy usage calculations
 '''
def calculate_water_usage():
    date_range()
    shower_and_bath()
    dishes_and_laundry()

    #Carter, the syntax used to add all the gallons for each day will be useful when you add the water energy used to the rest of the energy used per day

    total_gallons = [a + b + c + d for a, b, c, d in zip(shower_gal, bath_gal, dishes_gal, laundry_gal)] # adds up gallons used by all methods for each day
    total_gallons_daily = [list(e) for e in zip(string_dates, total_gallons)] # creates a list of date and total gallons used for each day

    total_hot = [w + x + y + z for w, x, y, z in zip(shower_hot_gal, bath_hot_gal, dishes_hot_gal, laundry_hot_gal)]  # adds up hot water gallons used by all methods for each day
    total_hot_daily = [list(e) for e in zip(string_dates, total_hot)] # creates a list of date and total hot water gallons used for each day

    total_water_records =  [tuple(e) for e in zip (string_dates, total_gallons, total_hot)] # creates a tuple of the date, total gal, and total hot for each day.
    # total_water_records is what is used in the api to enter the data into the database


    #Note From Will: You can get rid of the lines below if you want, this is just for my testing/thinking purposes.
    '''
    print("\n.....................................................................................")
    print(f"Timestamp of this run: {datetime.datetime.now()}")
    print("\n.....................................................................................")
    print("\nExecuted water_calculations.caclulate_water_usage function, which handles the following calculations:")
    print("\ntotal_gallons_daily\n total gallons\n total_hot\n and total_hot_daily")
    print(f"\n      _______________ \n        total_gallons\n      _______________\n{total_gallons}\n")
    print(f"\n      _______________ \n        total_gallons_daily\n      _______________\n{total_gallons_daily}")
    print(f"\n      _______________ \n       total_hot\n      _______________\n{total_hot}\n")
    print(f"\n      _______________ \n       total_hot_daily\n      _______________\n {total_hot_daily}")



    print("~~~~~~~~~`\n\ndate, total_gallons, hot_gallons\n\n" ,total_water_records,"\n\n~~~~~~~~~~~~~`")



    print("\n.....................................................................................")
    '''
    
    return total_water_records,total_gallons, total_gallons_daily


'''
returns tuple of the string date and cost of water used for each day - total_cost_daily
should be put into a database
'''
def calculate_water_cost():

    date_range()
    calculate_water_usage()

    total_gallons_cost = [a + b + c + d for a, b, c, d in zip(shower_gal, bath_gal, dishes_gal, laundry_gal)]

    for j in total_gallons_cost:
        cost = j * water_cost_per_gallon
        daily_cost.append(cost)

    total_cost_daily = [tuple(e) for e in zip(string_dates, daily_cost)]

    return total_cost_daily

'''
returns list of kw used per day from hot water usage
should be added to total daily electricity usage in Carter's electricity calculation function
'''
def calculate_water_electric_usage():
    date_range()
    calculate_water_usage()

    total_hot = [w + x + y + z for w, x, y, z in zip(shower_hot_gal, bath_hot_gal, dishes_hot_gal, laundry_hot_gal)] 


    for i in total_hot:
        hours_to_heat = round(((i * 4)/60),2)
        heat_times.append(hours_to_heat)


    for j in heat_times:
        water_kw_used = round(j * 4.5,2)
        water_kw_per_day.append(kw_used)

    return water_kw_per_day