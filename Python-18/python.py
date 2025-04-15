# 1-topshiriq
# import math

# print("Doiraning radiusini hisoblash")
# input = input("Radiusni kiriting: ")
# print("Doiraning yuzi: ", math.pi*int(input)**2)


# 2-topshiriq

import random

foydalanuvchi_soni = int(input("1 dan 100 gacha hohlagan bitta soningizni kiriting: "))

kampyuter_soni = random.randint(1, 100)

if foydalanuvchi_soni >= kampyuter_soni:
    print("Siz yutdingiz!")
else:
    print("Siz yutqazdingiz!")

# Kompyuter tanlagan son
print(f"Kompyuter tanlagan son: {kampyuter_soni}")







