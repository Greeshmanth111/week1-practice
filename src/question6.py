n=int(input())
a=[]
for _ in range(n):
    a.append(int(input()))
print("Total expenses:",sum(a))
print("Average expenses:",sum(a)/n)
print("Highest expense:",max(a))
print("Lowest expense:",min(a))
b=0
c=0
for i in a:
    if i>500:
        b+=1
    if i<=500:
        c+=1
print("Number of expanses above 500:",b)
print("Number of expanses below 500:",c)
