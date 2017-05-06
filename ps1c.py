#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 21:26:59 2017

@author: anna
"""


#initial parameters
semi_annual_raise=0.07
#total_raise=semi_annual_raise*6
r=0.04
total_cost=1000000
down_payment=total_cost*0.25
month=36
min_s=0
max_s=10000
min_save_rate=min_s/10000
max_save_rate=max_s/10000
steps=0
#ask user to input initial data
annual_salary=float(input('Enter your annual salary:'))
#make calculations
#monthly_salary=annual_salary/12
saving_rate=((min_s+max_s)/2)
savings=0
#savings=(monthly_salary*(saving_rate/10000)+monthly_salary*(saving_rate/10000)*r/12)*month
#
#    savings=(monthly_salary*(saving_rate/10000)+monthly_salary*(saving_rate/10000)*r/12)
#    if step%6==0:
#        monthly_salary=monthly_salary+monthly_salary*semi_annual_raise
#    print (savings)
while abs(savings - down_payment) >= 100 :
#    print('minimum saving rate=',min_save_rate, 'maximum savin rate=', max_save_rate, 'saving rate=', saving_rate)
    savings=0
    count=0
    monthly_salary=annual_salary/12
    while count<month:
        savings+=monthly_salary*(saving_rate/10000)+savings*r/12
        count+=1
        if count%6==0:
            monthly_salary=monthly_salary+monthly_salary*semi_annual_raise
#        print(monthly_salary)
#    savings=(monthly_salary*(saving_rate/10000)+monthly_salary*(saving_rate/10000)*r/12)*month
    if savings<down_payment:
        min_s=saving_rate
    else:
        max_s=saving_rate
    saving_rate=((min_s+max_s)/2)
    steps+=1
print('Steps in bisection search:', steps)
print('Best savings rate:', saving_rate/10000)



    
    
    








