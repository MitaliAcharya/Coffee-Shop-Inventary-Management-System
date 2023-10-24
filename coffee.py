class CoffeeShop:
    def __init__(self):
        self.inventory={
            'Arabica':0,
            'Robusta':0,
            'Liberica':0
        }
        self.sales={
            'Arabica':0,
            'Robusta':0,
            'Liberica':0
         }
    def add_inventory(self,coffee_type,amount):
        if coffee_type in self.inventory:
            self.inventory[coffee_type]+=amount
            print(f"{amount}KG of {coffee_type} added to inventory.")
        else:
            print(f"{coffee_type} is not valid coffee type.")
    def update_inventory(self,coffee_type,amount):
        if coffee_type in self.inventory:
            if self.inventory[coffee_type]<amount:
                print("Not enough inventory")
            else:
                self.inventory[coffee_type]-= amount
                print(f"{amount} KG of {coffee_type} sold")
                self.sales[coffee_type]+=amount
        else:
             print(f"{coffee_type} is not a valid coffee type")
    def view_inventory(self):
        print(f"Current inventory:")
        for coffee_type, amount in self.inventory.items():
            print(f"{coffee_type}:{amount}KG")
    def view_sales(self):
        print(f"Sales date:")
        for coffee_type, amount in self.sales.items():
            print(f"{coffee_type}: {amount} KG")
coffee_shop=CoffeeShop()
# add inventory
coffee_shop.add_inventory('Arabica',10)
coffee_shop.add_inventory('Robusta',5)
coffee_shop.add_inventory('Liberica',3)
#update inventory
coffee_shop.update_inventory('Arabica',5)
coffee_shop.update_inventory('Robusta',3)
#view current inventory and sales data
coffee_shop.view_inventory()
coffee_shop.view_sales()
