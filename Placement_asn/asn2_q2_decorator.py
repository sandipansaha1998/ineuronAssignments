# decorators act as wrapper functions and add extra functionality to the existing functions.

def decorate(fn):
    print("********")
    fn()
    print("********")
@decorate
def func():
    print("Hello World")

