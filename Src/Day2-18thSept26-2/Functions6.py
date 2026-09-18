# *args -multiple arguments

def print_arguments(*args):
    print(args)
    print(args[-1])
    print(type(args))

print_arguments(1,2,3,4,5,'Indra')