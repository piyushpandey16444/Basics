
def decorater_function(original_function):
    def wrapper_function():
        print(f"THIS IS DECORATOR FUNCT !")
        return original_function()
    return wrapper_function

@decorater_function
def display():
    print(f"This is display function !")

display()