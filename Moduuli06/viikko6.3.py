def gallona_litroiksi(gallonat):
    return gallonat * 3.785

def main():
    while True:
        g = float(input("Syötä gallonmäärä (negatiivinen luku lopettaa): "))
        if g < 0:
            print("Lopetetaan ohjelma.")
            break
        litrat = gallona_litroiksi(g)
        print(f"{g} gallonaa on {litrat: .2f} litraa.")

main()