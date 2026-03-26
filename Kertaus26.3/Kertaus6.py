# Funktiot eri laskutoimituksille
def yhteenlasku(a, b):
    return a + b


def vahennyslasku(a, b):
    return a - b


def kertolasku(a, b):
    return a * b


def jakolasku(a, b):
    if b == 0:
        return "Nollalla ei voi jakaa!"
    return a / b


# Tulostetaan tervetuloviesti kerran ohjelman alussa
print("TERVETULOA KÄYTTÄMÄÄN LASKINTA!")

while True:
    # Tulostetaan valikko kuvan mukaisesti
    print("\nValitse mitä toimintoa haluat käyttää:")
    print("A: Yhteenlasku")
    print("B: Vähennyslasku")
    print("C: Kertolasku")
    print("D: Jakolasku")

    # Kysytään valinta ja muutetaan se isoksi kirjaimeksi (.upper())
    valinta = input("Valintasi (A-D, Q lopettaa): ").upper()

    # Jos käyttäjä syöttää Q, poistutaan silmukasta
    if valinta == 'Q':
        print("Kiitos ja hei hei!")
        break

    # Tarkistetaan onko valinta jokin sallituista kirjaimista
    if valinta in ('A', 'B', 'C', 'D'):
        x = float(input("Anna ensimmäinen luku: "))
        y = float(input("Anna toinen luku: "))

        if valinta == 'A':
            print("Tulos:", yhteenlasku(x, y))
        elif valinta == 'B':
            print("Tulos:", vahennyslasku(x, y))
        elif valinta == 'C':
            print("Tulos:", kertolasku(x, y))
        elif valinta == 'D':
            print("Tulos:", jakolasku(x, y))
    else:
        print("Virheellinen valinta, yritä uudelleen.")