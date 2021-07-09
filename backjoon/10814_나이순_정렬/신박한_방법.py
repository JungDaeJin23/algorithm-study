import sys


N = int(input())
people = [[] for _ in range(201)]
for _ in range(N):
    person = list(sys.stdin.readline().split())
    people[int(person[0])].append(person[1])
for i in range(201):
    for j in people[i]:
        print(i, j)