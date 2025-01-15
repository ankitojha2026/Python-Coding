 # if the positiove number div by sum of its digits then it is called harshad number
def sum_of_digits(n):
    ans=0
    while n>0:
        ans=ans+n%10
        n//=10
    return ans
n=int(input("enter number"))
print("yes" if n%sum_of_digits(n)==0 else "no")
