import math


def luo_piste(x, y):
    return (x, y)


def etaisyys(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)


x1 = float(input("Anna x1: "))
y1 = float(input("Anna y1: "))
x2 = float(input("Anna x2: "))
y2 = float(input("Anna y2: "))

p1 = luo_piste(x1, y1)
p2 = luo_piste(x2, y2)

d = etaisyys(p1, p2)


print("Etäisyys:", round(d, 2))