def example_class_inside_class():
    """
    Purpose: If you define a class inside a class, it's just like
    putting that class variable in the persistent namespace of the outer class
    --> but again, that namespace isn't accessible from inside function like in module,
        can only access it through the self
    """
    class Outer:
        class Inner:
            pass

        def __init__(self):
            self.inner_obj = self.Inner()