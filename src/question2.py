cn=input()
age=int(input())
nt=int(input())
a=0
b=0
c=0
if age<12:
    b=120
    a=b*nt
elif 12<age<59:
    b=200
    a=b*nt
elif age<=60:
    b=150
    a=b*nt

print(cn)
print(b)
print(nt)
print(a)

if nt>=5:
    c=a*0.9
    print("Discount:10%")
    print("Final Amount:",c)
else:
    c=a
    print("No discount")
    print("Final Amount:",c)
