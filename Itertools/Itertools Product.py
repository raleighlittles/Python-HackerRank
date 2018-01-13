import itertools
list_A = map(int, input().split())
list_B = map(int, input().split())
main_list = [list_A, list_B]
cartesian_product = list(itertools.product(*main_list))
print(*cartesian_product, sep=" ")