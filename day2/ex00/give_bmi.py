import numpy

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    BMIs = []

    try:
        if len(height) != len(weight):
            raise AssertionError("lists are not on the same size!!!")
        for w, h in zip(weight, height):
            if not isinstance(w, (int, float)) or not isinstance(h, (int, float)):
                raise AssertionError("number is neither an integer or float")
            else:
                BMIs.append(w / (h ** 2))
        
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    
    return BMIs



def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    result = []

    try:
        for n in bmi:
            if not isinstance(n, (int, float)):
                raise AssertionError("neither an integer or float")
            result.append(n > limit)
    except Exception as e:
        print(f"an error occurred {e}")
        return []
    return result
        

