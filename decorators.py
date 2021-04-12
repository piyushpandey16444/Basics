def decorater_function(original_function):
    """
    This is the decorater function that takes original function
    """
    def wrapper_function():
        """
        this is wrapper function that when executed executes original function.
        """
        print(f"THIS IS DECORATOR FUNCT !")
        return original_function()
    return wrapper_function

@decorater_function
def display():
    print(f"This is display function !")

display()
