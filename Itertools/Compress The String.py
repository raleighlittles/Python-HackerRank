import itertools
input_string = input()
for key, value in itertools.groupby(input_string):
    print("({}, {})".format(len(list(value)), key), end=" ")