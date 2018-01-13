#!/bin/python3

import sys, collections

if __name__ == "__main__":
    s = input().strip()
    count_object = collections.Counter(s)
    # Can't use most_common() here since ordering in this case is important but most_common uses arbitrary ordering if elements are equal
    output = sorted(count_object.items(), key=lambda x: (-x[1], x[0]))
    for i in range(0, 3):
        print("{} {}".format(output[i][0], output[i][1]))
