class card:
    data={}
   
        
    def add(self):
        print("for ending adding press 'end'")
        while True:
            key=input("enter item name:")
            if key=="end":
                break
            value=int(input("enter quantity:"))
            self.data[key]=value
        print(self.data)
    def remove(self):
        item=input("enter remove item form card:")
        del self.data[item]
    def count(self):
        c=0
        l=list(self.data.values())
        for i in l:
            c+=i
        print("all items are :",c)
obj=card()
obj.add()
obj.remove()
obj.count()
        
        
