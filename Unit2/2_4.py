#Create a module with 4 functions of your choice. Import and use the functions using module in different ways.



def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b



if __name__ == "__main__":

  
    print("Addition:", add(10, 5))

    
    import __main__

    print("Subtraction:", __main__.subtract(10, 5))

  
    import __main__ as mm

    print("Multiplication:", mm.multiply(10, 5))

    
    from __main__ import divide

    print("Division:", divide(10, 5))

