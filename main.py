'''
        @Author: Viney Khaneja
        @Date: 2022-04-11 08:54AM
        @Last Modified by: Viney Khaneja
        @Last Modified time: None
        @Title : UC1_Check Employee Present or absent
    '''

print("Welcome to EmpWage Program in Python")

#Importing Random
import random

#CONSTANTS
IS_PRESENT = 2
IS_PART_TIME = 1
IS_ABSENT = 0
WAGE_PER_HOUR = 20
PART_TIME_HOURS = 4
FULL_DAY_HOURS = 8

def get_work_hours():
    '''
            Description: Function to get Employee Working hours
            Parameter: None
            Return: work_hrs as per Random Calculation
        '''
    #Variables
    work_hrs = 0
    emp_check = random.randint(0,2)

    if emp_check == IS_PRESENT:
        work_hrs = FULL_DAY_HOURS
    elif emp_check == IS_PART_TIME:
        work_hrs = PART_TIME_HOURS
    else:
        work_hrs = 0
    return work_hrs

daily_emp_wage = WAGE_PER_HOUR * get_work_hours()
print(f"Person earns {daily_emp_wage} rupees this day")