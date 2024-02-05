"""This is my custom module with various methods I wrote and the GUI widget for scheduling
the delivery appointment for the customer's order.

It has 3 functions that I use in main.py which are show_menu, show_items, and create_receipt().
It has 2 additional functions that are used to create the GUI Widget and its functionality -
these are show_selected_info() and get_selected_info. This is where the Widget info is created and
the necessary components are hubbed. 
"""

from tkinter import *
from tkcalendar import Calendar
from datetime import datetime, timedelta


# function defintion for displaying the menu options to the user 
def show_menu():
    """This custom made function displays the available options to the user so
        they can choose. Menu driver.
    """
    print("\nMenu:")
    print("1. Shop For Items (Add Items To Cart)")
    print("2. Remove Items From Cart")
    print("3. Display Cart Items")
    print("4. Place Order And Delivery")
    print("5. Exit")
    
 # function definition for displaying nested dictionary of items. 
def show_items(items):
    """ Displays the listed items for sale in a nested dictionary containter.
        Takes in a dictionary called items as a parameter.
    """
    print("\nInstruments For Sale:")
    print("{:-^35s}".format(""))
    for key, (item, price) in items.items():
        print(f"{key}. {item}: ${price:.2f}")

# function definition used for GUI Widget calendar
def show_selected_info(calendar, time_spinbox, date_label,time_label,message_label):
    """ This function is used to display the information selected from the calendar widget button on
    on the console and updates the widget, meaning what the user selects from the Button and Spinbox is echoed back for the user
    to see on the shell output and on the widget as a visual cue. The function takes in a calendar object, spinbox object and label objects
    all of which are used to display info on the shell console from the widget and extracting necessary info. 
    """
    
    # get the date the user selected for the delivery so it can be used as needed
    selected_date = calendar.get_date()
     # get the time the user selected for the delivery so it can be used as needed
    selected_time = time_spinbox.get()
    
    print("\nDate Selected:", selected_date)
    print("Time Selected:", selected_time)
    print("Exit Widget or Select Other Date and Time For Delivery.")
    # echo back on widget what user selected as choice for delivery time and date
    date_label.config(text=f"Selected Delivery Date: {selected_date}")
    time_label.config(text=f"Selected Delivery Time: {selected_time}")
    
    # let user know they can exit the widget window to continue with program
    message_label.config(text="Exit to Continue.")

# function definition used for GUI Widget
def get_selected_info():
    """ This function creates the GUI widget and its components. The major components are the
    Calendar widget, the button on the widget, the time spinbox for the time of delivery and the
    various labels that are on the widget. 
    """
    # call the tkinder construtor for root
    root = Tk()
    root.title("Delivery Calendar")
    # PROMPT the user that the widget window has popped up incase they dont see it
    print("\nChoose Delivery Date & Time On Pop-up Widget.")
    print("\nAfter Selecting Date & Time, Exit the Window to Continue.")
    
    # get current time now so the correct calendar date is displayed
    now = datetime.now()
    # get the difference in time from now until one year so the user can only place order in 1 year time span
    one_year = now + timedelta(days=365)
    
    #create the Calendar object widget 
    calendar = Calendar(root, selectmode="day", year=now.year, month=now.month, day=now.day, showToday=True, mindate=now,maxdate=one_year)
    calendar.pack(padx=50, pady=10)
    
    # label for date seleted that will be passed into show_selected_info()
    date_label = Label(root, text="Selected Date: ")
    date_label.pack(pady=5)
    
    # label for time seleted that will be passed into show_selected_info()
    time_label = Label(root, text="Select Delivery Time:")
    time_label.pack()

# create Spinbox object that gives user the avialable times to choose from for their delivery  
    time_spinbox = Spinbox(root, values=("9:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", "2:00 PM", "3:00 PM", "4:00 PM", "5:00 PM"))
    time_spinbox.pack()

# create Button object that is used to select delivery time and date. This allows the information that has been selected to be extracted and used 
    select_button = Button(root, text="Press To Select Date & Time", command=lambda: show_selected_info(calendar, time_spinbox, date_label,time_label, message_label))
    select_button.pack(pady=5)
    
    message_label = Label(root, text="")
    message_label.pack(pady=5)
    
    # in order to return the delivery date and time selected they must be strings
    delivery_time = time_spinbox.get()
    delivery_date = calendar.get_date()
    root.mainloop()
    
    # return both values as strings so they can be used in the program
    return delivery_time, delivery_date


# Function for creating reciept for order
def create_receipt(cart, customer, delivery_date, delivery_time, date_of_order, time_of_order):
    """ This function takes in a cart object, customer object, the selected delivery date and time from the user's
    Calendar widget selection, as well as the time and date the order was made. Each receipt has a unique invoice number
    and a customer number that is associated with it - this is printed on the receipt. Otherwise the function prints all the
    customer info like their complete name, address, contact info, subtotal, taxes, shipping and grand total for the customer
    to see on the reciept.txt file. 
    """
    
    # display the cart so the customer can see what items will be printed on the reciept 
    cart.display_cart()
    
    # exception handling
    try:
        # Open the file in write mode
        with open("receipt.txt", 'w') as file:
            # Write header
            file.write("========================================\n")
            file.write(f"            Receipt #{customer.get_invoice_num()}\n")
            file.write("========================================\n")

            # Write order details
            file.write(f"Customer #{customer.get_cust_num()} Information:")
            file.write(f"\n{customer.get_full_name()}")
            file.write(f"\n{customer.get_full_addrss()}")
            file.write(f"\n{customer.get_contact()}")
            file.write(f"\nDate of Order: {date_of_order}")
            file.write(f"\nTime of Order: {time_of_order}")
            file.write(f"\nScheduled Delivery Date: {delivery_date}")
            file.write(f"\nScheduled Delivery Time: {delivery_time}")
            file.write("\n----------------------------------------\n")

            # Write items and prices on receipt
            file.write(f"ITEM                 PRICE        QTY\n")
            for item_name, item_info in cart.cart_items.items():
                file.write(f"\n{item_name:5} -  ${item_info['price']:7.2f}  -  {item_info['quantity']}")
                
            # Get totals
            sub_total,taxes,shippping,grand_total = cart.calculate_totals()

            # Write totals
            file.write("\n----------------------------------------")
            file.write(f"\nSub-total     :                ${sub_total:7.2f}")
            file.write(f"\nTaxes(7.75%)  :                ${taxes:7.2f}")
            file.write(f"\nShipping(9.0%):                ${shippping:7.2f}")
            file.write(f"\nGrand Total   :                ${grand_total:7.2f}\n")
            file.write("========================================\n")
            file.write("               Thank you!\n")
            file.write("========================================\n")
    finally:
        # close file
        file.close()

    