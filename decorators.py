
def decorater_function(msg):
    message = msg  # free variable

    def wrapper_function():
        print(message)
    return wrapper_function

hi_p = decorater_function("hi")
bye_p = decorater_function("bye")
hi_p()
bye_p()
