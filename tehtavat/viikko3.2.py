hyttiluokka = input("Anna hyttiluokka (Lux, A, B, C): ")

if hyttiluokka == "Lux":
    print("hytti yläkannella ja parveke")
elif hyttiluokka == "A":
    print("ikkunnallinen hytti autokannen yläpuolella")
elif hyttiluokka == "B":
    print("ikkunaton hytti autokannen yläpuolella")
elif hyttiluokka == "C":
    print("Ikkunaton hytti autokannen alapuolella")
else:
    print("Virheellinen hyttiluokka")