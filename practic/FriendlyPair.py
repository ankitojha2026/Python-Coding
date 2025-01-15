def getSumOfFactors(n):
    x=0
    for i in range(1,n+1):
        if n%i==0:
            x=x+i
    return x
def getResult(sum,n):
    return (sum-n)//n

n1=int(input("Enter first number:"))
n2=int(input("enter second number :"))
x=getSumOfFactors(n1)
y=getSumOfFactors(n2)
if getResult(x,n1)==getResult(y,n2):
    print("yes")
else:
    print("no")