def kuusi(koko):
    print("Tämä on kuusi!")
    # Tulostetaan kuusen lehvät
    for i in range(1, koko + 1):
        tahdet = "*" * (2 * i - 1)
        valilyonnit = " " * (koko - i)
        print(valilyonnit + tahdet)
    # Tulostetaan kuusen runko
    print(" " * (koko - 1) + "*")

# Kutsutaan funktiota esimerkin mukaisesti
kuusi(5)