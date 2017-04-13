#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 21:02:25 2017

@author: anna
"""

#ask user to input initial data
annual_salary=float(input('Enter your annual salary:'))
portion_saved=input('Enter the percent of your salary to save, as a decimal:')
portion_saved=float('0'+portion_saved)
total_cost=float(input('Enter the cost of your dream home:'))
#make calculations
down_payment=total_cost*0.25
r=0.04
current_savings=0
month=0
while current_savings<=down_payment:
    current_savings+=(annual_salary/12)*portion_saved+current_savings*r/12
    month+=1
print('Number of months:',month)


