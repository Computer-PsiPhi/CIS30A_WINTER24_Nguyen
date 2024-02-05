"""CIS30A PROJECT NOEL PEREZ
NOTE: Requires Python 3.10 or later for "match" keyword. Previous version don't support this.
"""

import shoppingcart as sc
import utilities as utl
import person as prs
import customer as cust
 
def main():
    
    # Nested dictionary with available items for user to choose from 
    items = {
    1: ("Acoustic Guitar  ", 299.99),
    2: ("Electric Guitar  ", 729.99),
    3: ("Accordian        ", 1010.00),
    4: ("Drum Set         ", 1299.99),
    5: ("Bass Guitar      ", 679.99),
    6: ("Saxophone        ", 599.99),
    7: ("Clarinet         ", 800.00),
    8: ("Trumpet          ", 550.00),
    9: ("Flute            ", 600.00),
   10: ("Electric Piano   ", 399.99)
}
    cart = sc.ShoppingCart() # ShoppingCart object declaration
    sentinels = ["yes","yeah","ye","y","ye","ok","yea"] # Sentinel values for main menu while loop
    cont = "yes" # users choice to continue choosing from the menu choices
    
    # Prompts
    print("Welcome to Bob's Music Emporium!")
    print("Please Choose From The Menu.")
    
    # main while loop for menu choices
    while True:
        utl.show_menu() # display menu options. utl is from custom module
        menu = input("\nEnter your choice: ")
        
#  Match keyword can be used as Switch Case in Python which was introduced in Python 3.10 or later.
        match menu:
            case '1': # case 1 is for adding/purchasing to cart
                cont = "y"
                while cont in sentinels:
                    
                    utl.show_items(items) # show items user can choose from 
                    cart.display_cart()   # display what's in the cart while adding to it 
                    choice = int(input("\nPlease enter the number of the item you'd like to order: "))
                    
       # error checking with try/except block for              
                    try:
                        if(choice in items.keys()): # if the user's choice is valid, get the item, price and quanity of that item
                            item = items[choice][0]
                            price = items[choice][1]
                            quantity = (input(f"Quantity of {item.strip()}: "))
                            if(quantity.isdigit()): # make sure quantity they want is a valid digit 
                                quantity= int(quantity)
                            else:
                                quantity = int(input("Re-enter quantity: "))
                            cart.add_item(item,price,quantity)
                        else:
                            raise ValueError("Invalid item choice!") # raise an exception of the user chooses something not on the list 
                    except ValueError:
                        print("Error! Invalid Choice!")
                    cont = input("\nContinue adding items? (Y/N): ").lower() # ask if they want to continue shopping 
                     
            case '2': # case 2 is to remove items from the cart on the menu
                cart.remove_item() # shoppingcart class object has a remove_item() function
                
            case '3': # case 3 is for displaying what is in the cart currently. cart object has display_cart() method
                print("\nDisplaying Cart:")
                cart.display_cart() # call cart method to display it
                
            case '4': # case 4 is for checking out and scheduling a delivery date for the items
                
               # make sure the cart is not empty before checking out
                if(cart.isEmpty()): # call is_empty method from cart class
                    print("\nCannot Check Out: Cart Empty!")
                    continue 
                while True and not cart.isEmpty(): # loop for input validation 
                    print("\nNow Placing Order and Delivery Date.")
                   # Try/except block for input validation  
                    try:
              #do input validation for all the required variables needed to construct a customer object:
              #full name, complete adress and contact info
              #for all variables make sure input is: a string, not empty, and appropriate length
              #otherwise raise ValueError exception 
                        first_name = input("\nEnter first-name: ")
                        if not isinstance(first_name, str) or not first_name or len(first_name) > 20:
                            raise ValueError("First name must be a non-empty string.")

                        last_name = input("Enter last-name: ")
                        if not isinstance(last_name, str) or not last_name or len(last_name) > 20:
                            raise ValueError("Last name must be a non-empty string.")

                        address = input("Enter address: ")
                        if not isinstance(address, str) or not address or len(address) > 30:
                            raise ValueError("Address must be a non-empty string.")

                        city = input("Enter city: ")
                        if not isinstance(city, str) or not city or len(city) > 25:
                            raise ValueError("Address must be a non-empty string.")
            
                        state = input("Enter state: ")
                        if not isinstance(state, str) or not state or len(state) > 30:
                            raise ValueError("Address must be a non-empty string.")
                        
                        zip_code = input("Enter zip-code: ")
                        if not isinstance(state, str) or len(zip_code) != 5:
                            raise ValueError("Zip-code must be a non-empty string.")
            
                        phone_number = input("Enter phone number(###-###-####): ")
                        if not isinstance(phone_number, str) or len(phone_number) < 7 or len(phone_number) > 30:
                            raise ValueError("Phone number must be a non-empty string.")

                        email = input("Enter email: ")
                        if not isinstance(email, str) or '@' not in email or len(email) > 30:
                            raise ValueError("Email must be a non-empty string and must contain @.")
                
                # output prompt for user to verify the info they input 
                        print("\nVERIFY INFORMATION: IF INCORRECT PRESS 4 AGAIN.")
                        print("{:-^55s}".format(""))
                        print(first_name, last_name)
                        print(address, city, state,zip_code)
                        print(phone_number)
                        print(email) 
                        break    # after valid inputs, break out of the loop 
                    except ValueError: # exception block for try/except block
                        print("Invalid input!")
                        
           # create customer object with user's input once all user input has been validated and is good to go              
                customer_1 = cust.Customer(first_name, last_name, address, city,state, zip_code,phone_number, email)
                verify = input("\nIs Your Information Correct? (Y/N): ")
                verify = verify.lower()
          # once customer input has been verified then we can move onto the delivery date and time  
                if(verify == 'y'or verify =='yes'):
                    # calculate totatls: subtotal, tax, shipping, grand total so the customer object has correct amounts
                    # once it is sent to the create receipt function 
                        cart.calculate_totals()
                     # get the current date and time at this moment using import datetime in utilites module
                        now = utl.datetime.now()
                        
            # return the chosen delivery time and date variables so they can be passed to the receipt function to be printed
                        delivery_time, delivery_date = utl.get_selected_info()
    
                        # Get the current date and time
                        current_datetime = utl.datetime.now()

            # Extract current date and time as separate variables
                        current_date = current_datetime.date()  # Get current date
                        current_time = current_datetime.time()  # Get current time
    
            # Format the date and time
                        date_of_order = current_datetime.strftime("%B %d, %Y")
                        time_of_order = current_datetime.strftime("%I:%M:%S %p")
                    
    # Now everthing is ready to print the receipt
    # the utilities function has the print_receipt function which takes in the following parameters:
    # cart object, customer object, the desired delivery date and time, and the time and date the order took place 
                        utl.create_receipt(cart, customer_1, delivery_date, delivery_time, date_of_order, time_of_order)
                # Receipt with order details and all necessary information is printed for the customer in receipt.txt file
                        print("\nYour Recipet Has Been Printed!")
                        print("\nThanks For Shopping at Bob's Music Emporium!")
                        print("\nCheck receipt.txt")
                        break
            case '5': # user can by choosin option 5
                print("\nExiting!")
                break
            case _: # default case when invalid input is entered
                print("Invalid choice. Please try again.")
main()

