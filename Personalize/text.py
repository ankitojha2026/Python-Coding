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
tyes,budget=getBudget()
print(type(budget))