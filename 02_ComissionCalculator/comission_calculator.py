nombre_completo = input("Me diarias tu nombre completo ")
ventas = int(input("Cual fue el monto total de tus ventas? "))
comision = round(ventas * (13/100), 2)
print(f"{nombre_completo} el monto total de tu comision por tus ventas es ${comision}")
