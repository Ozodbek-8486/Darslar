from mahsulotlar import mahsulotlar
    
def buyurtma_berish():
    narxlar = []
    ishora = True
    while ishora:
        # Foydalanuvchidan mahsulot nomini so'rang.
        mahsulot_nomi = input("Mahsulot nomini kiriting:").lower().strip()

# Agar mahsulot mavjud bo'lsa narxlar ro'yxatiga qo'shiladi.
if mahsulot_nomi in mahsulotlar:
    narx = mahsulotlar[mahsulot_nomi]
    narxlar.append(narx)
    print(f"mahsulot_nomi.capitalize() narxi {narx} so'm")
else:
    print("Bizda bunday mahsulot yo'q.")

# Foydalanuvchidan yana mahsulot tanlashi i so'rang.
javob = input("Yana mahsulot tanlaysizmi? (ha/yo'q): ").lower()
if javob == "yo'q" or javob == "no":
    ishora = False
elif javob == "ha" or javob == "yes":
    continue
else:
    ishora = False

# Umumiy to'lov miqdorini hisoblang.
jami_summa = sum(narxlar)
print(f"Umumiy to'lov miqdori: {jami_summa} so'm")

