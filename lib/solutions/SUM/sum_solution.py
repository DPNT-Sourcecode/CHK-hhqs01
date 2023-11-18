# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    # Need to check if x and y in [0, 100]
    check_parameter(x)
    check_parameter(y)
    return x + y

def check_parameter(parameter):
    if not isinstance(parameter, int):
        raise TypeError("Input is not an integer")
    
    if parameter > 100 or parameter < 0:
        raise ValueError("Input is not in the expected range")