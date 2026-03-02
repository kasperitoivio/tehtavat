tunnus_oikein = "python"
salasana_oikein = "rules"
yritykset = 0

while yritykset < 5:
    tunnus = input("Käyttäjätunnus: ")
    salasana = input("Salasana: ")

    if tunnus == tunnus_oikein and salasana == salasana_oikein:
        print("Tervetuloa")
        break
    else:
        yritykset += 1
        if yritykset < 5:
            print(f"Väärin. Yrityksiä jäljellä {5 - yritykset}")
        else:
            print("Pääsy evätty")