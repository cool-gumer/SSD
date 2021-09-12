import inspect
import time 
from inspect import signature
global dict_ 
import io
from contextlib import redirect_stdout

def decorator_2(fun):
    dict_={}
    def wrapper(*args,**kwargs):
        if fun.__name__ in  dict_:
            dict_[ fun.__name__]+=1
        else:
            dict_[ fun.__name__]=1
        start = time.time()
        fun(*args)
        end = time.time()
        with io.StringIO() as buf, redirect_stdout(buf):
            fun(*args)
            output = buf.getvalue()
        print(fun.__name__, "call",  dict_[ fun.__name__] , "execution time", end - start)
        print("Name:   ",fun.__name__,"\n"
              "Type:   ", type(fun), "\n"
              "Sign:   ", signature(fun),"\n"
              "Args:   ", "positional",  fun.__defaults__, "\n",'key=worded',fun.__kwdefaults__, "\n"
              "Doc:   ",fun.__doc__,"\n"
              "Source:   ","\n",inspect.getsource(fun),"\n"
              "Output:  ",output )
    return wrapper
