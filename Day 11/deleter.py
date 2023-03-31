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

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value

    @name.deleter
    def name(self):
        del self.__name 

if __name__ == "__main__":

    bag1 = Bag("Chanel", 1000.00, 1)
    print(bag1.name)

    del bag1.name
    print(bag1.name)