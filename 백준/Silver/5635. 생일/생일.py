n = int(input())

students = []

for i in range(n):
  n,d,m,y = input().rstrip().split()
  d,m,y = map(int, (d,m,y))
  students.append((y,m,d,n))

students.sort()

print(students[-1][3])
print(students[0][3])
