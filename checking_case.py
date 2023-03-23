

def check_module(a,b):
    if a == b:
        return 1
    else:
        return 0 

def check_purpose(b):
    if b == "Project":
        return 1
    elif b == "Spare Part":
        return 0
    else:
        return -1
    
def check_quantity(a,b):
    if a >= b:
        inventory = a - b
        return 1,inventory
    else:
        return 0,0

def check_IPJ(a,b):
    if a == b:
        return 1
    else:
        return 0