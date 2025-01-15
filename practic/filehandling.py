num=int(input("enter digite:"))
i=1;
odd=0
even=0
while num>0:
    temp=num%10
    num//=10
    if i%2==0:
        even+=temp

    else:
        odd+=temp
    i+=1 
print(even ," ",odd)

print("difference b/w even-odd:", odd-even)