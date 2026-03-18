luvut = []

while True:
    annettu = input("anna luku (tyhjä lopettaa): ")

    if annettu == "":
        break

    luvut.append(float(annettu))
luvut.sort(reverse= True)

print("viisi suurinta lukua: ")
for luku in luvut [:5]:
    print(luku)