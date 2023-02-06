#transformaciones de tipos
name = "Enrique"
print(type(name))

name = 12
print(type(name))

name = False
print(type(name))

print("Enrique" + "Aguilera")
print(10 + 12)
print("Enrique" + "12")

age = 23
print("Mi edad es " + str(age))
print(f"Mi edad es {age}")

age = input("Escribe tu edad => ")
print(type(age))
age = int(age)
print(f"Tu edad en 10 años será: {age + 10}")