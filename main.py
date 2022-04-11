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

#Constants Class to get Constants for the Programs
class Constants:
    IS_PRESENT = 2
    IS_PART_TIME = 1
    IS_ABSENT = 0
    WAGE_PER_HOUR = 20
    PART_TIME_HOURS = 4
    FULL_DAY_HOURS = 8
    MAX_WORKING_DAYS_PER_MONTH = 20

def get_work_hours():
    '''
            Description: Function to get Employee Working hours
            Parameter: None
            Return: work_hrs as per Random Calculation
        '''
    #Variables
    work_hrs = 0
    emp_check = random.randint(0,2)

    match emp_check:
        case Constants.IS_PRESENT:
            work_hrs = Constants.FULL_DAY_HOURS
        case Constants.IS_PART_TIME:
            work_hrs = Constants.PART_TIME_HOURS
        case Constants.IS_ABSENT:
            work_hrs = 0
    return work_hrs

monthly_emp_wage = 0
for i in range(1,Constants.MAX_WORKING_DAYS_PER_MONTH + 1):
    monthly_emp_wage += Constants.WAGE_PER_HOUR * get_work_hours()

print(f"Person earns {monthly_emp_wage} rupees this month")