import math


def convertRadians(angle, unit):
    if unit == 'd':
        angle = angle
    elif unit == 'r':
        angle = float(angle) * (math.pi/180)
    return angle
    
def angleAdd(angleOrg, angles, unit):
    angle = start + angleOrg
    angle = convertRadians(angle, unit)
    angles.append(angle)
    return angles

def angleSub(angleOrg, angles, unit):
    angle = start - angleOrg
    angle = convertRadians(angle, unit)
    angles.append(angle)
    return angles

while input('go: ') == 'y':

    function = input('sin, cos or tan: ')
    unit = input('deg or rad: ')
    number = input('number: ')
    Range = input('range: ')

    start = 180
    angles = []
        
    if Range == '':
        Range = 360    
    
    if float(number) < 0:
        number = abs(float(number))
        set = 1
    else:
        number = number
        set = 0
    
    if function == 's':
        angle1 = (180/math.pi) * math.asin(float(number))
        angles.append(convertRadians(angle1, unit))
        while int(start) <= int(Range):
            if start % 180 == 0:
                angles = angleSub(angle1, angles, unit)
            else:
                angles = angleAdd(angle1, angles, unit)
            start += 90
    if function == 'c':
        angle1 = (180/math.pi) * math.acos(float(number))
        angles.append(convertRadians(angle1, unit))
        while int(start) <= int(Range):
            if start % 180 == 0:
                angles = angleSub(angle1, angles, unit)
            else:
                angles = angleAdd(angle1, angles, unit)
            start += 90
    if function == 't':
        angle1 = (180/math.pi) * math.atan(float(number))
        angles.append(convertRadians(angle1, unit))
        while int(start) <= int(Range):
            if start % 180 == 0:
                angles = angleSub(angle1, angles, unit)
            else:
                angles = angleAdd(angle1, angles, unit)
            start += 90
    
    print('here are all possible points within the given range:')
    angles.sort()
    if set == 0:
        angles.pop(2)
        angles.pop(2)
    elif set == 1:
        angles.pop(0)
        angles.pop(0)
    print(round(angles[0], 2))
    print(round(angles[1], 2))
