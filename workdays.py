#!/usr/bin/env python
# -*- coding: utf-8 -*-

import calendar
import datetime
my_calendar = calendar.Calendar()
months = [1,2,3,4,5,6,7,8,9,10,11,12]
years = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]

def show_month(current_year, current_month):
    dates = my_calendar.monthdatescalendar(current_year, current_month)
    # Initialize the counter
    holidays_count = 0
    workdays_count = 0
    # Define static holidays
    new_year = datetime.date(current_year, 1, 1)
    defender_of_ukraine_day = datetime.date(current_year, 10, 14)
    march_8 = datetime.date(current_year, 3, 8)
    
    for date in dates:
        for day in date:
            
            if (day.year == current_year) and (day.month == current_month):
                # Calendar module operates on weeks, so a week may contain previous
                # or next month's days.
                # That's why I have to filter those out.
                if (day == new_year or day == defender_of_ukraine_day or day == march_8) and (day.isoweekday() == 6 or day.isoweekday() == 7):
                    # static holiday is on weekend
                    holidays_count += 1
                elif (day == new_year or day == defender_of_ukraine_day or day == march_8) and (day.isoweekday() != 6 or day.isoweekday() != 7):
                    # static holiday on a regular day
                    holidays_count += 1
                elif (day.isoweekday() == 6 or day.isoweekday() == 7):
                    # just a Saturday or Sunday
                    holidays_count += 1
                else:
                    # Workday
                    workdays_count += 1
    return workdays_count, holidays_count

for year in years:
    total_workdays = 0
    total_holidays = 0
    for month in months:
        this_month_workdays, this_month_holidays = show_month(year,month)
        total_workdays += this_month_workdays
        total_holidays += this_month_holidays
    print (str(year) + " рік: " + str(total_workdays) + " робочих та " + str(total_holidays) + " вихідних днів")
