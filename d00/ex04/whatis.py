import sys

def find_type():
    arg = sys.argv

    if len(arg) == 1:
        return
    elif len(arg) != 2:
        raise AssertionError("more than one argument is provided")
    
    try:
        val = int(arg[1])
        if val % 2 == 0 :
            print("I'm even.")
        else:
            print("I'm Odd.")
    except Exception :
        raise AssertionError("argument is not an integer")

if __name__ == "__main__" :
    try:
        find_type()
    except Exception as e:
        print(f"Assertion Error: {e}")

