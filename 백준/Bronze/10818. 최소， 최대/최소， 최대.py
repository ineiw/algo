import sys

n = int(input())

datas = list(map(int,input().split()))

min,max = 10000000,-10000000

for i in datas:
    if min > i:
        min = i
    if max < i:
        max = i

print(min,max)