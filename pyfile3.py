N = int ( input ('Please give me a number '))

for i in range (1 , N + 1):

    if i % 15 == 0:
        print ('FizzBuzz')
        
    elif i % 5 == 0:
        print ('Fizz')
        
    elif i % 3 == 0:
        print ('Buzz')
        
    else:
        print (i)
