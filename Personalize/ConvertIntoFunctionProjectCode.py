#this print all about the totalcost and buduget..
def printSummary(destination,budget,days,totalCost,types,name):
    print(f'''
     ______________________________________________    
    | Hello {name} ,                              
    | Welcome To This Personalize Adventure Guide  |
    | _____________________________________________|
    | Your Destination   |  {destination          }           
    |____________________|_________________________|
    | Your Budget        |  {types               }     
    |____________________|_________________________|
    | No. Of Days        |  {days               }                 
    |____________________|_________________________|
    | TotalCost          |  {totalCost           }             
    |____________________|_________________________|
    

''')

#this function return the totalcost After calculating:
def getTotalCost(budget,days):
     return budget*days


#this function return the vilid days
def getDays():
     while True:
        try:
            days=int(input("For How Many Days Do You Want To Go ? Enter here:\n"))
            if days>0 and days<100:
                 return days
            else:
                 print("Invilid Days")
        except ValueError:
                print("Invild Days")
 
# this function return the vilid destination Beach or mountain
def getRightDst():
    while True:
        dst=input("Where You Want To Go ? Enter Here: \n").strip().lower()
        if dst=="beach":
            return dst
        elif dst=="mountain":
            return dst
        else:
            print('Sorry!!! you have not selected any know destination .. Re-Enter Again :')

# this function return the vilid budget 
def getBudget():
    while True:
        try:
            budget=int(input("Enter Your Daily Budget : \n"))
            if budget>= 500:
                    return ("luxury",budget)
            elif budget>= 200:
                    return ("good",budget)
            elif budget >0:
                    return ("budget friendly",budget)
            else:
                    print(" Sorry!!! Inviled Budget Enter Again:")
            
        except ValueError:
            print("Sorry!!! Inviled Budget Enter Again: ")



name=input(("Hello User ! Please Enter Your Good Name :\n")).title()
message=f'Hello {name} , Welcome To This Personalize Adventure Guide :\n'
print(message)

''' 
Take Destination form the user :
-> Mountain
-> Beach

destination= getRightDst(dst)
'''

destination=getRightDst().title()
#print(f'You Have Selected {destination} \n')

'''
Take budget 
If Budget:
    >=500                ->luxury
    200<= budget <500    -> good
    0< budget< 200       ->budget friendly
budget= getBudget()

'''
types,budget=getBudget()
#print(f"You Have Selected {types} Budget: \n")

'''
Take number of days 
form 1 day to 99 day under:

days=getDays()

'''
days=getDays()

'''
calculate the total cast for ...
totalCost=budget*days

totalCost=getTotalCost(budget,days)

'''

totalCost=getTotalCost(budget=budget,days=days)
'''


print the summary all about related to totalcost

printSummary(destination,budget,days)

'''
printSummary(destination=destination,budget=budget,days=days,totalCost=totalCost,types=types,name=name)
