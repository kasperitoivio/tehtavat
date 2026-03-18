import random

maara = int(input("Montako arpakuutiota heitetään: "))

summa = 0

for i in range(maara):
    heitto = random.randint(1, 6)
    summa = summa + heitto

print("Silmälukujen summa on: ", summa)