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
IS_PRESENT = 1

emp_check = random.randint(0,1)
if emp_check == IS_PRESENT:
    print("Employee is present")
else:
    print("Employee is absent")