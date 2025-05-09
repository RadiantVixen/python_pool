import sys

if len(sys.argv) == 2:
    try:
        object = int(sys.argv[1])
        if object % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except ValueError:
        print("AssertionError: argument is not an integer")
else:
    print("AssertionError: more than one argument is provided")

if main == main:
    