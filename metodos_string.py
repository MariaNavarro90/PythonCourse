"""
texto = "Controlar la complejidad es la esencia de la programación"
resultado = texto

print(resultado)

"""
#Metodo para pasar a MAYUSCULAS "upper"

texto = "Controlar la complejidad es la esencia de la programación"
resultado = texto.upper()

print(resultado)

texto = "Controlar la complejidad es la esencia de la programación"
resultado = texto[2].upper()

print(resultado)

#METODO PARA PASAR A minusculas "lower"

texto = "Controlar la complejidad es la esencia de la programación"
resultado = texto.lower()

print(resultado)

#Metodo para separar "split"
#split separa los elementos tomando los espacios como quiebre de separacion

texto = "Controlar la complejidad es la esencia de la programación"
resultado = texto.split()

print(resultado)
#En este caso le estamos diciendo que tome como quiebre de separacion la letra "T"
texto = "Controlar la complejidad es la esencia de la programación"
resultado = texto.split("t")

print(resultado)

#Metodo unir "join"

a = "aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d])
print(e)

#metodo para buscar "find"

texto = "Controlar la complejidad es la esencia de la programación"
resultado = texto.find("a")

print(resultado)

#Metodo para remplazar "replace"

texto = "Controlar la complejidad es la esencia de la programación"
resultado = texto.replace("Controlar", "Comer")

print(resultado)

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
print(frase.replace("difícil", "fácil").replace("mala","buena"))

