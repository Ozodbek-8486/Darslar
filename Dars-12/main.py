menu = ['osh','jiz','shashlik','lavash','kabob','chuchvara']
buyurtmalar = []
narx = 0

x = int(input("Hurmatli mijoz,nechta taom buyurtirasiz: "))
for i in range(0,x):
    buyurtma = input(f"{i+1}-burutmani kiriting: ")
    buyurtmalar.append(buyurtma)


if buyurtmalar:
    for taom in buyurtmalar:
        if taom in menu:
            print(f"\nSizning {taom.title()} nomli buyurtmangiz qabul qilindi!")
        else:
            print(f"\nSizning {taom.title()} nomli buyurtmangiz mavjud emas!")

else:
    print("Savatchangiz bo'sh!")
for a in buyurtmalar:
    if a == "osh":
        narx += 10_000
    if a == "jiz":
        narx += 15_000
    if a == "shashlik":
        narx += 20_000
    if a == "lavash":
        narx += 25_000
    if a == "kabob":
        narx += 30_000
print(f"\nSizning buyurtmalar soningiz: {len(buyurtmalar)}")
print(f"Sizning to'lovingiz: {narx}")
