#Telephone Directory with functions (Find number given name, Update a number, Save a new number, Delete a number, Display whole telephone directory)

print ("*****TELEPHONE DIRECTORY***")
list1=[]
list2=[]
dict1={}
temp=100
n=int(input("Enter the number of contacts : "))
for i in range(0,n):
    name1=input("Enter your name: ")
    num=int(input("Enter your phone number: "))
    list1.extend([name1])
    list2.extend([num])
    dict1=dict(zip(list1,list2))
print (dict1)		
