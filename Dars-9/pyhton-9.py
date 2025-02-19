
# Kod-3
ism = input("Ismingizni kiriting: ")
if ism.lower() != "ozodbek":
    print(f"Uzur, {ism.title()} biz Ozodbekni kutayapmiz.)")
else:
    print("Salom,Ozodbek")



# Kod-2
javob = float (input("12x6 nechiga teng?>>>"))
if javob != 72:
    print("Javob noto'g'ri!")
else:
    print("Javob to'g'ri!")



# Kod-3

yosh = int(input("Yoshingiz nechida?>>>"))
if yosh >= 18:
    print("Xush kelibsiz!")
else:
    print("Kirish mumkin emas!")



# Kod-4

login = input("Yangi login tanlang: ")
if len(login) <=5:
    print("Login 5 ta harfdan iborat bo'lishi shart!")
else:
    print(f"{login} login sifatida qabul qilindi!")

# Kod-5

yosh = int(input("Iltimos yoshingiz kiriting?>>>"))
if yosh < 18:
    print("Kirishingiz bepul!")
elif 18 <= yosh <= 35:
    print(f"Sizning yoshingiz {yosh} da bo'lganligi sababli tizim sizga 10.000 so'm narx belgiladi.")
else:
    print(f"Sizning yoshingiz {yosh} da bo'lganligi sababli tizim sizga 5.000 so'm narx belgiladi.")

# Kod-6

a = int (input(f"Birinchi soni kiriting."))
b = int (input(f"Ikinchi soni kiriting."))
c = int (input(f"Uchinchi soni kiriting."))

son =[a, b, c]
son.sort()
print(son)

# Kod-7

login = input("Login kiriting: ")
parol = input("Parol kiriting: ")

if login.lower() == "admin" and parol == "12345678":
    print("Xush kelibsiz!")
else:
    print("Login yoki parol xato kiritildi.Iltimos boshqatdan urinib ko'ring! ")
