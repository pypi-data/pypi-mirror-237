"""
When overloading the __getattr__ method this could cause infinite recursion when used with copy, deepcopy

Why? Because when deepcopy starts making a new
object it doesn't at first run through the init
-> so if your __getattr__ function relies on 
any attributes set in the init, will try to access them, and then end up calling the __getattr__ function again and cause infinite 
recursion

Solution:

def __getattr__(self,name):
    if name[:2] == "__":
        raise AttributeError(name)
"""


class MyClass:
    """
    Example of how to implement a getattr that allows for
    1) deepcopy
    2) hasattr not to throw error if no attribute
    """
    def __init__(self,x):
        self.x = x
        
    def __getattr__(self,k):
        if name[:2] == "__":
            raise AttributeError(name)
        if int(k) < 10:
            return k
        else:
            return self.__getattribute__(k)
        
obj = MyClass(90)
hasattr(obj,"11")