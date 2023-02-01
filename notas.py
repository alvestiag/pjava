not1 = 0
not2 = 0
media = int

not1 = float(input("digite a primeira nota: "))
not2 = float(input("digite a segunda nota: "))

media = (not1 + not2) / 2
print("A média foi: ", media)

if media >= 7 and media < 10:
    print("Aprovado")
elif media == 10:
    print("Aprovado com distinção")
else:
    print("Reprovado")