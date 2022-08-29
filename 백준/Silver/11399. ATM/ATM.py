n = int(input())
lis = list(map(int,input().split()))
lis.sort()
sum = 0
sumofsum = 0
for i in lis:
    sum += i
    sumofsum += sum 

print(sumofsum)
