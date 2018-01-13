if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    tupl = tuple(integer_list)
    print(hash(tupl))
