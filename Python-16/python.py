
# 1-topshiriq
def anagram(soz1, soz2):

    if soz1.lower() == soz2.lower():
        print("Anagram")
    else:
        print("Anagram emas")

x = input("Birinchi so'zni kiriting: ")
y = input("Ikkinchi so'zni kiriting: ")
anagram(x, y)


# 2-topshiriq

def tub_sonlar(n):
    sonlar = []
    for i in range(2, n+1):
        tub = True
        for j in range(2, i):
            if i % j == 0:
                tub = False
                break
        if tub:
            sonlar.append(i)

    return sonlar
print(tub_sonlar(20))


# 3-topshiriq

def palindrom(x,y):
    if x.lower()[::-1] == y.lower()[::-1]:
        print("Ushbu so'zlar palindrom")
    else:
        print("Ushbu so'zlar palindrom emas")
soz1 = input("Birinchi so'zni kiriting: ")
soz2 = input("Ikkinchi so'zni kiriting: ")
palindrom(soz1, soz2)



# 4-topshiriq

def xisobla():
    sonlar = []
    while True:
        son = input(f"Son kiriting(stop orqali to'xtating): ")
        if son.lower() == "stop":
            break
        else:
            sonlar.append(int(son))
    print(f"\nSonlar yig'indisi: {sum(sonlar)}\nO'rta qiymati: {sum(sonlar)/len(sonlar)}")



