# 1-masala

kinolar = []
print("5-sevimli kinolaringizni kiriting:")
for i in range(5):
    kinolar.append(input(f"{i+1}-kino: "))
print(kinolar)

# 2-masala

# 
sonlar =list(range(11,100,2))
for son in sonlar:
    print(f"{son} ning kubi: {son**3}")



# 3-masala


# Juft sonlar ro'yxati:

sonlar = list(range(10,50,2))
print(f"Juft sonlar:  {sonlar}")
print(f"Juft sonlar soni: {len(sonlar)}")



# Toq sonlar ro'yxati:

sonlar = list(range(11,50,2))
print(f"Toq sonlar:  {sonlar}")
print(f"Toq sonlar soni: {len(sonlar)}")



# 4-masala

summa = 0   
sonlar = list(range(1,20,))
for son in sonlar:
    summa += son
print(f"Javob: {summa}")




