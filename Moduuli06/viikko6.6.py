import math

def laske_yksikkohinta(halkaisija_cm, hinta_euro):
    # Muutetaan säde metreiksi (halkaisija / 2 / 100)
    sade_m = (halkaisija_cm / 100) / 2
    pinta_ala_m2 = math.pi * (sade_m ** 2)
    return hinta_euro / pinta_ala_m2

def main():
    # Pizza 1 tiedot
    h1 = float(input("Anna 1. pizzan halkaisija (cm):"))
    p1 = float(input("Anna 1. pizzan hinta (e):"))

    # Pizza 2 tiedot
    h2 = float(input("Anna 2. pizzan halkaisija (cm): "))
    p2 = float(input("Anna 2. pizzan hinta(e): "))

    hinta1 = laske_yksikkohinta(1, 1)
    hinta2 = laske_yksikkohinta(2, 2)

    print(f"\nPizza 1 yksikköhinta: {hinta1:.2f} e/m**2")
    print(f"Pizza 2 yksikköhinta: {hinta2:.2f} e/m**2")

    if hinta1 < hinta2:
        print("Ensimmäinen pizza antaa paremman vastineen rahalla.")
    elif hinta2 < hinta1:
        print("Toinen pizza antaa paremman vastineen rahalle.")
    else:
        print("Molemmat ovat samanarvoisia")


main()