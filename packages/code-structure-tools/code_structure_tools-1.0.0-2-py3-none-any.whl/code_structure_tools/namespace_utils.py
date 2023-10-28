"""
Purpose: To help understand namespaces in python
and how they relate to objects

Tutorial link: https://realpython.com/python-namespaces-scope/#:~:text=the%20next%20level.-,Namespaces%20in%20Python,values%20are%20the%20objects%20themselves.


python implements namespaces as like a dictionary
--> looks up the variable name you typed as a key in the dictoinary

global refers to the enclosure of the python file or 
--> can access the dictionary with globals()
--> can directly edit this dictionary and it changes namespace

to reference the immediate enclosure namespace dict
locals()
--> cannot directly edit this dictionary (because it is a copy), changes to dictionary will not be refelcted in local namespace


keywords:
global: reference or creates a variable in the global (py file) enclosing namespace
nonlocal: references a variable in the nearest enclosing namespace [will error if there is not a variable upstream in namespace that it can bind to]



To print the namespace of __main__ just do
    print(dir())
"""

def print_builtin_namepsace():
    """
    __builtins__ will be a dictionary inside this module,
    but if did this in main ipynb __builtins__ would be a module
    """
    return dir(__builtins__)


def order_of_namespaces_checked():
    print(f"local flat one, things defined in same enclosure")
    print(f"namespace of one enclosure above (even spatially below")
    print(f"namespace of one enclosure above (even spatially below)")
    print(f"...")
    print(f"namespace of the py file (or interactive seesion)")
    print(f"built in namespace")
    
def examample_order_of_namespace_resolution():
    #  will NOT issue an error
    def another_func():
        print("another one")

    def my_func():
        x = 10

        def print_var():
            def deeper_func():
                print(x)
                print(y)
                another_func()

            deeper_func()
        y = 40
        print_var()
        #deeper_func()
        return x

    my_func()


def print_global_variables():
    print(globals().keys())
    
def print_locals_variables():
    zz = 10
    def f(x, y):
        s = 'foo'
        print(locals())
        
    f(10,30)
    
    
y = 10

def modify_global():
    global y # tells y should refer to global namespace
    y = 40
    
def not_modify_global():
    y = 50
    
    
modify_global()
not_modify_global()
print(y) #should print 40


# --- example of can add to global namespace
def adding_name_to_global_namespace():
    global new_var
    new_var = 100000
    
adding_name_to_global_namespace()
    
print(F"new_var = {new_var}")


# non-local example
def non_local_keyword_example():
    def f():
        x = 5000

        def g():
            nonlocal x
            x = -1

        g()
        print(x)


    f()