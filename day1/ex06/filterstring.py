import sys
from ft_filter import ft_filter

def main():
    if len (sys.argv) == 5:
        num = int(sys.argv[4])
        stra = sys.argv[3]
        lc = stra.split(" ")
        result = ft_filter(lambda x: len(x) > num, lc)
        print(result)
    else:
        print ("AssertionError: the arguments are bad")

if __name__ == "__main__":
    main()

