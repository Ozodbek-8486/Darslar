
# 1-topshiriq 

class Kitob:
    def __init__(self, nomi, muallif,sahifa_soni):
        self.nomi = nomi,
        self.muallif = muallif
        self.sahifa_soni = sahifa_soni
    def __info__(self):
        print("Kitob nomi: ",self.nomi)
        print("Muallifi: ",self.muallif)
        print("Sahifa soni: ",self.sahifa_soni)

kitob1 = Kitob("Ufq", "Abdulla Qodiriy", 100 )
kitob2 = Kitob("Jinoyat va Jazo", "Dostoyevskiy", 120)
kitob3 = Kitob("Otgan kunlar", "O'tkir Hoshimov", 150)

kitob1.__info__()
print("Kitob nomi:", kitob1.nomi)
kitob2.__info__() 
print("Kitob muallifi:",kitob2.muallif)
kitob3.__info__()
print("Kitob sahifasi:",kitob3.sahifa_soni)


# 2-topshiriq

class Hodim:
    def __init__(self,ismi):
         self.ismi = ismi
    def ish_turi(self):
        print(f"{self.ismi} Umumiy ishlarni bajaradi.")
      
            
class Menejer(Hodim):
    def ish_turi(self):
        print(f"{self.ismi} menejerlik vazifalarini bajaradi.")

h1 = Hodim("Ali")
m2 = Menejer("Dilshod")

h1.ish_turi()
m2.ish_turi()


# 3-topshiriq
class Hayvon:
    def __init__(self,nomlari):
        self.nomlari = nomlari

class Mushuk(Hayvon):
    def ovoz_turi (self):
        print(f"\n Bu mushukning ovozi:  {self.nomlari}")
        # self.ovoz_turi = ovoz_turi

class Kuchuk(Hayvon):
    def ovoz_turi(self):
        print(f" Bu Kuchukning ovozi: {self.nomlari}")

class Qush (Hayvon):
    def ovoz_turi (self):
        print(f" Bu Qushning ovozi: {self.nomlari}\n")
h1 = Hayvon("Ovozlari")
m2 = Mushuk("miyov-miyov")
n3 = Kuchuk("vov-vov")
l4 = Qush("qov-qov")

# h1.ovoz_turi()
m2.ovoz_turi()
n3.ovoz_turi()
l4.ovoz_turi()


