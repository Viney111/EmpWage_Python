'''
        @Author: Viney Khaneja
        @Date: 2022-04-11 08:54AM
        @Last Modified by: Viney Khaneja
        @Last Modified time: 2022-04-12 10:29AM
        @Title : EmpWage Problem Statements
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
    MAX_WORK_HRS_PER_MONTH = 100

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

def calculate_emp_wage():
    '''
            Description: Function to calculate monthly and daily employee wage
            Parameter: None
            Return: Nothing, just prints the monthly Wage & emp wage day-wise
        '''
    #Initializing Variables with zero value
    monthly_emp_wage = total_work_hrs = total_work_days = daily_wage = 0
    daily_wage_dict = {}
    #Applying Conditions of Max Working days and hours in Whie Loop
    while total_work_hrs <= Constants.MAX_WORK_HRS_PER_MONTH and total_work_days < Constants.MAX_WORKING_DAYS_PER_MONTH:
        work_hrs_per_day = get_work_hours() #Calling GetWorkHrs Function...
        daily_wage = work_hrs_per_day * Constants.WAGE_PER_HOUR
        total_work_hrs += work_hrs_per_day
        total_work_days += 1
        daily_wage_dict[total_work_days] = daily_wage

    monthly_emp_wage = Constants.WAGE_PER_HOUR * total_work_hrs
    print(f"Person earns {monthly_emp_wage} rupees this month & Daily Emp Wage daywise:\n{daily_wage_dict} respectively.")

if __name__ == "__main__":
    calculate_emp_wage()