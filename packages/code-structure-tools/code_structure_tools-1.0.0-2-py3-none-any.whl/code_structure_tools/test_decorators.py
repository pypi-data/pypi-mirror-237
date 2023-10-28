hi = 5
yes = 10
my_list = [5,6,7,8,9,10]
my_dict = {
    "blue":20,
    "green":60
}


parameter_set = dict(
    _message_ = "hi there",
    x = 50,
    y = 80,
    _sleeping_sound = "zzzzzzz",
)


from .decorators import default_args,regular_wrapper

@default_args()
def print_hello(
    name,
    y = None,
    x = None,):
    print(f"name = {name}, yes = {yes}, y = {y}, x = {x}")
    
    print("another one")
    
@default_args(prefix = "_",namespace = parameter_set)
def snore(
    name,
    sleeping_sound = None
    ):

    print(f"{name} is {sleeping_sound}")
    
@default_args(
    prefix = "_",
    suffix = "_",
    namespace = parameter_set
)
def talking(
    name,
    message = None
    ):
    print(f"{name} is saying {message}")
    
    
class Person:
    def __init__(
        self,
        name,
        sleeping_sound = None,
        message = None,
        ):
        
        self.name = name
        self.sleeping_sound = sleeping_sound
        self.message = message
        
        

def get_self():
    return test

import inspect
def inspect_test():
    return inspect.stack()

import decorators
def module_calling_func():
    return decorators.module_calling_func(verbose = True)
        
import test
        

