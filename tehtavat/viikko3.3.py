sukupuoli = input("Anna sukupuoli (nainen/mies): ")
hb = int(input("Anna hemoglobiiniarvo: "))

if sukupuoli == "nainen":
    if hb < 117:
        print("Alhainen")
    elif hb <= 175:
        print("Normaali")
    else:
        print("Korkea")

elif sukupuoli == "mies":
    if hb < 134:
        print("Alhainen")
    elif hb <= 195:
        print("Normaali")
    else:
        print("Korkea")