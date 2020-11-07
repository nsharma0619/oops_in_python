def decorator_function(original_function):
    def wrapper_function():
        print("i am in wrapper now")
        return original_function()
    return wrapper_function



@decorator_function
def display():
    print("i am in this function")

# decorated_function = decorator_function(display)

# decorated_function()
display()