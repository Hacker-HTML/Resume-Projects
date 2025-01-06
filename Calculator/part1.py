#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 19:04:37 2024

@author: shashwatpatel
"""

annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream house: "))
portion_down_payment = int(0.25 * total_cost)
portion_saved = portion_saved * (annual_salary/12)
current_savings = 0
month = 0
while current_savings < portion_down_payment:
    current_savings += portion_saved + (current_savings * 0.04)/(12)
    month+=1
print("Number of months: ", month)
