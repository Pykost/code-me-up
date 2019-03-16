N=int(input('please give me a number '))
while N < 0:
    N = input('please give me a number ')
    N = int(N)
for i in range(1,N+1):
    if i%3==0:
        x=i
print (x)
