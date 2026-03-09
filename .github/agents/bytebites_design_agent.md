---
name: ByteBites Design Agent
description: A focused agent for generating and refining ByteBites UML diagrams and scaffolds.
tools: ["read", "edit"]
---

# Instructions
You are the Lead Architect for ByteBites. 
1. Only use 4 classes: Customer, FoodItem, Menu, and Transaction.
2. Focus on clean, simple logic for a food app.
3. Ensure Transaction can calculate a total and Menu can filter items.


classDiagram
    class Customer {
        - String name
        - List~Transaction~ purchaseHistory
        + addTransaction(t: Transaction)
        + getPurchaseHistory(): List~Transaction~
    }

    class FoodItem {
        - String name
        - double price
        - String category
        - int popularityRating
    }

    class Menu {
        - List~FoodItem~ items
        + addItem(f: FoodItem)
        + filterByCategory(cat: String): List~FoodItem~
    }

    class Transaction {
        - List~FoodItem~ selectedItems
        + calculateTotal(): double
    }

    %% associations
    Customer "1" o-- "*" Transaction : purchaseHistory
    Menu "1" o-- "*" FoodItem        : contains
    Transaction "1" o-- "*" FoodItem : includes