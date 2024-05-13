dic = {'c1':55, 'c2':[10,20,30], 'c3':{'s1':100, 's2':200}}
print(dic['c2'][2])
#buscar un elemento y pasarlo a mayusculas
dic1 = {'c1':['a','b','c'], 'c2':['d','e','f']}
print(dic1['c2'][1].upper())

dic2 = {1:'a', 2:'b'}
print(dic2)
#Agregar un elemento al diccionario
dic2[3] = 'c'

print(dic2)
#Sobre escribir un elemento
dic2[2] = 'B'

print(dic2)

#Con .keys vamios a saber todas las claves de mi diccionario
print(dic2.keys())
#Con .values vamos a saber los valores de nuestras claves
print(dic2.values())
#Con .items podemos saber la clave y el valor del diccionario
print(dic2.items())

#Ejercicios de practica
#1)

#nombre: Karen
#apellido: Jurgens
#edad: 35
#ocupacion: Periodista

mi_dic = {'nombre':'Karen','apellido':'Jurgens','edad'
:35,'ocupacion':'Periodista'}
print(mi_dic)

#2)
mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict["puntos"]["points2"][1])

#3)

mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}

mi_dic["edad"] = 36
mi_dic["ocupacion"] = "Editora"
mi_dic["pais"] = "Colombia"

print(mi_dic)