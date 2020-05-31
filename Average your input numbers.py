numb= int(input('Please enter your number: ' ))
sum_num=0
count=0
while numb != -1 :
    sum_num = sum_num + numb
    numb= int(input ('Please enter your number: '))
    count = count + 1

print ('Your average is : ' , sum_num // count)