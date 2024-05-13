"""m_tuple = (1,2,3,4)
print(m_tuple)

mi_tuple = (1,2,(20,10),3)

mi_tuple = list(mi_tuple)

mi_tuple = tuple(mi_tuple)

print(type(mi_tuple))"""

t = (1,2,3)
x,y,z = t
print(x,y,z)

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(mi_tupla.count(2))

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_tupla = list(mi_tupla)
mi_lista = mi_tupla
print(type(mi_lista))

mi_tupla = (1, 2, 3, 4)
a,b,c,d = mi_tupla
print(a,b,c,d)