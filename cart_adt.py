class Cart:
    def __init__(self):
        self._items = []

    def add(self, item):
        self._items.append(item)

    def count(self):
        return len(self._items)

    def is_empty(self):
        return len(self._items) == 0

    def remove(self, item):
        if not self._items:
            print("Cart is empty")
        elif item in self._items:
            self._items.remove(item)
            print("Removed:", item)
        else:
            print("Item not found")


# Test 1: Add two items and check the count
cart = Cart()
cart.add("Milk")
cart.add("Bread")
print(cart.count())

# Test 2: Remove Bread and check the count
cart.remove("Bread")
print(cart.count())

# Test 3: Try to remove a missing item
cart.remove("Eggs")

# Test 4: Try to remove an item from an empty cart
empty_cart = Cart()
empty_cart.remove("Milk")