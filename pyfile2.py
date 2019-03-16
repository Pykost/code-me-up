shape = input('Please choose a shape . Triangle or square ')

if shape == 'triangle':

    height = input('Enter a height ')
    height = int(height)

    while height < 0:
        #I am picking the command while so that I can loop the same thing over and over until the user gets it right

        height = input('Please enter a height ')
        height = int(height)

    base = input('Please enter a base ')
    base = int(base)

    while base < 0:

        base = input('Please enter a base ')
        base = int(base)

    side1 = input('Please enter a side ')
    side1 = int(side1)
    #first side of the triangle

    while side1 < 0:

        side1 = input('Please enter a side ')
        side1 = int(side1)

    side2 = input('Please enter another side ')
    side2 = int(side2)
    #second side of the triangle

    while side2 < 0:

        side2 = input('Please enter another side ')
        side2 = int(side2)

    print('The area of the square is', height * base)

    print('The perimeter of the square is', (base + side1 + side2))
    #I took the height and 2 other sides because I wanted the perimeter of any triangle not just from a rectangulare

elif shape == 'square':
    i = input('Please enter a side ')
    i = int(i)
    while i < 0:

        i = input('Please enter a side ')
        i = int(i)

    j = input('Please enter a different side ')
    j = int(j)

    while j < 0:

        j = input('Please enter a different side ')
        j = int(j)

    print('The area of the square is', i * j)

    print('The perimeter of the square is', 2 * i + 2 * j)
