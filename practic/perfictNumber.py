def getPerfect(x):
    sum=1
    for i in range(2,x//2+1):
        if x%i==0: 
            sum+=i
    if sum==x:
        return True
    else:
        return False
n=int(input("enter number..."))
print(getPerfect(n))