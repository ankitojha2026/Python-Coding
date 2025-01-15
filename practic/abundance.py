#sum of proper divdider is equal to the other number
def getSumOfFactors(n):
    x=1
    for i in range(2,n//2+1):
        if n%i==0:
            x=x+i
    return x/n


n1=int(input("Enter first number:"))
n2=int(input("enter second number :"))
x=getSumOfFactors(n1)
y=getSumOfFactors(n2)
if x==y:
    print("number is appendence")
else:
    print("no ")