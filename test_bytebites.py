import pytest
from models import Customer, FoodItem, Menu, Transaction


def test_transaction_calculate_total_multiple_items():
    """Test that Transaction.calculate_total() works with multiple items."""
    # Create test items
    item1 = FoodItem("Burger", 10.50, "Main", 4)
    item2 = FoodItem("Fries", 3.50, "Side", 5)
    item3 = FoodItem("Soda", 2.00, "Beverage", 3)
    
    # Create transaction and add items
    transaction = Transaction()
    transaction.add_item(item1)
    transaction.add_item(item2)
    transaction.add_item(item3)
    
    # Verify total is correct
    assert transaction.calculate_total() == 16.00


def test_transaction_calculate_total_empty():
    """Test that Transaction.calculate_total() returns 0 when no items are added."""
    transaction = Transaction()
    assert transaction.calculate_total() == 0


def test_menu_filter_by_category():
    """Test that Menu.filter_by_category() only returns items from the correct category."""
    # Create test items with different categories
    burger = FoodItem("Burger", 10.50, "Main", 4)
    fries = FoodItem("Fries", 3.50, "Side", 5)
    salad = FoodItem("Salad", 8.00, "Main", 4)
    soda = FoodItem("Soda", 2.00, "Beverage", 3)
    
    # Create menu with items
    menu = Menu([burger, fries, salad, soda])
    
    # Filter by "Main" category
    main_items = menu.filter_by_category("Main")
    
    # Verify only Main category items are returned
    assert len(main_items) == 2
    assert burger in main_items
    assert salad in main_items
    assert fries not in main_items
    assert soda not in main_items