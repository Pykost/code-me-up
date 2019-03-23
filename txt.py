age = input('How old are you?')
age = age.strip
while not age.isdigit():
    age = input('Age must be a number!Try again.')
age = int(age)
while age<0 or age>100:
    age = input('age must be between 0 and 100!Try again.')


int(age)

0<age<100