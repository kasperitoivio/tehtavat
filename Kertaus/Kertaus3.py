kirjasto = {
    "kirja1": ["Author1", 2000, "Fantasy"],
    "kirja2": ["Author2", 2010, "Sci-Fi"]
}


print(kirjasto["kirja1"][0])
print(kirjasto["kirja2"][2])


kirjasto["kirja1"][2] = "Adventure"


kirjasto["kirja3"] = ["Author3", 2020, "Drama"]


del kirjasto["kirja2"]


print(kirjasto)