import random
comp_number = random.randint(1,99)
print('My guess is', comp_number)
myresults = input('Is it true ? ( b=bigger , s=smaller , y=yes ): ')
while myresults !=  'y' :
    if myresults == 'b' :
        comp_number = random.randint(comp_number,99)
        print('My guess is', comp_number)
        myresults = input('Is it true ? ( b=bigger , s=smaller , y=yes ): ')
        
    else:
        comp_number = random.randint(1,comp_number)
        print('My guess is', comp_number)
        myresults = input('Is it true ? ( b=bigger , s=smaller , y=yes ): ')
        
        
print('Excellent, You are win')
