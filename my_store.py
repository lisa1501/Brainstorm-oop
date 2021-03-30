# # Intro to OOP Activity

# ### Learning Goals
#   * Use correct syntax to construct a Class and initialize an instance of the Class
#   * Consider the following problems and come up with a solution through Class methods


# ### Brainstorm
# We've opened our very own store, shop, bakery, etc.! Think of a name for your new business, as well as at least 3-4 items your business would likely sell. This can be hair care products, baked good, clothing, whatever!

# **Time**: 5 minutes in small group

# Now that we've got an idea, let's turn it into a Class. Here is a blueprint:

#   ``` python
#   class Store:
#     def __init__(self):
#       # we need a name, 
#       # a collection of our items with a price and a quantity
#       # a collection of the store's owners' names

#     # here are some methods we will create later
#     def welcome_message(self):
#       pass

#     def sell_items(self):
#       pass
#   ```
# ---

# ### Class Construction
# Fill out your "constructor" method, which will *init*ialize instances of your Store. There are three required attributes we need. Think of any others you might want? Add 'em!

# **Time**: 5 minutes in small group

# **Questions**: What did you come up with to hold all of your Store items? Did you add any extra attributes?

# ---

# ### Welcome Message
# This method will print out:
# 1. a welcome message that states the shop's name
# 2. the shop owners
# 3. all items the shop will sell (plus price).

# **Time**: 10-15 minutes in small group

# ---

# ### Sell Items
# This method takes in a string `item_name` that represents an item. 
# 1. Print a successful checkout message of the item sold.
# 2. Decrease the quantity of that item in your shop.

# **Time**: 25-30 minutes in small group
# **Question**: Are we missing some things? Can you think of some additional features we should add to this method to make it more robust? Do so now!


# ### Group Talk
# Let's use the remaining time to present our solutions!


class Store:
    def __init__(self, store_name, address, item):
        # we need a name, 
        # a collection of our items with a price and a quantity
        # a collection of the store's owners' names
        self.store_name = store_name
        self.address = address
        # dict key=item_name value = Q {donut: 25}
        self.item = item

    # here are some methods we will create later
    def welcome_message(self):
        print(f"Welcome to {self.store_name}!")

    def sell_items(self, item_name):        
        for item in self.item:
            if item["name"] == item_name:
                if item["quantity"] > 0:
                    item["quantity"] -= 1
                    print(f"One {item_name} is sold.")


top10bakery = Store("top 10 bakery", "101 1st Ave", [{"name": "donuts","price": 5,"quantity": 20},{"name":"scone","price": 6,"quantity": 206}])

top10bakery.welcome_message()
top10bakery.sell_items("donuts")
print(top10bakery)
print(top10bakery.item)
print(top10bakery.item[0])
print(top10bakery.item[0]["quantity"])