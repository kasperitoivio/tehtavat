leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat:" ))
luodit = float(input("Anna luodit:" ))

naulat_yht = leiviskat * 20 + naulat
luodit_yht = naulat_yht * 32 + luodit
grammat = luodit_yht * 13.3

kg = int(grammat // 1000)
g = int(grammat % 1000)

print(f"Massa nykymittojen mukaan: {kg} kilogrammaa ja {g} grammaa.")
