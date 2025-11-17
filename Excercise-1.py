# -*- coding: utf-8 -*-
"""
Created on Sun Nov 16 19:34:58 2025

@author: Hi
"""

#1.Exercise 1: Age Calculator

#importing datetime 
from datetime import datetime
#defining function
def age_calculator():
    try:
        birth_input=input('enter birthdate in format(mm/dd/yyyy)')
        ## 1. Ask user for birth date
        try:
            birth_date=datetime.strptime(birth_input,'%m/%d/%Y')
        except ValueError:
            print('invalid dateformat')
            return
        # get today's date
        today=datetime.today()
        
        # check if birthdate in the future
        if birth_date>today:
            print('Birthdate cannot be in the future!')
        
        #calculate age in years
        age=today.year-birth_date.year
        
        ## Adjust age if birthday hasn't occurred yet this year
        if (today.month,today.day)<(birth_date.month,birth_date.day):
            age-=1
        # 4. Convert to European format
        European_format=birth_date.strftime('%d%m%Y')
        
        # Display results
        print(f'\n you are {age} years old')
        print(f'\n Your birthdate in European format is:{European_format}')
        
    except Exception as e:
        # Handle any unexpected errors
        print(f"An unexpected error occurred: {e}")
        
        
age_calculator()       
