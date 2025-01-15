num = int(input('enter the number'))
digits=[]
#sep digits
while num>0:
    rem=num%10#6,2,3,9,2
    digits.insert(0,rem)
    num=num//10#2932
    #digits = [2,9,3,2,6]
    ans=0
    smallest=min(digits)
    largest=max(digits)
    for next_digit in digits:
        if next_digit is smallest:
            ans=ans*10+largest
        else:
            ans=ans*10+next_digit

print(ans)            
#jdddj
