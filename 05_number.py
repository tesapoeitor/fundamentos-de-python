#number
#calcular el promedio de los presupuestos de tres meses

badget_january = int(input("Ingresa el presupuesto de enero: "))
badget_february = int(input("Ingresa el presupuesto de febrero: "))
badget_march = int(input("Ingresa el presupuesto de marzo: "))

sum = badget_january + badget_february + badget_march

averange = sum / 3

print(f"El promedio de los presupuestos es: {averange}")