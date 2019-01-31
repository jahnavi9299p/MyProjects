n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
print(student_marks[query_name])
s=[]
# a=s.[0]
# b=s.[1]
# c=s.[2]
# avg=(a+b+c)/3
# print("0.2f",avg)
s=student_marks[query_name].copy()
a=s[0]
b=s[1]
c=s[2]
avg=(a+b+c)/3
print("%0.2f"%(avg))