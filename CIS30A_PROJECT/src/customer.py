"""Customer class inherits from Person class - it is a sub-class of the Person class
    It inherits all the parents member variables and methods.
    It also has 2 additional member variables and 2 more member methods apart from
    what it inherits.
"""
from person import Person
import random as rand

class Customer(Person):
    """Apart from inheriting from the parent class, this Customer class has 2 unique member variables
    of its own which are a customer number(cust_num) and invoice number (invoice_num) for their order.
    There are also 2 member funtions for returning these variables as needed.
    """
    def __init__(self,first_name, last_name, address,city,state,zip_code, phone_number, email):
        super().__init__(first_name, last_name, address,city,state,zip_code ,phone_number, email)
        self.cust_num = self.first_name[0]+self.last_name[0]+str(rand.randrange(1,999999)) # assign the customer a unique customer number
        self.invoice_num = str(rand.randrange(1,10000000)) # assign customer's invoice a number
   
   # function definition for getting the customer number member variable
    def get_cust_num(self):
        """This member function returns the customer object's unique customer ID as a
        formatted string
        """
        num = f"{self.cust_num}"
        return num
        
   # function definition for getting the invoice number member variable
    def get_invoice_num(self):
        """This member function returns the customer object's unique receipt number as a
        formatted string
        """
        inv_num= f"{self.invoice_num}"
        return inv_num