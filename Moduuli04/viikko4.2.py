while True:
    tuumat = float(input("Anna tuuma määrä (negatiivinen lopettaa): "))

    if tuumat < 0:
        print("Ohjelma lopetetaan")
        break

    sentit = tuumat * 2.54
    print(f"{tuumat} tuumaa on {sentit} cm")