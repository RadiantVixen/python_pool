def ft_filter(func, lst):
    ''' filter(function or None, iterable) --> filter object

        Return an iterator yielding those items of iterable for which function(item)
        is true. If function is None, return the items that are true.'''
    result = []

    for item in lst:
        if func is None:
            if item:
                result.append(item)
        elif func(item):
            result.append(item)
    return iter(result)


