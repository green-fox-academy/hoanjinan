def new_filter(interable, function):
    for i in interable:
        if function(i):
            yield i