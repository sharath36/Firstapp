#!/usr/bin/env python
# coding: utf-8

# Create the below pattern using nested for loop in Python.

# In[11]:


n = int(input("Enter number of Rows: "))
list = []
for i in range(1,n+1):
    list.append("*"*i)
print("\n".join(list))
for i in range(n-1,0,-1):
    print("*"*i)


# Write a Python program to reverse a word after accepting the input from the user.

# In[14]:


word = input("Enter Word: ")
Rev = word[::-1]
Rev


# In[ ]:




