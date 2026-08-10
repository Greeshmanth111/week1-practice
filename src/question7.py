n=int(input())
a=[]
for _ in range(n):
    a.append(int(input()))
result=[]
for i in a:
    if not result or i!=result[-1]:
        result.append(i)
print(result)