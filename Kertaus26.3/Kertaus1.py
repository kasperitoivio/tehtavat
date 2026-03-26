numero = int(input("Anna numero (1-10): "))

if 1 <= numero <= 10:
    for i in range(1, 11):
        print(f"{i} * {numero} = {i * numero}")
else:
    print("Numero ei ollut välillä 1-10.")