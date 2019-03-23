N=int(input('please give me a number '))

while N < 0:
    N = input('please give me a number ')
    N = int(N)
    
#While added so it loops every time a negative number is given until the user gives the expected answer.

for i in range(1,N+1):
    if i%3==0:
        x=i
        
print (x)
