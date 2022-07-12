#Program to find if a number is Disarium Number


Number=int(input("Enter the number to check Disarium Number = "))
length=len(str(Number))
Temp=Number
Sum=0
rem=0

while Temp>0:
    rem=Temp%10
    Sum=Sum + int(rem**length)
    Temp=Temp // 10
    length=length-1
    
print("The sum of digits = %d" %Sum)
if Sum==Number:
    print("\n%d is a Disarium Number: "%Number)
else:
    print("\n%d is not a Disarium Number: "%Number)
