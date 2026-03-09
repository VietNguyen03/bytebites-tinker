# ByteBites System Design

## Class Diagram
- **Customer**
  - Attributes: name (str), purchase_history (list)
- **FoodItem**
  - Attributes: name (str), price (float), category (str), rating (int)
- **Menu**
  - Attributes: all_items (list)
  - Methods: filter_by_category(category_name), sort_by_popularity()
- **Transaction**
  - Attributes: items (list), customer (Customer)
  - Methods: add_item(item), calculate_total()