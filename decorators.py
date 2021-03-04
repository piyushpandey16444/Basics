
def decorater_function(msg):
    def wrapper_function():
        print(msg)
    return wrapper_function

def display():
    print(f"This is mesaage: {msg}")