'''


-- Transitions for maintaining backwards compatibility

# Automatic Transition from flat class to composition


Option 1: Explicitly define property

Option 2: Using alias object list
def __getattr__(self,item):
    """
    Dynamically updates
    """
    for obj in self.alias_objects:
        if hasattr(obj,item):
            return getattr(obj,item)
    
    raise Exception(f"{item} not found in object or alias_objects {alias_objects}")
    
# Transition from dict/list to an object
def __getitem__(self,item):
    return getattr(self,item)


'''