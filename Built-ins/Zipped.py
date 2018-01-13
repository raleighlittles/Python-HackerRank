import statistics

N, X = map(int, input().split())
all_scores = []
for i in range(0, X):
    grades = input().split()
    all_scores.append([float(g) for g in grades])
    #print(grades)


for stu_score in zip(*all_scores): # Unpack the all_scores list and apply zip on it!
    print(statistics.mean(stu_score))