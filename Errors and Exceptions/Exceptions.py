T = int(input())
for i in range(0, T):
    a, b = input().split()
    try:
        print(int(a)//int(b))
    except (ValueError, ZeroDivisionError) as e:
        print("Error Code:", e)