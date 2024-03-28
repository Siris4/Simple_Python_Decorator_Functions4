import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before
        function()
        function()
        # Do something after
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye")

# Without the @ syntactic sugar
def say_greeting():
    print("How are you?")

decorated_function = delay_decorator(say_greeting)
# Call the decorated function
decorated_function()

# This last print line seems to be a misunderstanding of decorators usage.
# If you want to demonstrate calling the decorated function directly, it should be like this:
say_hello()  # This will automatically include the delay because of the @delay_decorator
say_bye()    # Same as above

# If you're trying to use the decorator directly in a single call, it’s not done with print, but like this:
delay_decorator(say_greeting)()
