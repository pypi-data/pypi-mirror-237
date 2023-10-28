import inspect
import sys
from functools import wraps,partial,update_wrapper

import numpy as np

prefix = ""
module_prefix = ""
suffix = ""


def regular_wrapper(func):
    @wraps(func)
    def inner(*args,**kwargs):
        print('hi')
        return func(*args,**kwargs)
        
    return inner

def value_from_namespace(namespace,key):
    value = getattr(namespace,key,None)
    if value is None:
        try:
            value = namespace[key]
        except:
            value = None
    return value

def to_list(obj):
    if not hasattr(obj,"__iter__"):
        return [obj]
    return obj

def default_args(
    namespace=None,
    prefix = None,
    module_prefix = None,
    suffix = None,
    debug_params_to_set = False,
    debug_dict_assignment = False,
    ):
    curr_module = module_calling_func(levels_up=2)
    
    if module_prefix is None:
        module_prefix = dcu.module_prefix
        
    if suffix is None:
        suffix = dcu.suffix
    
    if namespace is None:
        namespace = curr_module
        if prefix is None:
            prefix = module_prefix
            
    if prefix is None:
        prefix = dcu.prefix

    
    def wrapper_func(func):
        param_values = fu.parameters_and_defaults_from_func(
            func
        )
        
        param_names = list(param_values.keys())
        param_to_update = [
            k for k,v in param_values.items()
            if v is None 
            and value_from_namespace(namespace,f"{prefix}{k}{suffix}") is not None
        ]
        
        
        # just for debugging purposes
        if debug_params_to_set:
            param_to_update = []
            for k,v in param_values.items():
                if debug_params_to_set:
                    curr_name = f"{prefix}{k}{suffix}"

                value = value_from_namespace(namespace,curr_name)
                    
                if debug_params_to_set:
                    print(f"curr_name= {curr_name}, value = {value}")
                    print(f"v = {v}")
                if v is None and value is not None:
                    param_to_update.append(k)
                    
            if debug_params_to_set:
                print(f"After checking, param_to_update = {param_to_update}")

        @wraps(func)
        def inner(*args,**kwargs):
            default_dict = {k:value_from_namespace(namespace,f"{prefix}{k}{suffix}")
                            for k in param_to_update}
            
            if debug_dict_assignment:
                print(f"default_dict = {default_dict}")
                
            args_dict = {k:v for k,v in zip(param_names,args)}
            default_dict.update(args_dict)
            default_dict.update(kwargs)
    
            
            if debug_dict_assignment:
                print(f"args_dict = {args_dict}")
                print(f"kwargs = {kwargs}")
                print(f"default_dict = {default_dict}")
            
            return func(**default_dict)
        return inner
    
    return wrapper_func

from functools import update_wrapper

def attribute_dict_from_function_obj_overlap(
    func,
    obj,
    verbose = False,
    debug = False,):
    """
    Purpose: Find an attribute dictionary from an object
    that matches parameters of a function
    """
    param_values = fu.parameters_and_defaults_from_func(
            func
    )

    attribute_dict = dict()
    for k in param_values.keys():
        if debug:
            print(f"working on {k}")
        try:
            value = getattr(obj,k)
            if debug:
                print(f"value = {value}")
        except:
            continue
        else:
            attribute_dict[k] = value
        
    if verbose:
        print(f"attribute_dict = {attribute_dict}")

    return attribute_dict


def example_attribute_dict_from_function_obj_overlap():  
    class Person():
        name = "Brenadn"
        address = "17229"
    
    def example_func(
        name,
        height = "510",
        #address = "12345"
        ):
        return name
    
    p = Person()
    
    attribute_dict_from_function_obj_overlap(
        example_func,
        p,
        verbose = True,
        debug = True
    )   
    
class FuncWrapper:
    def __init__(self,function_list,function_wrapper,function_args=None,name = None):
        self.function_list = to_list(function_list)
        self.function_wrapper = function_wrapper
        if function_args is None:
            function_args = {}
        self.function_args = function_args
        self.name = None
        
def adding_self_to_function(f):
    @wraps(f)
    def new_func(self,*args,**kwargs):
        return f(*args,**kwargs)
    return new_func

def unpacking_obj_to_function(f):
    @wraps(f)
    def new_func(self,*args,**kwargs):
        attr_dict = attribute_dict_from_function_obj_overlap(
            f,self
        )
        
        kwargs.update(attr_dict)
        return f(*args,**kwargs)
    return new_func

def send_obj_to_function(f,obj_name=None):
    debug = False
    @wraps(f)
    def new_func(self,*args,**kwargs):
        if debug:
            print(f"obj_name = {obj_name}")
        
        param_names = fu.parameter_names_from_func(f)
        
        args_idx = np.arange(len(args)).astype('int')
        first_arg = fu.first_parameter_name(
                f
        )
    
        shift_args = 0
        args_new = []
        if obj_name is None:
            shift_args = 1
            args_new = [self]
            if debug:
                print(f"adding obj name to args")
        else:
            if obj_name == first_arg:
                shift_args = 1
                
            kwargs[obj_name] = self
            if debug:
                print(f"adding obj to kwargs")
            
        #updating with the other arguments
        args_dict = {param_names[idx + shift_args]:val for
                     idx,val in zip(args_idx,args)}
        kwargs.update(args_dict)
        
        if debug:
            print(f"kwargs = {kwargs}")
            print(f"args_new = {args_new}")
        return f(*args_new, **kwargs)
    
    return new_func

def static_function(f):
    return update_wrapper(staticmethod(f),f)
        
def add_func(
    func_to_add = None,
    func_to_add_unpacked = None,
    func_to_add_obj=None,
    obj_name = None,
    func_to_add_static = None,):
    """
    Things to do:
    1) preserve the docstring of the function
    2) unpack the object attributes that match the
    parameters of function and send them 
    """
    
            
    wrapper_objs = [
        FuncWrapper(func_to_add,adding_self_to_function),
        FuncWrapper(func_to_add_unpacked,unpacking_obj_to_function),
        FuncWrapper(func_to_add_obj,send_obj_to_function,
                    function_args = dict(obj_name = obj_name)),
        FuncWrapper(func_to_add_static,static_function),
    ]
    
    def class_wrapper(cls):
        @wraps(cls,updated=())
        class NewClass(cls):
            pass
        
        # adding functions that accepts self but not unpack
        for wrap_obj in wrapper_objs:
            for f in wrap_obj.function_list:
                if f is None:
                    continue
                
                #print(f"Trying to add func {wrap_obj}")
                if not hasattr(NewClass,f.__name__):
                    setattr(NewClass,f.__name__,wrap_obj.function_wrapper(f,**wrap_obj.function_args))

        return NewClass
    return class_wrapper


import test
def inspect_test():
    return test.inspect_test()

def module_calling_func(
    levels_up = 1,
    verbose = False):
    stack = inspect.stack()
    frm = stack[levels_up]
    mod = inspect.getmodule(frm[0])
    if verbose:
        print(f"module (after levels_up = {levels_up} = {mod}")
    return mod

    
from . import function_utils as fu
from . import decorators as dcu