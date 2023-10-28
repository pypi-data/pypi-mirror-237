
def attributes_in_object(obj,verbose = True):
    object_methods = [method_name for method_name in dir(obj)
                  if not callable(getattr(obj, method_name))
                  and "__" != method_name[:2]]
    return object_methods

def functions_in_object(obj,verbose = True):
    object_methods = [method_name for method_name in dir(obj)
                  if callable(getattr(obj, method_name))
                  and "__" != method_name[:2]]
    return object_methods

from . import object_utils as obju
