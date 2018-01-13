def person_lister(f):
    def inner(people):
        # complete the function
        return map(f, sorted(people, key= lambda p: int(p[2]))) # sort on age
    return inner

