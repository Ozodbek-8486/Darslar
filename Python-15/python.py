talabalar = ["Ozodbek","Og'abek","Nursilton","Zuxridin","Gavhar","G'olibek","Ogabek"]
n = 0
baxolar = {}

while n < len(talabalar):
    talaba = talabalar[n]
    n = 1 + n
    baxo = int(input(f"{talaba} ning baxosini kiriitng: "))
    baxolar[talaba] = baxo

print("\nTalabalar baxosi:")
for i,b in baxolar.items():
    print(f"{i} ning baxosi: {b}")





