n = int(input())

ab = list(map(int,input().split()))

ab2 = sorted(ab)
ab_dict = {}

i = 0
for a in ab2:
    if a in ab_dict:
        continue
    ab_dict[a] = i
    i+=1

for a in ab:
    print(ab_dict[a],end=" ")
