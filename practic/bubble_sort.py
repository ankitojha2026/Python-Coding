l=[1,2,3,4,2,1,5,6,7,4]
for i in range(0,len(l)-1):
    for j in range(0,len(l)-i-1):
        if l[j]>l[j+1]:
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp
print(l)