import collections, statistics

N = int(input())
header_fields = input().split()

Students = []
students = collections.namedtuple('student',header_fields)
for i in range(N):
    fields = input().split()
    student=students(*fields)
    Students.append(student)
    
print(statistics.mean([int(stu.MARKS) for stu in Students]))