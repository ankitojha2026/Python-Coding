num = int(input('enter the number'))
digit=[]
#sep digits
while num>0:
    rem=num%10#6,2,3,9,2
    digit.insert(0,rem)
    num=num//10#2932
    #digits = [2,9,3,2,6]
    ans=0
    for i in range(len(digit)):
        if digit[i]%2==0:
             digit[i]=0
        else:
            digit[i]=1
    for next_dig in digit:
        ans=ans*10+next_dig


print(ans)            
