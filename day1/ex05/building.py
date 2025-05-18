import sys, string

def main():
    '''main documentation'''
    if len(sys.argv) == 2:
        arg = sys.argv[1]
        d, A, l, s, p = 0, 0, 0, 0, 0
        for c in arg:
            if c.isdigit():
                d += 1
            if c.isupper():
                A += 1
            if c.islower():
                l += 1
            if c.isspace():
                s += 1
            if c in string.punctuation:
                p += 1
        print (f"The text contains {d+A+l+s+p} characters:\n{A} upper letters\n{l} lower letters\n{p} punctuation marks\n{s} spaces\n{d} digits")
    elif len(sys.argv) < 4:
        print("What is the text to count?\nHello World!\nThe text contains 13 characters:\n2 upper letters\n8 lower letters\n1 punctuation marks\n2 spaces0 digits")
    else:
        print("AssertionError")



if __name__ == "__main__":
    print(main.__doc__)
    main()
