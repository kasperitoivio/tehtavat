oppilaat = {
    "Matti": ["Matti", 9, "Math"],
    "Liisa": ["Liisa", 8, "Art"]
}


print(oppilaat["Matti"][1])
print(oppilaat["Liisa"][2])


oppilaat["Matti"][2] = "Physics"


oppilaat["Teemu"] = ["Teemu", 7, "Music"]


del oppilaat["Liisa"]


print(oppilaat)