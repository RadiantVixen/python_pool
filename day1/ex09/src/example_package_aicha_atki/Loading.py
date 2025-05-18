def ft_tqdm(lst: range):
    '''Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested.'''
    
    for i in lst:
        per = int(100 * i / lst.stop) + 1
        per2 = int(80 * i / lst.stop) + 1
        bar = "-" * (per2) + ">" + " " * (80 - per2)
        line = f"{per}%|[{bar}]| {i}/{lst.stop}"
        print(f"\r{line}", end="", flush=True)
        yield i