import math

n1 = float(input())
n2 = float(input())
theta1 = float(input())

calc2 = math.sin(theta1)
print(calc2)
calc1 = abs(calc2*(180/math.pi))
print(calc1)

theta2 = math.asin(calc1)
print(theta2)

print((theta2 * (180/math.pi)))