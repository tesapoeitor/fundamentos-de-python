name = "Enrique"
last_name = "Aguilera"
age = 23
print(name)
print(last_name)
print(age)

full_name = name + " " + last_name
print(full_name)

quote = "I'm Enrique"
print(quote)

quote2 = 'She said "Hello"'
print(quote2)

#format
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name + " y tengo " + str(
  age) + " años."
print(template)

template = "Hola, mi nombre es {} y mi apellido es {} y tengo {} años.".format(
  name, last_name, age)
print(template)

template = f"Hola, mi nombre es {name} y mi apellido es {last_name} y tengo {age} años."
print(template)