import math

n = int(input("Number: "))
digits = len(str(n))
temp = n
sum1 = 0
while temp!=0:
    digit = temp%10
    sum1+= (digit**digits)
    temp //=10

if n==sum1:
    print("armstrong")
else:
    print("not armstrong")