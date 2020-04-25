#!/usr/bin/env python
# coding: utf-8

# 1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed

# In[12]:


n = []
for x in range(2000,3200):
    if x%7==0 and x%5!=0:
        n.append(x)
print(n)


# Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name.

# In[13]:


x = input("Enter your first name: ")
y = input("Enter your second name: ")
print(y,x)


# Write a Python program to find the volume of a sphere with diameter 12 cm

# In[14]:


D =12
r =D/2
V = 4/3*3.14*r*r
V

