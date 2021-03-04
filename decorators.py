
def decorater_function():
    message = 'Hi'  # free variable

    def wrapper_function():
        print(message)
    return wrapper_function

p = decorater_function()
p()
