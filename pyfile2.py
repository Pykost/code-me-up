shape = input('please enter a shape ')
if shape == 'triangle':
    height = input('Enter a height ')
    height = int(height)
    while height < 0:
        height = input('Enter a height ')
        height = int(height)
    base = input('Enter a base ')
    base = int(base)
    while base < 0:
        base = input('Enter a base ')
        base = int(base)
    side1 = input('Enter a side')
    side1 = int(side1)
    while side1 < 0:
        side1 = input('Enter a side ')
        side1 = int(side1)
    side2 = input('Enter another side')
    side2 = int(side2)
    while side2 < 0:
        side2 = input('Enter another side ')
        side2 = int(side2)
    print('The area of the square is', height * base)
    print('The perimeter of the square is', (base + side1 + side2))
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