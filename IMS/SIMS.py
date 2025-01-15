from prettytable import PrettyTable
class Items:
    def __init__(self , name ,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

#it will be return all items details
    def getItems(self):
        return [self.name,self.price,self.quantity]

# it will be retun the name of the items
    def getName(self):
        return self.name
# it will return the quantity
    def getQuantity(self):
        return self.quantity




class Inventory:
    def __init__(self):
        self.items=[]
    def addIntems(self,name,price,quantity):
        self.items.append(Items(name,price,quantity))
    def update_quantity(self):
        
        name=input("Enter Item Name: ")
        for i in range(len(self.items)):
            if(name==self.items[i].getName()):
                print(self.items[i].getQuantity())
                new_quantity=input("Enter new Quantity:")
                self.items[i].quantity=new_quantity
                print("Updated")
                

    def displayItems(self):
        item= PrettyTable(["Name","price","quantity"])
        for i in range(len(self.items)):
         item.add_row(self.items[i].getItems())
        print(item)


i1=Inventory()
i1.addIntems("pen",12,30)
i1.addIntems("box",200,3000)
i1.addIntems("pencile",10,40)
i1.addIntems("Note-Box",350,680)
i1.addIntems("marker",130,681)
i1.addIntems("c-book",400,100)
i1.addIntems("python-book",600,200)
i1.displayItems()
temp=input("you want to update quantity 'yes' or 'no' ").upper()
if temp=='YES':
    i1.update_quantity()
i1.displayItems()

