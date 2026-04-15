lentoasemat = {}

while True:
    toiminto = input("\nValitse toiminto (lisää, hae, lopeta): ").lower()

    if toiminto == "lisää":
        icao = input("Anna ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi

    elif toiminto == "hae":
        icao = input("Anna ICAO-koodi: ")
        if icao in lentoasemat:
            print(lentoasemat[icao])
        else:
            print("Ei löytynyt")

    elif toiminto == "lopeta":
        print("Ohjelma lopetettu.")
        break

    else:
        print("Virheellinen valinta")