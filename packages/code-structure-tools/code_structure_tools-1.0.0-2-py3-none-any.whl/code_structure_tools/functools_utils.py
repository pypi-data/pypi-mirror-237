"""
Purpose: to help explain methods available in functools
and provide useful wrappers

Useful things: 
1) cache results (for functions and methods)
2) automatic/dynam default args, partial (for functions and methods)
3) overload by arg type (functions and methods)
4) transfer function/class metadata when pass through wrapper


Methods: 

1) @cached_property: can add as a decorator to class methods
so that the computed property will instead be cached and not recomputed

2) cmp_to_key():
Will turn a comparison function (2 args, returns -1,0,1 based on which is greater) into a key function (takes one arg and returns another alue to be used as sort key)
- used mainly for transitioning from python 2 to python 3

3) @lru_cache(maxsize = 128) (least recently used cache)
Purpose: to store the results of a set of arguments to a function so that the argument doesn't have to be rerun
- parameter maxsize sets the number of possibilities will store (if exceeds then will drop the least recently used one)
- can print out function.cache_info to find stats on how often reused
    misses: number of times called and result not already stored
    hits: number of times already stored
    curr_size: the total number of values stored

4) @total_ordering: class wrapper 
Purpose: to reduce # of lines of code for implementing comparisons
Motivation: want to use all the <, =<, > , == syntax magic but don't want to implement all __lt__, __le__, __gt__ functions
HOw to implement: add as decorator above class that has one of the __lt__ functions implemented as well as __eq__, and the decorator will add the rest


Downside: 
- code will be a little bti slower
- The error stack trace will be harder

5) partial: function returning another function
Purpose: Allows to reduce the signature of a function by dynamically assigning new default argument values

Downside: 
- docstring not automatically copied over
- if partial is specified without a keyword, then can't
overload that one with a keyword call

6) partialmethod:
Purpose: same thing as partial but for class methods
How to implement: assign output like class variable

Downside: 
Doesn't copy over docstring as well

7) reduce: to reduce an iterable into a single number
Purpose: In order to change a list into a single number

Why? Could programmatically switch out the operator that 
    did the reducing to get different functionality
    
8) @singledispatch: For overloading functions based on first argument type
Purpose: May want different functionality based on a type difference in the first argument (and not want to implement this with an if statement and different subfunctions)

How to implement: 
- decorate the function want to overload with @signledispatch
- create new functions decorated with 

    @func_name.register
    _(var: type_hint):
        pass
    
    @func_name.register
    _(var: diff_type):
        pass  
    
9) @singledispatchmethod:
Purpose does same thing but for methods of a class

10) update_wrapper: keep metadata the same
PUrpose: when you decorate a function, the docstring and name
is not copied over

Solution: use this function as a wrapper to handle that for you

11) @wraps(func_wrapped) : convinience for update_wrapper func

"""

from functools import lru_cache

@lru_cache
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

def lru_cache_example():
    list_of_fib_numbers = [fib(n) for n in range(16)]
    print(list_of_fib_numbers)
    pirnt(fib.cache_info())
    
    
from functools import total_ordering
def total_ordering_example():
    
    @total_ordering
    class Pythonista:
        firstname: str
        lastname: str
        
        def __eq__(self, other:obj) -> bool:
            return False
        
        def __lt__(self,other:obj) -> bool:
            return True
        
from functools import partial

def euclid_dist(point1,point2):
    """function that computes euclidean distance
    """
    x1,y1 = point1
    x2,y2 = point2
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

import math
def partial_example():
    new_func = partial(euclid_dist,(0,0))
    return new_func

def partial_error_example_because_kwarg_conflict():
    from functools import partial

    def my_func(a=10,b=20,c=30):
        return a*b*c

    new_func = partial(my_func,3,c = 3)
    new_func(a = 3)
    
from functools import partialmethod


def partialmethod_example():
    class Cell(object):
        def __init__(self):
            self._alive = False
            
        @property
        def alive(self):
            return self._alive
        
        def set_state(self,state):
            """
            for setting alive status
            """
            self._alive = bool(state)
            
        set_alive = partialmethod(set_state,True)
        set_dead = partialmethod(set_state, False)
        
    c = Cell()
    c.set_alive()
    print(c.alive)
    return c


from functools import reduce
from operator import add,mul
def reduce_example():
    """
    
    """
    my_list = [1,2,3,4,5]
    
    print(reduce(add,my_list))
    print(reduce(mul,my_list))
    
    
from functools import singledispatch,singledispatchmethod

def singledispatch_example():
    @singledispatch
    def mul(a,b):
        if type(a) is not type(b):
            return Exception
        else: 
            return a*b
        
    @mul.register
    def _(a: str, b:str):
        return a + b
    
    print(mul(1,2))
    print(mul("hi","hello"))
    
    
    # -- for classes 
    class Negator:
        @singledispatchmethod
        def neg(self,arg):
            raise Exception("")
        
        @neg.register
        def _(self,arg:int):
            return -arg
        
        @neg.register
        def _(self,arg:bool):
            return not arg
        
        
    obj = Negator()
    print(obj.neg(5))
    print(obj.neg(True))
    
    
    
from functools import wraps

def wraps_example():
    """
    Showing how you can preserve metadata from the function
    that is decorated
    """
    def show_args_without_wrap(f):
        def new_func(*args,**kwargs):
            print(f"args = {args},kwargs = {kwargs}")
            return f(*args,**kwargs)
        
        return new_func
    
    def show_args(f):
        @wraps(f)
        def new_func(*args,**kwargs):
            print(f"args = {args},kwargs = {kwargs}")
            return f(*args,**kwargs)
        
        return new_func
    
    @show_args_without_wrap
    def mult_values_without_wrap(a,b):
        """values are multiplied
        """
        return a*b
    
    print(mult_values_without_wrap.__name__)
    print(mult_values_without_wrap.__doc__)
    
    @show_args
    def mult_values(a,b):
        """values are multiplied
        """
        return a*b
    
    print(mult_values.__name__)
    print(mult_values.__doc__)
    
    
def using_update_wrapper_with_partial():
    from functools import partial,update_wrapper

    def mult_values(a,b):
        """values are multiplied
        """
        return a*b


    mult_basic = partial(mult_values,20)
    print(mult_basic.__doc__)
    
    mult_single = update_wrapper(
        partial(mult_values,10),
        mult_values)
    
    print(mult_single.__doc__)