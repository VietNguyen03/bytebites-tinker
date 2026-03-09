# ByteBites Core Models
# Classes: Customer, FoodItem, Menu, Transaction


class Customer:
    """Customer class for managing customer information and purchase history."""
    
    def __init__(self, name, purchase_history=None):
        """
        Initialize a Customer.
        
        Args:
            name (str): The customer's name
            purchase_history (list, optional): List of past purchases. Defaults to empty list.
        """
        self.name = name
        self.purchase_history = purchase_history if purchase_history is not None else []


class FoodItem:
    """FoodItem class for food products on the menu."""
    
    def __init__(self, name, price, category, rating):
        """
        Initialize a FoodItem.
        
        Args:
            name (str): The food item's name
            price (float): The food item's price
            category (str): The food item's category
            rating (int): The food item's rating
        """
        self.name = name
        self.price = price
        self.category = category
        self.rating = rating


class Menu:
    """Menu class for managing food items."""
    
    def __init__(self, all_items=None):
        """
        Initialize a Menu.
        
        Args:
            all_items (list, optional): List of FoodItem objects. Defaults to empty list.
        """
        self.all_items = all_items if all_items is not None else []
    
    def filter_by_category(self, category_name):
        """
        Filter menu items by category.
        
        Args:
            category_name (str): The category to filter by
        """
        pass
    
    def sort_by_popularity(self):
        """
        Sort menu items by popularity (rating).
        """
        pass


class Transaction:
    """Transaction class for managing food purchases."""
    
    def __init__(self, items=None, customer=None):
        """
        Initialize a Transaction.
        
        Args:
            items (list, optional): List of FoodItem objects in the transaction. Defaults to empty list.
            customer (Customer, optional): The customer making the purchase.
        """
        self.items = items if items is not None else []
        self.customer = customer
    
    def add_item(self, item):
        """
        Add a food item to the transaction.
        
        Args:
            item (FoodItem): The food item to add
        """
        pass
    
    def calculate_total(self):
        """
        Calculate the total cost of the transaction.
        
        Returns:
            float: The total cost
        """
        pass