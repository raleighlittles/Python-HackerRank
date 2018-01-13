import statistics
def average(array):
    # your code goes here
    return(statistics.mean(list(set(array))))