import math

peakX = float(input("peak x: "))
peakY = float(input("peak y: "))
dropX = float(input("drop x: "))
dropY = float(input("drop Y: "))

a = (peakY - dropY)/2
b = (math.pi)/(dropX - peakX)
c = (0-1) * peakY
d = (dropY + a)

print("A: " + str(a))
print("B: " + str(b))
print("C: " + str(c))
print("D: " + str(d))