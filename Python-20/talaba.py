from datetime import datetime
hozir = datetime.now()  
def talablar(ism,familiya,kurs,yonalish,tugulgan_yil,yosh):
    talablar = {
        'ism':ism,
        'familiya':familiya,
        'kurs':kurs,
        'yonalish':yonalish,
        'tugulgan_yil':tugulgan_yil,
        'yosh':yosh
    }
    print(f"\n Ism: {ism} \nFamiliya: {familiya} \nKurs: {kurs} \nYonalish: {yonalish} \nTugulgan yil: {tugulgan_yil} \nYosh: {hozir.year - tugulgan_yil} ")

ism = input("Ismingizni kiriting: ")
familiya = input("Familiyangizni kiriting: ")
kurs = input("Kursingizni kiriting: ")
yonalish = input("Yonalishingizni kiriting: ")
tugulgan_yil = int(input("Tugulgan yilingizni kiriting: "))
yosh = hozir.year - tugulgan_yil
talablar(ism,familiya,kurs,yonalish,tugulgan_yil,yosh)









