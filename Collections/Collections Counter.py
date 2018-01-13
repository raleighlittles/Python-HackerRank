import collections
num_shoes = int(input())
shoe_sizes = list(map(int, input().split()))
shoe_sizes_dict = collections.Counter(shoe_sizes)

num_customers = int(input())
earned_amount = 0
for c in range(0, num_customers):
    shoe_size, price = map(int, input().split())
    if shoe_sizes_dict[shoe_size] > 0:
        shoe_sizes_dict[shoe_size] = shoe_sizes_dict[shoe_size] - 1
        earned_amount += price
        
        
print(earned_amount)        