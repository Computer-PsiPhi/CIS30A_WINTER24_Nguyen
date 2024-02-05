# CIS30A Project - Bob's Music Emporium

This Python project simulates an online shopping experience for Bob's Music Emporium. Users can browse through available items, add them to their cart, remove items, and proceed to checkout by providing their personal information for delivery.

## Prerequisites

- Python 3.10 or later is required due to the use of the `match` keyword introduced in Python 3.10.

## Project Structure

The project consists of the following files:
- `main.py`: Contains the main function to drive the program.
- `shoppingcart.py`: Defines the `ShoppingCart` class for managing items in the cart.
- `utilities.py`: Contains utility functions used throughout the project, including menu display, input validation, and receipt generation.
- `person.py`: Defines the `Person` class, which represents a generic person with attributes such as complete name, addreess, and contact information.
- `customer.py`: Defines the `Customer` class, which inherits from the `Person` class and represents a customer with additional attributes like customer number and their
-  `unique invoice number.

## Usage

1. Run the `main()` function defined in `main.py`.
2. Browse items, add them to the cart, and proceed to checkout by providing personal information.
3. Provide your personal information for delivery when prompted and schedule delivery date and time using the GUI widget.
4. Once the order is complete, a receipt will be generated and saved to `receipt.txt`.

## Features

- **Browse Items**: Users can view available items along with their prices.
- **Add and Remove Items**: Users can add items to their cart and remove them if necessary.
- **Checkout and Delivery**: Users can proceed to checkout, providing their personal information for delivery scheduling.
- **Receipt Generation**: After successful checkout, a receipt is generated and saved to `receipt.txt`.


Thank you for using Bob's Music Emporium shopping simulator!


### ShoppingCart Class

- **Dictionary for Cart Items**: The `ShoppingCart` class manages a dictionary of items added to the cart along with their prices and quantities.
- **Empty Cart Check**: The `isEmpty()` method checks if the shopping cart is empty.
- **Add Items**: Users can add items to the cart using the `add_item()` method.
- **Remove Items**: Items can be removed from the cart with the `remove_item()` method.
- **Display Cart**: The `display_cart()` method shows the items in the cart along with their prices and quantities.
- **Total Calculation**: The `calculate_totals()` method calculates the subtotal, tax, shipping, and grand total for items in the cart.

### Customer Class

- **Inherits from Person Class**: The `Customer` class inherits from the `Person` class and includes additional attributes like a customer number and invoice number.
- **Customer Information**: It includes methods to retrieve the customer's unique number and invoice number.

### Utilities Module

- **Menu Display**: The `show_menu()` function displays available options to the user.
- **Item Display**: The `show_items()` function lists available items for sale.
- **Receipt Generation**: The `create_receipt()` function creates a receipt with order details, customer information, and totals.
- **Delivery Scheduling Widget**: Functions `show_selected_info()` and `get_selected_info()` manage a GUI widget for selecting delivery dates and times.

## Requirements

The project meets the following requirements as specified:

- **Tkcalendar Integration**: Tkcalendar is used for selecting delivery date and time.

- **User Interaction and Display**:
  - The program prompts the user to select products and delivery date and time from the available options in the 1-year span.
  - Displays the user selection on the screen.

- **Order Summary and Output**:
  - Program outputs the order summary and appointment in a text file.

- **Components**:
  - Include comments throughout the program 
  - Use variables and lists (or tuples/dictionaries) to store and access data
  - Utilize string objects to display and control text output 
  - Define 2 or more functions and use function calls to execute tasks - stored in utilities.py
  - Implement loops (for, while, or both) 
  - Include conditional statements (if, if-else, or if-elif-else)
  - Use a non-built-in module (custom module) 
  - Contains at least 2 classes and 1 sub-class 
  - Includes 1 or more objects and 1 or more methods in each class 
  - Implement error detection using Python built-in exceptions 
  - Implement file operations and file output 
  - Integrate GUI 
