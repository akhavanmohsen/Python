x = input("number:")
x=int(x)
c=0
for i in range(1,x):
    if (x%i==0):
        c+=1
if (c==1):
    print("ODD Number")

else:
    print("NOT ODD Number")
print(c)