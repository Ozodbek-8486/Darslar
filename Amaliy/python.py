# 1-topshiriq

# class Shape:
#     def __init__ (self,name):
#         self.name = name

#     def info(self):
#         return f"{self.name} bu geometrik shakldir."

# class Triangle(Shape):
#     def __init__(self):
#         super().__init__("Uchburchak")
#     def sides(self):
#             return 3
# class Square(Shape):
#     def __init__(self):
#         super().__init__("Kavadrat")
#     def sides(self):
#             return 4
        
# triangle = Triangle()
# square = Square()

# print(triangle.info())
# print(f" Soni: {triangle.sides()} ta tomon.")



# print(square.info())
# print(f"Soni: {square.sides()} ta tomon.")



# 2-topshiriq


def check_shape(shape_name):
    
    shape_name = shape_name.lower()
    if shape_name == "triangle":
        shape = Triangle()
    elif shape_name == "square":
        shape = Square()
    else:
        return "Bunday shakl yo‘q"
    
    return f"{shape.info()} Soni: {shape.sides()} ta tomon."
print(check_shape("Triangle"))
print(check_shape("Square"))
print(check_shape("Circle"))


# 3-topshiriq









