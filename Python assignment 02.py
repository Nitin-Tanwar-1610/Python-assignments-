#!/usr/bin/env python
# coding: utf-8

# In[4]:


## Write a Python program to convert kilometers to miles?
Km = int(input("Enter the distance in kilometers: "))
Miles = 0.621371 * Km
print(f"{Km} kilometers is equal to {Miles} miles.")


# In[5]:


## Write a Python program to convert Celcius to Fahrenheit?
celcius = int(input("Enter the temperature in degree celcius: "))
farenheit = (9/5)* celcius + 32
print(f" {celcius} degree celcius is equal to {farenheit} degree farenheit.")


# In[8]:


## Write a Python program to display calendar?
import calendar
yy = int(input("Enter current year: "))
mm = int(input("Enter current month: "))
print(calendar.month(yy, mm))


# In[29]:


## Write a Python program to solve quadratic equation?
import cmath
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
des = (b**2) - (4*a*c)
x1 = (-b + cmath.sqrt(des))/(2*a)
x2 = (-b - cmath.sqrt(des))/(2*a)
print(f" Solutions for given quadratic equation are {x1} and {x2}")


# In[31]:


## Write a python program to swap two variables without using temp variable ?
a = 3
b = 7
a,b = b,a
print(f"a = {a}")
print(f"b = {b}")

