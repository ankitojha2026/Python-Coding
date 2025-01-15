name=input("helllo user! pless enter ur name:\n").title()
message=f'hello {name}, welcome to this'
print(message)
'''
take dst input from user
* mountain
*beach

'''
destination=input("where your want to go").strip().lower()
if destination== "mountain":
    print("your have selected mountain")
elif destination=="beach":
    print("you have selected beach")
else:
    print("you have not selected any know destination:")

''' 
tack budget , no . days - input fom the user
if budeget:
>=500 -. luxury
200<= budget <500 ->good
0< budget< 200 -> budget friendly
'''
budget =int(input("enter your budget"))
if budget>= 500:
    print("luxury")
elif budget>= 200:
    print("good")
elif budget >0:
    print("budget friendly")
else:
    print("invild budget")

def toatalCost(budget, days):
    return budget * days
toatalcost=toatalCost(budget,days)

print(f''' days- {days} \n
budget- {budget}\n
total cost-{totalcost}\n
 ''')


