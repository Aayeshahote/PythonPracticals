#Python program to check if a number is happy number


def is_Happy_num(n):
  past=set()
  while n!=1:
        n=sum(int(i)**2 for i in str(n))
        if n in past:
            return False
        past.add(n)
  return True   
print(is_Happy_num(32))
print(is_Happy_num(3))
print(is_Happy_num(28))