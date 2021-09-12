#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time 

global dict_ 

def decorator_1(func):
    dict_={}
    def wrapper(*args,**kwargs):
        #nonlocal count
        #count+=1        
        if func.__name__ in  dict_:
            dict_[ func.__name__]+=1
        else:
            dict_[ func.__name__]=1
        start = time.time()
        func(*args)
        end = time.time()
        
        print(func.__name__, "call",  dict_[ func.__name__] , "execution time", end - start)
    return wrapper


# In[ ]:




