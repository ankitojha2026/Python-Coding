def getSumOfFactors(n):
    x=0
    for i in range(1,n+1):
        if n%i==0:
            x=x+i
    return x

def getResult(x,n):
    return (x-n)//n

l=[28,6,12,45,899,65,43,223,65]
ans=[]
for i in range(len(l)):
    for j in range(i+1,len(l)):

        x=getSumOfFactors(l[i])
        y=getSumOfFactors(l[j])
        if getResult(x,l[i])==getResult(y,l[j]):
            ans.append((l[i],l[j]))
for i in ans:
    print(i)
