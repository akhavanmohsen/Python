Number = int(input('Please enter your 3 digit number : '))
A1 = str(Number // 100)
A2 = str((Number % 100) // 10)
A3 = str((Number % 100) % 10)
# A4 = A1+A2+A3
# Num= str(A3)+str(A2)+str(A1)
print(int(A3+A2+A1)*2)