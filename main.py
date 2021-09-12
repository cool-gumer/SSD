#!/usr/bin/env python
# coding: utf-8

# In[10]:


import task1,task2,task3,task4

from task1 import decorator_1
from task2 import decorator_2
from task3 import Decorator_3 , Rank
from task4 import Decorator_4
import random
import math


#TASK1 for example 
@decorator_1
def quadratic_equation(a,b,c):
    D = b*b - 4*a*c
    if a==0 :
        if b!=0: 
            print(-c/b)
        else: 
            print("No roots")
    else:
        if D>0:
            print("x_1 = ", (-b+math.sqrt(D))/(2*a), "x_2 = ",(-b-math.sqrt(D))/(2*a))
        elif D==0: print("x = ",-b/(2*a))
        else:
            print("No solutions")
#using lambda first
@decorator_1
def func():
    print("I am ready to Start")
    result = 0
    n =  random.randint(10,751)
    prod = lambda x : x*x
    for i in range(n):
        result += prod(i)
        
        

@decorator_1
def funx(n=2, m=5):
    print("I am ready to do serious stuff")
    max_val = float('-inf')
    
    n =  random.randint(10,751)
    res = [pow(i,2) for i in range(n)]
    for i in res:
        if i > max_val: 
            max_val = i


# TASK 2  using lambda second
@decorator_2
def find_div(bar1, bar2=""):
    """
    This function does something useful 
    :param bar1: description
    :param bar2: description
    """ 
    #
    lll=  list(filter(lambda x: x%bar1==0, bar2))
    print ("dividers", lll)
    print("some\nmultiline\noutput")
    
    
#TASK 3
@Decorator_3
def func1():
    print("I am ready to Start")
    result = 0
    n =  random.randint(10,751)
    for i in range(n):
        result += (i**2)
        
@Decorator_3
def func2(n=2, m=5):
    print("I am ready to do serious stuff")
    max_val = float('-inf')
    n =  random.randint(10,751)
    res = [pow(i,2) for i in range(n)]
    for i in res:
        if i > max_val: 
            max_val = i      
@Decorator_3
def func3(a,b):
    print(a," ?= ",b , a==b)
    
@Decorator_3
def func4(a):
    fact=1
    for i in range (1,a):
        fact=fact*i
    print(fact)
    
#TASK 4 
@Decorator_4 
def pascal_triangle(n):
    
    def next_string(a):
    
        b = [0]

        for i in range(len(a)-1):
            b.append(a[i]+a[i+1])
        b.append(0)

        return(b)

    a = [0,1,0]

    for i  in range(n):

        print(a[1:len(a)-1])
        a = next_string(a)    
    
if __name__ == "__main__":
    quadratic_equation(1,4,5)
    find_div(2,[1,3,4,7,10])
    func1()
    func2()
    func3(4,5)
    func4(10)
    Rank()
    
    pascal_triangle(5)
#now create some mistake ()
    pascal_triangle(5,3,1)


# In[ ]:





# In[ ]:




