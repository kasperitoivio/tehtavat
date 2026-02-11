leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat:" ))
luodit = float(input("Anna luodit:" ))

#muunnokset
luoti_grammoina = 13.3
naula_grammoina = 32 * luoti_grammoina
leiviskat_grammoina = 20 * naula_grammoina

massa_grammoina = (leiviskat * leiviskat_grammoina + naulat * naulat_grammoina + luodit * luoti_grammoina)

kilot = int(massa_grammoina // 1000)
grammat = massa_grammoina % 1000

print(f"{kilot} kilogrammaa ja {grammat} grammaa.")