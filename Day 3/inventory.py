"""
AUTHOR: Mary Grizelle Hamor
DESCRIPTION: This program simulates an inventory management system of shoes. It can add, update and delete items in the record. 
"""

class Inventory:
    def __init__(self):
        self.record = []

    def add_shoes(self, shoes):
        self.record.append([shoes.stock_number, shoes.color, shoes.size])

    def show_shoes(self, shoes):
        print(f"\nStock #\t\tColor\t\tSize")
        for item in self.record:
            for feature in item:
                if item[-1] == feature:
                    print(feature)
                    break
                print(feature, end="\t\t")

    def update_shoes(self, number, feature, new_data):
        self.record[number][feature] = new_data

    def del_shoes(self, number):
        self.record.remove(self.record[number])

class Shoes:
    def __init__(self, stock_number, color, size):
        self.stock_number = stock_number
        self.color = color
        self.size = size

if __name__ == "__main__":
    inventory = Inventory()

    # Initial stock
    colors = ["red", "white", "yellow", "pink", "black"]
    sizes = [14, 15, 16, 17, 18]

    for i, color, size in zip(range(5), colors, sizes):
        shoes = Shoes(i, color, size)
        Inventory.add_shoes(inventory, shoes)

    while True:
        print("\nI N V E N T O R Y    M A N A G E M E N T")
        Inventory.show_shoes(inventory, shoes)

        print("\n1 : Add item\n" \
            "2 : Update item\n" \
            "3 : Delete\n" \
            "4 : Exit")
        action = input("\nEnter your chosen action: ")

        if action == '1':
            stock_number = int(inventory.record[-1][0]) + 1
            color = input("Enter shoe color: ")
            size = input("Enter shoe size: ")

            shoes = Shoes(stock_number, color, size)
            Inventory.add_shoes(inventory, shoes)

        elif action == '2':
            number = int(input("Enter stock # to be updated: "))

            existing = []
            for item in inventory.record:
                count = 1
                for feature in item:
                    if count == 1:
                        existing.append(feature)
                    count += 1

            if number in existing:
                print("\nWhat would you like to update?\n" \
                    "1 : Color\n" \
                    "2 : Size")
                update = int(input("Chosen feature: "))
                new_data = input("Enter updated value: ")

                if update == 1 or update == 2:
                    Inventory.update_shoes(inventory, number, update, new_data)
                else:
                    print("\nWARNING: Invalid feature.")    
            else:
                print("\nWARNING: The item does not exist.")

        elif action == '3':
            number = int(input("Enter stock # to be deleted: "))

            existing = []
            for item in inventory.record:
                count = 1
                for feature in item:
                    if count == 1:
                        existing.append(feature)
                    count += 1
            
            if number in existing:
                Inventory.del_shoes(inventory, number)
            else: 
                print("\nWARNING: The item does not exist.")

        elif action == '4':
            exit(0)

        else: 
            print("\nWARNING: Invalid action.")