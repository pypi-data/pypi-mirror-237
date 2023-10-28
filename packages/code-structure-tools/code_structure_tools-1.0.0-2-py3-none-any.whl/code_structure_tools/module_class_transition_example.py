"""
Create a module with functions that 
all will be reused in a class 

Application: To test out the decorators 
that add functions to classes

"""

from .decorators import default_args,add_func
address = "1882 Hidden Glen"
last_name = "Celii"
hourly_rate = 100
hours_per_week = 40


# -- function for just adding self
def print_hi():
    print(f"hi")

# -- functions for unpacking
@default_args()
def print_personal_info(
    first_name,
    last_name=None,
    address=None,
    ):
    
    print(f"{first_name} {last_name} lives at {address}")
    
@default_args()
def calculate_salary(
    hourly_rate=None,
    hours_per_week = None,
    weeks_per_year = 50):
    """
    docstring for calculate salary
    """
    return hourly_rate*hours_per_week*weeks_per_year

# -- function to receive object
def two_person_greeting(person,other_person):
    print(f"Person id {person.count} ({person.first_name}) greets Person id {other_person.count} ({other_person.first_name})")


# --- static functions
def print_greeting(
    name="Bob"
    ):
    print(f"hi {name}")
    
    
# --- function to recieve obj as first parameter
def construct_address(obj,delimiter=", "):
    return f"{obj.street}{delimiter}{obj.city}{delimiter}{obj.state}{delimiter}{obj.zipcode}"


def print_address_dict(add_dict,delimiter=", "):
    print(f"{add_dict['street']}", {add_dict['state']} )

@add_func(
    func_to_add_obj = [construct_address],
)
class Address:
    def __init__(
        self,
        street,
        city=None,
        state=None,
        zipcode=None,):
        
        street = str(street)
        street_split = street.split(", ")
        
        street = street_split[0]
        if city is None and len(street_split) > 1:
            city = street_split[1]
        if state is None and len(street_split) > 2:
            state = street_split[2]
        if zipcode is None and len(street_split) > 3:
            zipcode = street_split[3]
            
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
        
        self.order = ["street","city","state","zipcode"]

    
    @property
    def address(self,):
        return self.construct_address()
        
    @property
    def address_pretty(self):
        return self.construct_address("\n")
    
    def __getitem__(self,item):
        if type(item) is int:
            return_value = getattr(self,self.order[item],None)
        return_value = getattr(self,item,None)
        
        #if return_value is None:
        #    raise Exception("")
        
         
@add_func(
    func_to_add = [print_hi],
    func_to_add_unpacked = [
        print_personal_info,
        calculate_salary,
    ],
    func_to_add_obj = [two_person_greeting],
    obj_name = "person",
    func_to_add_static = [print_greeting]
)
class Person:
    count = 1
    
    @default_args()
    def __init__(
        self,
        first_name,
        last_name = None,
        hourly_rate=None,
        address = None):
        
        self.first_name = first_name
        self.last_name = last_name
        self.hourly_rate = hourly_rate
        
        self.address_obj = Address(address) 
        
        self.alias_objects = [self.address_obj]
        self.count = self.__class__.count
        self.__class__.count += 1
        
    @property
    def address(self):
        return self.address_obj.address
        
    def __getattr__(self,item):
        """
        Dynamically updates
        """
        for obj in self.alias_objects:
            if hasattr(obj,item):
                return getattr(obj,item)
        
        raise Exception(f"{item} not found in object or alias_objects {self.alias_objects}")
    
    def __getitem__(self,item):
        return getattr(self,item)
        
    
            