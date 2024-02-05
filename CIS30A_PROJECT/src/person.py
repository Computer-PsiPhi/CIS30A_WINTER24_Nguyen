"""Person class - base class for Customer class
    This class 8 member variables and 3 member functions
"""
class Person:
    def __init__(self, first_name, last_name, address,city,state,zip ,phone_number, email):
        """Peson class: 
        """
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone_number = phone_number
        self.email = email
  
  # function definition for getting the person's full name
    def get_full_name(self):
        """ This member function gets the person's full name which is
        thier first name and last name and returns it as a formmated string
        """
        full_name = f"{self.first_name} {self.last_name}"
        return full_name
    
 # funcion definition for getting the complete address of a person object 
    def get_full_addrss(self):
        """This member function gets the complete address of a person as one
        complete entity, this includes street number/address, city , state, and zip code
        The address is formatted and the function returns it.
        """
        full_address = f"{self.address} \n{self.city}, {self.state} {self.zip}"
        return full_address
   
  # function definition for retrieving a person object's contact info
    def get_contact(self):
        """This member function returns the Persons object contact information
        which is phone number and email address as a formatted string. 
        """
        contact = f"Phone: {self.phone_number} \nEmail: {self.email}"
        return contact
    
   



