#Created by Michael Laoudis

#This program is a dependency for file 'Laoudis_Michael_Emp-Main.py' 


class Employee:
    #Initialize Employee attributes (name, number)
    def __init__(self, name, emp_number):
        self.__name = name
        self.__emp_number = emp_number
        
    #Mutator methods
        
        #Setters
    def set_name(self, name):
        self.__name = name
        
    def set_emp_number(self, emp_number):
        self.__emp_number = emp_number
    
    
        #Getters
    def get_name(self):
        return self.__name
    
    def get_emp_number(self):
        return self.__emp_number
    
class ProductionWorker(Employee):
    #Pass attributes inherited from Employee class
    def __init__(self, name, emp_number, shift_num, hpr):              #Initialize two new attributes (shift, hpr)
        
        #Call __init__ method from Employee class
        Employee.__init__(self, name, emp_number)
        
        #Set input to be either 1 or 2, otherwise output error
        if shift_num == 1 or shift_num == 2:
            self.__shift = shift_num
        else:
            raise ValueError('Please enter a Shift Number of 1 or 2.')
        
        
        #Private variables shift_num and hpr created
        self.__shift_num = shift_num
        self.__hpr = hpr
        

    
    #Mutator methods for new variables shift_num & hourly pay rate
        
        
    #Setters
        
        #User input shift number must be equal to 1 or 2, otherwise output error statement
    def set_shift_num(self, shift_num):
        if shift_num == 1 or shift_num == 2:
            self.__shift = shift_num
        else:
            raise ValueError('Please enter a Shift Number of 1 or 2.')
        
        #Set hpr to float value
    def set_hpr(self, hpr):
        self.__hpr = float(hpr)
        
        
    #Getters
        
        #Assign shift number 1 to return 'Day', number 2 to return 'Night'
    def get_shift_num(self):            
        if self.__shift_num == 1:
            return 'Day'
        else:
            return 'Night'       
        
        #Format hourly pay input to 2 decimal places
    def get_hpr(self):
        return format(self.__hpr, ',.2f')
        
        
    
    