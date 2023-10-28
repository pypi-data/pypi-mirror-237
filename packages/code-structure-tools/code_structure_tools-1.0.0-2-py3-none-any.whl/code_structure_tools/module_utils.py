def all_callable_in_module(
    mod,
    return_str = False,
    verbose = False,):
    
    func_str = "<function"
    
    callable_funcs = []
    for k in dir(mod):
        if "_" == k[:1]:
            continue
        attr = getattr(mod,k)
        if callable(attr) and str(attr)[:len(func_str)] == func_str:
            if return_str:
                callable_funcs.append(k)
            else:
                callable_funcs.append(attr)
    if verbose:
        print(f"# of callable = {len(callable_funcs)}")
        
    return callable_funcs

functions_in_module = all_callable_in_module

from . import module_utils as modu
                
            
            
    
    