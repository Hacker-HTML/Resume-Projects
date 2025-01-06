#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 19:04:37 2024

@author: shashwatpatel
"""

annual_salary = int(input("Enter the starting salary: "))
low = 0
high = 1
portion_saved = (low+high) / 2
epsilon = 0.01
total_cost = 1000000
semi_annual_raise = .07
portion_down_payment = 0.25 * total_cost
monthly_salary = portion_saved * (annual_salary/12)
current_savings = 0
month = 0
count = 0

max_monthly = (annual_salary/12)
for month in range(36):
    current_savings += max_monthly + (current_savings * 0.04)/(12)
    month+=1
    if month%6==0:
        max_monthly += semi_annual_raise * max_monthly

if current_savings < portion_down_payment:
    print("It is not possible to pay the down payment in three years.")
else:
    
    while abs(current_savings - portion_down_payment) >= epsilon:
        
        while month < 36:
            current_savings += monthly_salary + (current_savings * 0.04)/(12)
            month+=1
            if month%6==0:
                monthly_salary += semi_annual_raise * monthly_salary
        if current_savings > portion_down_payment:
            high = portion_saved
        else:
            low = portion_saved
            
        if(abs(current_savings - portion_down_payment) <= epsilon):
            break
        current_savings = 0
        portion_saved = (high + low) / 2
        monthly_salary = portion_saved * (annual_salary/12)
        month = 0
        count+=1
    
        
    print("Best savings rate:", portion_saved)
    print("Steps in bisection search ", count)
