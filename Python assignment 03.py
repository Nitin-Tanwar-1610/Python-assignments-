#!/usr/bin/env python
# coding: utf-8

# In[7]:


## Write a Python Program to Check if a Number is Positive, Negative or Zero?

a = int(input("Enter a number: "))
if a<0:
    print("Provided number is a negative number.")
elif a>0:
    print("Provided number is a positive number.")
else:
    print("Provided number is equal to zero.")


# In[8]:


## Write a Python Program to Check if a Number is Odd or Even?

a = int(input("Enter a number: "))
if a%2 == 0:
    print("Provided number is an even number.")
else:
    print("Provided number is an odd number.")
    


# In[5]:


## Write a Python Program to Check Leap Year?

year = int(input("Enter a year: "))
if (year%400 == 0) and (year%100 == 0):
    print("{0} is a leap year".format(year))
elif (year%4 == 0) and (year%100 != 0):
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))
    


# In[17]:


## Write a Python Program to Check Prime Number?

n = int(input("Enter a number: "))
for i in range(2,n):
    if n % i == 0:
        print("Provided number is not a prime number.")
        break
else:
    print("Provided number is a prime number.")


# In[22]:


## Write a Python Program to Print all Prime Numbers in an Interval of 50-100?

list = []
for x in range(50,101):
    for i in range(2,x):
        if x%i == 0:
            break
    else:
        list.append(x)
print(list)

