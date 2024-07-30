import math

while input('go: ') == 'y':

    function = input('sin, cos or tan: ')
    unit = input('deg or rad: ')
    number = input('number: ')
    Range = input('range: ')

    start = 180
    angles = []

    if unit == 'd':
        number = number
    elif unit == 'r':
        number = float(number) * (180/math.pi)
        
    if function == 's':
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
    if function == 'c':
        angle1 = (180/math.pi)*math.acos(float(number))
        angles.append(angle1)
        while int(start) <= int(Range):
            if start % 180 == 0:
                angle2 = start - angle1
                angles.append(angle2)
            else:
                angle2 = start + angle1
                angles.append(angle2)
            start += 90
    if function == 't':
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