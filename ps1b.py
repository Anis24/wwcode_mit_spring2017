#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 18:17:55 2017

@author: anna
"""

#ask user to input initial data
annual_salary=float(input('Enter your annual salary:'))
portion_saved=float(input('Enter the percent of your salary to save, as a decimal:'))
#portion_saved=float('0'+portion_saved)
semi_annual_raise=float(input('Enter the semi­annual raise, as a decimal:'))
#semi_annual_raise=float('0'+semi_annual_raise)
total_cost=float(input('Enter the cost of your dream home:'))
#make calculations
down_payment=total_cost*0.25
r=0.04
current_savings=0
month=0
monthly_salary=annual_salary/12
while current_savings<=down_payment:
    print(monthly_salary)
    current_savings+=monthly_salary*portion_saved+current_savings*r/12
    month+=1
    if month%6==0:
        monthly_salary=monthly_salary+monthly_salary*semi_annual_raise
#    print(current_savings)
print('Number of months:',month)

