#Python Program to check if given number is harshad number (number which is divisible by sum of its digits)
num = 156;    
rem = sum = 0;     
n = num;       
while(num > 0):    
    rem = num%10;    
    sum = sum + rem;    
    num = num//10;     
if(n%sum == 0):    
    print(str(n) + " is a harshad number");    
else:    
    print(str(n) + " is not a harshad number");  
