#!/usr/bin/env python
# coding: utf-8

# In[5]:


## Write a Python program to find sum of elements in list?

list = [2, 4, 7, 9, 12]
a = 0
for i in list:
    a += i
print(f" Sum of all the elements of list is {a}.")


# In[6]:


## Write a Python program to Multiply all numbers in the list?

list = [3, 5, 9, 2, 7]
a = 1
for i in list:
    a = a*i
print(f" Multiplication of all the elements of the list is {a}.")


# In[15]:


## Write a Python program to find smallest number in a list?

list = [9, 6, 12, 5, 23]
a = min(list)
print(f"The smallest value in the list is {a}.")


# In[41]:


## Write a Python program to find smallest number in a list?

list = [9, 6, 12, 5, 23]
list.sort()
print(list)
print(f"The smallest value in the list is {list[0]}.")


# In[16]:


## Write a Python program to find largest number in a list?

list = [19, 26, 62, 85, 43]
a = max(list)
print(f"The greatest value in the list is {a}.")


# In[40]:


## Write a Python program to find largest number in a list?

list = [19, 26, 62, 85, 43]
list.sort()
print(list)
print(f"The greatest value in the list is {list[-1]}.")


# In[38]:


## Write a Python program to find second largest number in a list?

list = [2, 4, 76, 89, 64, 79, 93]
list.sort()
print(list)
print(f"The second largest number in the list is {list[-2]}.")


# In[47]:


## Write a Python program to find nth largest elements from a list?

n = int(input("The value of n = "))
list = [32, 6, 88, 3, 23, 89, 53]
list.sort()
print(list)
print(f"The {n}th largest element in the list is {list[n-1]}.")


# In[51]:


## Write a Python program to print even numbers in a list?

l1 = [23, 42, 56, 79, 75, 98, 29, 12]
l2 = []
for i in l1:
    if i%2 == 0:
        l2.append(i)
    else:
        continue
print(l2)
        


# In[68]:


## Write a Python program to print odd numbers in a List?
l1 = [12, 43, 39, 84, 91, 78]
l2 = []
for i in l1:
    if i%2 != 0:
        l2.append(i)
    else:
        continue
print(l2)


# In[63]:


## Write a Python program to Remove empty List from List?

list = [12, 34, 56, "fan", [], [2, 3, 6], [], 23, [], "ring"]
for i in list:
    if i == []:
        list.remove([])
print(list)


# In[69]:


## Write a Python program to Cloning or Copying a list?

l1 = [2, 4, 5, 8, 9]
l2 = []
for i in l1:
    l2.append(i)
print(f" Original list is {l1}.")
print(f" Cloned list is {l2}.")


# In[80]:


## Write a Python program to Count occurrences of an element in a list?

l1 = [21, 34, 61, 21, 98, 34, 21, 12, 21, 34, 87]
l2 = []
a = int(input("count the occurrence of: "))
for i in l1:
    if i == a:
        l2.append(i)
print(f" The count of occurrence of {a} in list is {l2.count(a)}.")
        

