
# 1-topshiriq

# a = int(input(f"A sonini kiritling: "))
# b = int(input(f"B sonini kiritling: "))

# if a  <=0:
#     print("Bu son katta: ")
# if b >=0:
#     print("Bu son kichkina: ")

# 2-topshiriq
# hafta = int(input(f"Son kiriting: "))
# if   hafta range(1,2,12):
#     print (f"Hozir Qish oyi!")
# elif hafta range(3,5):
#     print(f"Hozir Bahor oyi!")
# elif hafta range(6,8):
#     print(f"Hozir Yoz oyi! ")
# elif hafta range(9,11):
#     print(f"Hozir Kuz oyi!")
# else:
#     print("Bunday oy yo'q!")

oy = int(input("Oy raqamini kiriting: "))
if oy in[12,1,2]:
    print("Qish")
if oy in[3,4,5]:
    print("Bahor")
if oy in[6,7,8]:
    print("Yoz")
if oy in[9,10,11]:
    print("Kuz")
else:
    print("bunday oy yo'q!")