import math

while input('go: ') == 'y':

    function = input('sin, cos or tan: ')
    unit = input('deg or rad: ')
    number = input('number: ')
    Range = input('range: ')

    start = 180
    angles = []

    if unit == 'deg':
        number = number
    elif unit == 'rad':
        number = number * (180/math.pi)
        
    #number = float(number) * (math.pi/180)
    if function == 'sin':
        angle1 = (180/math.pi)*math.asin(float(number))
        angles.append(angle1)
        while int(start) <= int(Range):
            print(start)
            if start % 180 == 0:
                print(4)
                angle2 = start - angle1
                angles.append(angle2)
            else:
                angle2 = start + angle1
                angles.append(angle2)
            start += 90
    if function == 'cos':
        angle1 = (180/math.pi)*math.ascos(float(number))
        angles.append(angle1)
        while int(start) <= int(Range):
            if start % 180 == 0:
                angle2 = start - angle1
                angles.append(angle2)
            else:
                angle2 = start + angle1
                angles.append(angle2)
            start += 90
    if function == 'tan':
        angle1 = (180/math.pi)*math.atan(float(number))
        angles.append(angle1)
        while int(start) <= int(Range):
            if start % 180 == 0:
                angle2 = start - angle1
                angles.append(angle2)
            else:
                angle2 = start + angle1
                angles.append(angle2)
            start += 90

    print('here are all possible points within the given range:')
    print(angles)