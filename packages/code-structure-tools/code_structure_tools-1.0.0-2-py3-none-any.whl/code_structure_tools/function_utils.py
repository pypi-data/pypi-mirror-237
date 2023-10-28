import inspect


empty_value = inspect._empty
def is_empty(value):
    return value == empty_value

def parameters_and_defaults_from_func(func):
    """
    To return the name of all the functions and their
    default paramaters
    """
    return_dict = {}
    for param in inspect.signature(func).parameters.values():
        if param.default is param.empty:
            return_dict[param.name] = param.empty
        else:
            return_dict[param.name] = param.default
    return return_dict

def parameter_names_from_func(func):
    return [k.name for k in inspect.signature(func).parameters.values()]


def first_parameter_name(func):
    names = parameter_names_from_func(func)
    if len(names) > 0:
        return names[0]
    else:
        return None

def module_calling_func(
    levels_up = 1,
    verbose = False):
    stack = inspect.stack()
    frm = stack[levels_up]
    mod = inspect.getmodule(frm[0])
    if verbose:
        print(f"module (after levels_up = {levels_up} = {mod}")
    return mod


from . import object_utils as obju
functions_in_object = obju.functions_in_object

from . import module_utils as modu
functions_in_module = modu.functions_in_module

from . import function_utils as fu