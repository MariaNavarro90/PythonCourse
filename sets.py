mi_set = set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)

otro_set = {1,2,3}
print(type(otro_set))
print(otro_set)

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2) #unir sets con .union

s1.add(4) #agregar con .add

s1.remove(3) #eliminamos con .remove

s1.discard(6) #descarta un elemento

s1.pop() #Elimina un elemento aleatoria. se usa en sorteos

s1.clear() #vacia el set

print(s1)

mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5}
mi_set_3 = mi_set_1.union(mi_set_2)
print(mi_set_3)

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.pop()
print(sorteo)

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.add("Damián")
print(sorteo)
