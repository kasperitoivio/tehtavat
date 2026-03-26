# Luodaan lista itse
sanat = ["puuhöylä", "nahkaiset", "punaiset", "stringit", "moi", "mato"]
yli_5_kirjainta = 0

for sana in sanat:
    if len(sana) > 5:
        yli_5_kirjainta += 1

print(f"Listassa on {yli_5_kirjainta} sanaa, joissa on enemmän kuin 5 kirjainta.")