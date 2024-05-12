"""
#Funcion format: Se encierra las posiciones de las variables entre corchetes {}, y a continuacion del string llamamos a las variables con la funcion format.
x = 10
y = 5


print("Mis numeros son {} y {} ".format(x,y))

#cadenas literales (f-string): Podemos anticipar la concatenacion de variables anteponiendo f al string

color = "azul"
patente = 521

print(f"El auto es {color} y su patente es {patente}")

#Práctica Formatear Cadenas 1
#Necesitamos imprimir el nombre y número de asociado dentro de la siguiente frase:

#Estimado/a (nombre_asociado), su número de asociado es: (numero_asociado)

nombre_asociado = "Jesse Pinkman"
numero_asociado = 399058

print(f"Estimado/a {nombre_asociado}, su número de asociado es: {numero_asociado}")

#Práctica Formatear Cadenas 2
#Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente frase:

#Has ganado (puntos_nuevos) puntos! En total, acumulas (puntos_totales) puntos

puntos_nuevos = 350
puntos_totales = 1225

print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos")


#Práctica Formatear Cadenas 3
#Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente frase:

#Has ganado (puntos_nuevos) puntos! En total, acumulas (puntos_totales) puntos

#En esta ocasión, la cantidad de puntos acumulados (totales) será igual a los puntos_anteriores más los puntos_nuevos.

puntos_anteriores = 875
puntos_nuevos = 350
puntos_totales = puntos_anteriores + puntos_nuevos

print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos")




"""


