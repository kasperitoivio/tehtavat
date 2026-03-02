syote = input("Anna luku (tyhjä lopettaa): ")

if syote == "":
    print("Tu pelle et syöttäny yhtäkää lukua.")

else:
    pienin = float(syote)
    suurin = float(syote)

    while True:
        syote = input("Anna luku (tyhjä lopettaa): ")

        luku = float(syote)

        if luku < pienin:
            pienin = luku

        if luku > suurin:
            suurin = luku

    print("Pienin luku:", pienin)
    print("Suurin luku:", suurin)

