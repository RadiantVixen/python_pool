def slice_me(family: list, start: int, end: int) -> list:
    """ take an array then slice it"""
    result = []

    try:
        if not isinstance(family, list) or not all(isinstance(row, list) for row in family):
            raise AssertionError("the input most be a list of lists")
        for l in family:
            if len(l) != len(family[0]):
                raise AssertionError("lengths are not the same")
        print(f"My shape is : ({len(family)}, {len(family[0])})")
        if end < 0:
            end = len(family) + end
        print(end)
        while start < end:
            result.append(family[start])
            start += 1
        print(f"My new shape is: ({len(result)}, {len(result[0])})")
        return result

    except Exception as e:
        print(f"an error occurred {e}")
        return []


        

