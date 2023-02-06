#crear un programa que evalue si un número es par o impar
number = int(input("Ingresa un número: "))
if (number % 2 == 0):
  print(f"{number} es par")
else:
  print(f"{number} es impar")