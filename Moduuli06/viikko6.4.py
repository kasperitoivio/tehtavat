def laske_summa(luvut):
    return sum(luvut)

def main():
    testilista = [123, 111, 678, 1]
    tulos = laske_summa(testilista)
    print(f"Listan {testilista} summa on: {tulos}")

main()