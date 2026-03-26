def suurin_arvo(a, b, c):
    return max(a, b, c)

# Kysytään luvut input-funktiolla
luku1 = float(input("Anna 1. luku: "))
luku2 = float(input("Anna 2. luku: "))
luku3 = float(input("Anna 3. luku: "))

suurin = suurin_arvo(luku1, luku2, luku3)
print(f"Suurin arvo on: {suurin}")