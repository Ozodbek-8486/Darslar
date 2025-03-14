

# 1-topshiriq


# def anogram(soz_1,soz_2):
#     if soz_1.lower() == soz_2.lower():
#         print("So'zlar bir xil")
#     else:
#         print("So'zlar bir xil emas")
# x = input("Birinchi so'zni kiriting: ")
# y = input("Ikkinchi so'zni kiriting: ")
# anogram(x,y)



# 2-topshiriq



# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# n = int(input("Sonni kiriting: "))
# print(fibonacci(n))




# 3-topshiriq



# def tub_sonlar(n):
#     tub_sonlar = []
#     for num in range(2, n + 1):
#         if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
#             tub_sonlar.append(num)
#     return tub_sonlar

# n = int(input("Sonni kiriting: "))
# print(tub_sonlar(n))    


# 3-topshiriq

# def tub_sonlar(n):
#     sonlar = []
#     for i in range(2,n+1):
#         tub = True
#         for j in == range(2,i):
#             tub = False
#             break
#         if tub:
#             sonlar.append(i)
#     return sonlar



# 4-topshiriq
def xisobla(n):
    sonlar = []
    while True:
        son = int(input(f"Sonni kiriting: "))
        if str(son).lower() == "stop":
            break
            print("Xayr")

        else:
            sonlar.append(int(son))
    print(f"Kiritilgan sonlar yig'indisi: {sum(sonlar)}\nO'rtacha qiymati:{sum(sonlar)}")

       
xisobla()







