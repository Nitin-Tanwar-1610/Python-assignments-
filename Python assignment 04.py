#!/usr/bin/env python
# coding: utf-8

# In[17]:


## Write a Python Program to Find the Factorial of a Number?

num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("sorry, factorial doesn't exist for negative numbers")
elif num==0:
    print("factorial of zero is 1.")
else:
    for i in range(1, num+1):
        factorial = factorial * i
    print(f"Factorial of {num} is {factorial}")


# In[20]:


## Write a Python Program to Display the multiplication Table?

num = int(input("Enter a number: "))
for i in range(1,11):
    print(f"{num} * {i} = {num*i}")
    


# In[24]:


## Write a Python Program to Print the Fibonacci sequence?

n = int(input("Enter the terms: "))
n1,n2 = 0,1
count = 0
if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print(f" Fabonacci sequence upto {n} is:")
    print(n1)
else:
    print("Fabonacci sequence:")
    while count < n:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count +=1 
        


# In[5]:


## Write a Python Program to Find the Sum of Natural Numbers?

num = int(input("Enter the number of terms: "))
sum = (num*(num+1))/2
print(f" Sum of first {num} natural numbers is {sum} ")

