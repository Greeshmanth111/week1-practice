n=int(input("Enter parking hours:"))
a=0
b=0
if n<=2:
    a=30*n
elif 3<=n<=5:
    a=25*n
elif n>5:
    a=20*n
print("Parking charge:",a)

if a>150:
    b=20
print("Service charge:",b)

total=a+b
print("Final amount:",total)