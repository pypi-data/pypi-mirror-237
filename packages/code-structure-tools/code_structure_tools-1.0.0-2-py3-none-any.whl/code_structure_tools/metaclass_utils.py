"""
A class is just an object, which inside the namespace
has a function (constructor) that can be invoked to create an object that is an instance of that class (aka the namespace is linked and it's functions have special properties)

But ic a class is an object, then constructor makes these objects --> metaclasses

Metaclass is an class object that when constructor is called, the output object is another class object (one with its own constructor)



Examples of metaclass:
type
- thats why when you do type(ClassName) --> gives type
- what are instances of class type
    user-defined classes
    class function (functions defined are instances of this)
    module class (module objects are instances of this)
    
    
Explanation of Metaclasses

https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python


"""

import types

def make_function_without_def_keyword():
    code = compile('print(5)', 'foo.py', 'exec')
    function = types.FunctionType(code, globals())

    function()  # output: 5
    
    
def make_class_without_class_keyword():
    """
    uses the type metaclass
    """
    def echo_bar(self):
       print(self.bar)

    FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar})
    hasattr(Foo, 'echo_bar')
    hasattr(FooChild, 'echo_bar')
    my_foo = FooChild()
    my_foo.echo_bar()
