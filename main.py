import random

options = ("piedra", "papel", "tijera")
rounds = 0
user_wins = 0
computer_wins = 0

while True:
  print("*" * 15)
  print(f"ROUND {rounds}")
  print("*" * 15)

  if (computer_wins > 0 or user_wins > 0):
    print(f"computer wins {computer_wins}")
    print(f"user wins {user_wins}")

  user_option = input("piedra, papel o tijera => ").lower()
  computer_option = random.choice(options)

  if (not user_option in options):
    print("esa opción no es valida")
    print("")
    print("")
    continue

  print(f"user option => {user_option}")
  print(f"computer option => {computer_option}")

  if (user_option == computer_option):
    print("empate!")
  elif (user_option == "piedra"):
    if (computer_option == "tijera"):
      print("piedra le gana a tijera")
      print("user gana!")
      user_wins += 1
    else:
      print("papel le gana a piedra")
      print("computer gana!")
      computer_wins += 1

  elif (user_option == "papel"):
    if (computer_option == "piedra"):
      print("papel le gana a piedra")
      print("user gana!")
      user_wins += 1
    else:
      print("tijera le gana a papel")
      print("computer gana!")
      computer_wins += 1

  elif (user_option == "tijera"):
    if (computer_option == "papel"):
      print("tijera le gana a papel")
      print("user gana!")
      user_wins += 1
    else:
      print("piedra le gana a tijera")
      print("computer gana!")
      computer_wins += 1

  rounds += 1
  print("")
  print("")

  if (computer_wins == 2):
    print("#" * 15)
    print("computer gano!!")
    print("#" * 15)
    break
  if (user_wins == 2):
    print("#" * 15)
    print("user gano!!")
    print("#" * 15)
    break