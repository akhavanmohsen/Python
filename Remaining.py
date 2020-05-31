Number = int(input('Please enter your number : '))
Remaining = Number % 10
if Remaining == 0 :
	print('Next Number is : ', Number+10)
else:
	temp = 10 - Remaining
	print('Next Number is : ', temp+Number)