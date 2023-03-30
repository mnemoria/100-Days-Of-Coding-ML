class Bag:
    bag_list = []

    def __init__(self, name: str, price: float, quantity=0):
        # Validate received arguments
        assert price >= 0, f"Price {price} cannot be negative"
        assert quantity >= 0, f"Quantity {quantity} cannot be negative"

        # Assign to instance variables
        self.__name = name
        self.price = price
        self.quantity = quantity

        Bag.bag_list.append(self)

    @property # similar to a getter
    # Property Decorator = Read-Only Attribute
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long")
        else:
            self.__name = value

class Knapsack(Bag):
    def __init__(self, name:str, price:float, quantity=0, pocket=0):
        # Call super() to access parent class attribute
        super().__init__(
            name, price, quantity
        )

        assert pocket >= 0, f"Pocket {pocket} cannot be negative"
        self.pocket = pocket