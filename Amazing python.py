#!/usr/bin/env python
# coding: utf-8

# ### Python was invented by Guido van Rossum in 1991 from Dutch
# # some of the. application of python are netfilx , facebook tagging, and alexa
# ### Different domain catered by python are
# - web development , testing, web scraping,data analysis , computer graphis,machine learing,big data, IOT
# ## google ,nasa,firefox,rasberry pi
# ## Pythons is not that complex
# - it is a high level programming language
# - its very easy to read and understand
# - python has the high spike since last five years comparing to other programming Languages.

# ## Secret module
# - it generates secure random numbers for managing secretes
# - secretes.randbelow(n) - it returns a random int in the range[0,n)
# - secrets.randbits(k)- it returns an int with k random bits
# - secrets.choice(sequence) - returns a randomly chosen element from a non-empty sequence
# - byte token - secrets.token_bytes([n]) return a random yte string contining nbytes numbers of bytes. if n is none or not supplied, a defult is used
# - hex token - serete.token_hex([n]) - it returns a random text string, in hexadecimal, the string has n random bytesconverted to two hexbytes
# - safe_urls - return a random URL_safe text string,containig n random bytes , the text is base 64 encoded                                                              

# ### what is the diff betwwn random and secure number means?
# - the secret module provides access to most secure sourse of randomness that your os provides, in perticularly secrets should be used in preference to
# - the defult pseudo-random, number generte in the random module , which is designed for modelling and stimulation,not security or cryptograpy

# ### enumarte -
# - add indices to the elements of a list

# In[1]:


data= [
'alpha','beta','gama'
]
data_with_indices=list(enumerate(data))


# In[2]:


print(data_with_indices)


# ### convert the strng to integers in one go

# In[3]:


data="10,20,30"
strings= data.split(',')
print(strings)
### we have strings so far


# In[4]:


## we want integres 
num=list(map(int,data.split(',')))
## coversion takes place here
print(num)


# ### list all the factors of a given number

# In[5]:


n=123
for x in range(1,n):
    if n%x==0:
        print(x)


# n=156
# for x in range(1,n):
#     if n % x==0:
#         print(x)

# In[6]:


### Install package of emoji


# In[7]:


pip install emoji


# In[8]:


### Emoji module
from emoji import emojize


# In[9]:


print(emojize(':bus::house:'))
print(emojize(':phone:',use_aliases=True))


# ### Rounding numbers with .5 fractions
# - it will round to the nearest even number

# In[10]:


print(round(0.5))
print(round(1.5))
print(round(2.5))
print(round(3.5))
print(round(4.5))


# ### input vs. row input
# - difference in the return type of input()
# 

# In[11]:


item=input("enter something:")
print(type(item))


# In[12]:


### integer division in python 2 and 3
a=10
b=3
c=a/b
d=a//b
print(c)
print(d)


# In[13]:


# in python 3 print is a function we need to have brackets


# In[14]:


print 'hello world'


# In[ ]:


print('hello world')


# In[ ]:


# to print the pattern below
n=int(input("enter the num of lines"))
for i in range(1,n+1):
    print('* '*i)
for j in range(n-1,0,-1):
    print('* '*j)


# In[ ]:


## There is a poem written in python by TimPeters we can read it by just importing this


# In[ ]:


import this


# In[ ]:


### we can return multiple values in python


# In[ ]:


# Multiple Return Values in Python! 
def func(): 
   return 1, 2, 3, 4, 5
  
one, two, three, four, five = func() 
  
print(one, two, three, four, five) 


# #### In Python, everything is done by reference. It doesn’t support pointers

# ### What are Pointers?
# - Pointers are variables which store the address of other variables.

# ### python tips and trics 

# In[19]:



### adding two lits in python
a=[1,2,3,4,5]
b=[4,5,6,7,8]
c=a+b
c


# In[20]:


## calender
import calendar
print(calendar.month(2020,4))


# In[25]:


print(calendar.day_name)


# In[26]:


##swap
a=10
b=20
a,b=b,a
print(a)


# In[28]:


## List
a='hello world'
b=list(a)
print(a)


# In[29]:


### JOin
msg=['well','done']
msg


# In[31]:


msg1="".join(msg)


# In[32]:


msg1


# In[33]:


### time module


# In[37]:


import datetime
date=datetime.datetime.now()
date=date.strftime("%d-%m-%y %I:%M:%S %p")


# In[35]:


date


# In[50]:


### RAndom
import random
a=1,2,3,4,5,6,7,8,9,3,4,5,5,6,78,899,87,3,3,3
a=random.choice(a)


# In[51]:


a


# In[57]:


b='abcdefghijklmnopqrstuvwxyz'
random.choice(b)


# In[61]:


random.choice(b)


# In[63]:


random.choice(b)


# ### Extend in python
# - Add the elements of a list(or any iterable), to the current list

# In[66]:


f=['apple','banana','orange']
cars=['ford','bmw','volvo']
f.extend(cars)
print(f)


# In[67]:


## programm
n=int(input('enter the num:'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print("")


# In[69]:


print ("hello",end=" ") 


# In[70]:


tuple=(1,2,3,4)
tuple.append((5,6,7))
print(len(my_tuple))


# In[71]:


l=list('123456')
l[0]=l[5]=0
l[3]=l[-2]
print(l)


# In[ ]:




