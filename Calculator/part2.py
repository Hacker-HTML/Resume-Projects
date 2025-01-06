#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 19:04:37 2024

@author: shashwatpatel
"""

annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream house: "))
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal:"))
portion_down_payment = 0.25 * total_cost
monthly_salary = portion_saved * (annual_salary/12)
current_savings = 0
month = 0
while current_savings < portion_down_payment:
    current_savings += monthly_salary + (current_savings * 0.04)/(12)
    month+=1
    if month%6==0:
        monthly_salary += semi_annual_raise * monthly_salary
print("Number of months: ", month)
