# CIS30A Project - Bob's Music Emporium

This Python project simulates an online shopping experience for Bob's Music Emporium. Users can browse through available items, add them to their cart, remove items, and proceed to checkout by providing their personal information for delivery.

## Prerequisites

- Python 3.10 or later is required due to the use of the `match` keyword introduced in Python 3.10.

## Project Structure

The project consists of the following main files:

- `shoppingcart.py`: Defines the `ShoppingCart` class responsible for managing the items in the user's cart.
- `utilities.py`: Contains utility functions used throughout the project, including menu display, input validation, and receipt generation.
- `person.py`: Defines the `Person` class, which represents a generic person with attributes such as name and contact information.
- `customer.py`: Defines the `Customer` class, which inherits from the `Person` class and represents a customer with additional attributes like address and email.

## Usage

1. Run the `main()` function defined in `main.py`.
2. Follow the prompts displayed in the command-line interface to browse items, add them to the cart, and proceed to checkout.
3. Provide your personal information for delivery when prompted.
4. Once the order is confirmed, a receipt will be generated and saved to `receipt.txt`.

## Features

- **Browse Items**: Users can view available items along with their prices.
- **Add and Remove Items**: Users can add items to their cart and remove them if necessary.
- **Checkout and Delivery**: Users can proceed to checkout, providing their personal information for delivery scheduling.
- **Receipt Generation**: After successful checkout, a receipt is generated and saved to `receipt.txt`.


Thank you for using Bob's Music Emporium shopping simulator!

