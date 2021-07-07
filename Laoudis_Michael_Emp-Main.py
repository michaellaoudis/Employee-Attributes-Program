#Created by Michael Laoudis


#This program is dependent on file 'Laoudis_Michael_Employee.py'

#The purpose of this program allows for a user to input employee attributes, which will be collected
#and then returned back to the user prompt. Shift time periods are assigned based on shift number input.



#import ProductionWorker & Employee Classes
import Laoudis_Michael_Employee


def main():
    
    
    #Local variables to store employee attributes (name, number, shift, hourly pay rate)
    super_name = ''
    super_emp_number = ''
    super_shift_num = 0
    super_hpr = 0.0
    
    
    #Retrieve data attributes from user
    super_name = input('Please enter the employee name: ')
    super_emp_number = input('Please enter the employee ID number: ')
    super_shift_num = int(input('Please enter the employee shift number: '))
    super_hpr = float(input("Please enter the employee's hourly pay rate: "))
    
    

    
    
    #Create employee object of Class ProductionWorker - pass local variables created in main
    employee = Laoudis_Michael_Employee.ProductionWorker(super_name, super_emp_number, super_shift_num, super_hpr)
    
    print("Employee information:")                           #Output title to user
    print("Name:", employee.get_name() )                     #Collect employee name from user by calling get_name()
    print("Employee Number:", employee.get_emp_number() )    #Collect employee number from user by calling get_emp_number()
    print("Shift Number:", employee.get_shift_num() )        #Collect shift number from user by calling get_shift_num()
    print("Hourly Pay Rate:", employee.get_hpr() )           #Collect hourly pay rate by calling get_hpr()
    





#Call the main function
main()