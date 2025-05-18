import sys

def main():
    try :
        if len(sys.argv) != 4:
            raise AssertionError("AssertionError: the arguments are bad")
        morse = {" ": "/ ", "a": ".- ", "b": "-... ", "c": "-.-. ", "d": "-.. ",
        "e": ". ", "f": "..-. ", "g": "--. ", "h": ".... ", "i": ".. ", "j": ".--- ",
        "k": "-.- ", "l": ".-.. ", "m": "-- ", "n": "-. ", "o": "--- ", "p": ".--. ",
        "q": "--.- ", "r": ".-. ", "s": "... ", "t": "- ", "u": "..- ", "v": "...- ",
        "w": ".-- ", "x": "-..- ", "y": "-.-- ", "z": "--.. ", "0": "----- ", "1": ".---- ",
        "2": "..--- ", "3": "...-- ", "4": "....- ", "5": "..... ", "6": "-.... ",
        "7": "--... ", "8": "---.. ", "9": "----. "}

        for c in sys.argv[3].lower():
            if c in morse:
                print(morse[c], end = "")
            else:
                raise AssertionError("AssertionError: the arguments are bad")
        print("")
    
    except ValueError:
        print("k")


if __name__ == "__main__":
    main()



