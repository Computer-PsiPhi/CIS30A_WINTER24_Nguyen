"""ShoppingCart class has a dictionary cart_items, the tax rate and ship rate as member variables
Items are added to the shoppingcart object in main which the class holds in a dictionary  
"""

class ShoppingCart:
    """Shopping cart class with 3 member variables and 5 member functions
    """
    def __init__(self):
        self.cart_items={}
        self.tax_rate = 0.0775
        self.ship_rate = 0.09
 
 # function definition for checking if the cart is empty 
    def isEmpty(self):
        """Check if the shopping cart is empty or not
        """
        if not self.cart_items:
            return True
        else:
            return False
        
  # function definition for adding items to the cart object    
    def add_item(self,item,price,quantity):
        """Check if the item is in the cart; if it is not then add that item
        with its corresponding price and the quantity. If it is only update the quantity
        """
        if (item not in self.cart_items):
            self.cart_items[item] = {"price": price, "quantity": quantity}
        else:
            self.cart_items[item]["quantity"] = quantity
 
 # function definition removing items from the cart object
    def remove_item(self):
        """If the cart is empty do nothing. Otherwise display what is in the cart
        and let the user choose what to remove by picking the number associated with the item.
        Do some exception handling with input validation so only valid items and quantities can
        be removed.
        """
        
        # if empty do nothing
        if self.isEmpty():
            print("\nCart is empty.")
            return

        print("\nItems in Cart:")
        for i, (item_name, item_info) in enumerate(self.cart_items.items(), 1):
            print(f"{i}. {item_name} - Quantity: {item_info['quantity']}")

        choice = input("\nEnter the number of the item to remove: ")
    # try/except block so user can only remove items that are in the cart and for valid quantities, meaning
    # let them remove more items than are actually in the cart 
        try:
            choice = int(choice)
            if 1 <= choice <= 10: # check to remove number of item that is acutally on the list of items
                item_to_remove = list(self.cart_items.keys())[choice - 1]
                quantity_to_remove = int(input(f"Enter the quantity of {item_to_remove}to remove: "))
                if quantity_to_remove < 0 or quantity_to_remove > self.cart_items[item_to_remove]["quantity"]:
                    print("\nInvalid quantity!")
                elif quantity_to_remove == self.cart_items[item_to_remove]["quantity"]:
                    del self.cart_items[item_to_remove]
                    print(f"{item_to_remove:5} removed from the cart.")
                else:
                    self.cart_items[item_to_remove]["quantity"] -= quantity_to_remove
                    print(f"{quantity_to_remove} {item_to_remove}removed from the cart.")
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError: # end of try/except block
            print("Invalid input. Please enter a number.")
            
 # function definition for displaying what is in the cart         
    def display_cart(self):
        """If the cart has item(s) in it show the name, price and quantity of the item(s)
            and a running total so far; otherwise let them know it is empty 
        """
        if (self.cart_items):
            sub_total=0
            print("\nShopping Cart Status:")
            print("{:-^55s}".format(""))
            for item_name, item_info in self.cart_items.items():
                sub_total += item_info["price"]*item_info["quantity"]
                print(f"{item_name:5} -  Price: ${item_info['price']:7.2f}  - Quantity: {item_info['quantity']}")
            print("{:-^55s}".format(""))
            print(f"Sub-Total: ${sub_total:.2f}")
        else:
            print("\nCart is Empty.")
  
  # function definition for calculating various totals needed in program
    def calculate_totals(self):
        """This function calculates the subtotal, tax rate, shipping rate, and grand total of the items
        in the cart. It returns all these values separatly so they can be used in the program. 
        """
        sub_total = 0
        shippping=0
        taxes=0
        grand_total=0
        # get subtotal which is based on price and quantity of each item
        for item_info in self.cart_items.values():
            sub_total += item_info["price"] * item_info["quantity"]
        
        taxes = sub_total*self.tax_rate
        shippping = sub_total*self.ship_rate
        grand_total = sub_total+taxes+shippping
# multi value returning function 
        return sub_total,taxes,shippping,grand_total
    

