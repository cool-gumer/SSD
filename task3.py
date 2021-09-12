#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import random
import inspect
global rank_dic
import io
from contextlib import redirect_stdout
rank_dic={}
class Decorator_3:
    def __init__(self, fun):
        self.fun = fun
        self.arguments = []
        self.count = 0
        self.execution_time = 0
    def __call__(self,*args):
        self.count+=1
        start = time.time()
        self.fun(*args)
        end = time.time()
        rank_dic[self.fun.__name__ ] = end - start
        with io.StringIO() as buf, redirect_stdout(buf):
            self.fun(*args)
            output = buf.getvalue()
        with open(self.fun.__name__+'.txt','w') as f:
            f.write(self.fun.__name__+ " call " + str(self.count) + " execution time " + str(end - start)+ "\n"+
              "Name:   " + self.fun.__name__ + "\n" + 
              "Type:   " + str(type(self.fun)) + "\n" + 
              "Sign:   " + str(inspect.signature(self.fun)) + "\n" +
              "Args:   " +  "positional" + str(self.fun.__defaults__) + "\n" +'key=worded' + str(self.fun.__kwdefaults__) +  "\n"+
              "Doc:   "+str(self.fun.__doc__)+"\n"+
              "Source:   "+"\n"+str(inspect.getsource(self.fun))+"\n"+
              "Output:  "+ output)
            f.close()
            
def Rank():
    sorted_dict = {}
    sorted_keys = sorted(rank_dic, key=rank_dic.get) 
    for w in sorted_keys:
        sorted_dict[w] = rank_dic[w]
    print ("PROGRAM | RANK | TIME ELAPSED")
    temp=1
    for k in sorted_dict.keys():
        print(k,"   ", temp ,"  ",sorted_dict[k])
        temp+=1


# In[ ]:




