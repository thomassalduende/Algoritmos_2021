from arbol_binario_thomi import Arbol
arbol_nombre = Arbol()
arbol_codigo = Arbol()

dionosaurio = {'name': "T-Rex", 'codigo': '4979', 'caracter': 'A7'}
arbol = arbol_nombre.insertar_nodo(dionosaurio['name'], dionosaurio)
arbol1 = arbol_codigo.insertar_nodo(dionosaurio['codigo'], dionosaurio)
dionosaurio = {'name': "Saltasaurus", 'codigo': '1880', 'caracter': 'A4'}
arbol = arbol_nombre.insertar_nodo(dionosaurio['name'], dionosaurio)
arbol1 = arbol_codigo.insertar_nodo(dionosaurio['codigo'], dionosaurio)
dionosaurio = {'name': "Ornithomimus", 'codigo': '6575', 'caracter': 'A1'}
arbol = arbol_nombre.insertar_nodo(dionosaurio['name'], dionosaurio)
arbol1 = arbol_codigo.insertar_nodo(dionosaurio['codigo'], dionosaurio)
dionosaurio = {'name': "Eoraptor", 'codigo': '792', 'caracter': '1A'}
arbol = arbol_nombre.insertar_nodo(dionosaurio['name'], dionosaurio)
arbol1 = arbol_codigo.insertar_nodo(dionosaurio['codigo'], dionosaurio)
dionosaurio = {'name': "Diplodocus", 'codigo': '548', 'caracter': '3B'}
arbol = arbol_nombre.insertar_nodo(dionosaurio['name'], dionosaurio)
arbol1 = arbol_codigo.insertar_nodo(dionosaurio['codigo'], dionosaurio)
dionosaurio = {'name': "Sgimoloch", 'codigo': '5448', 'caracter': '3C'}
arbol = arbol_nombre.insertar_nodo(dionosaurio['name'], dionosaurio)
arbol1 = arbol_codigo.insertar_nodo(dionosaurio['codigo'], dionosaurio)
dionosaurio = {'name': "Diplodocus", 'codigo': '512', 'caracter': '3H'}
arbol = arbol_nombre.insertar_nodo(dionosaurio['name'], dionosaurio)
arbol1 = arbol_codigo.insertar_nodo(dionosaurio['codigo'], dionosaurio)
dionosaurio = {'name': "Diplodocus", 'codigo': '534', 'caracter': '3D'}
arbol = arbol_nombre.insertar_nodo(dionosaurio['name'], dionosaurio)
arbol1 = arbol_codigo.insertar_nodo(dionosaurio['codigo'], dionosaurio)
dionosaurio = {'name': "Alosaurio", 'codigo': '334', 'caracter': '7G'}
arbol1 = arbol_nombre.insertar_nodo(dionosaurio['name'], dionosaurio)
arbol1 = arbol_codigo.insertar_nodo(dionosaurio['codigo'], dionosaurio)
dionosaurio = {'name': "T-Rex", 'codigo': '560', 'caracter': '6K'}
arbol = arbol_nombre.insertar_nodo(dionosaurio['name'], dionosaurio)
arbol1 = arbol_codigo.insertar_nodo(dionosaurio['codigo'], dionosaurio)
dionosaurio = {'name': "Raptor", 'codigo': '569', 'caracter': '9H'}
arbol = arbol_nombre.insertar_nodo(dionosaurio['name'], dionosaurio)
arbol1 = arbol_codigo.insertar_nodo(dionosaurio['codigo'], dionosaurio)
dionosaurio = {'name': "Centosauros", 'codigo': '56', 'caracter': '6T'}
arbol = arbol_nombre.insertar_nodo(dionosaurio['name'], dionosaurio)
arbol1 = arbol_codigo.insertar_nodo(dionosaurio['codigo'], dionosaurio)
dionosaurio = {'name': "Velociraptor", 'codigo': '536', 'caracter': '10H'}
arbol = arbol_nombre.insertar_nodo(dionosaurio['name'], dionosaurio)
arbol1 = arbol_codigo.insertar_nodo(dionosaurio['codigo'], dionosaurio)
dionosaurio = {'name': "Triceratop", 'codigo': '156', 'caracter': '5J'}
arbol = arbol_nombre.insertar_nodo(dionosaurio['name'], dionosaurio)
arbol1 = arbol_codigo.insertar_nodo(dionosaurio['codigo'], dionosaurio)
dionosaurio = {'name': "Raptor", 'codigo': '556', 'caracter': '11H'}
arbol = arbol_nombre.insertar_nodo(dionosaurio['name'], dionosaurio)
arbol1 = arbol_codigo.insertar_nodo(dionosaurio['codigo'], dionosaurio)


print('realizar un barrido en orden del árbol ordenado por nombre')
#arbol.inorden()#PUNTO 3
print()
print('mostrar toda la información del dinosaurio 792')
#arbol.mostrar_info_792()
print()
print('mostrar toda la información de todos los T-Rex que hay en la isla')
#arbol.mostrar_info_TRex()
print()
print('modificar el nombre del dinosaurio en Sgimoloch')
#arbol.modificar_donosaurio('Sgimoloch')
print()
print('mostrar la ubicación de todos los Raptores que hay en la isla;')
#arbol.mostrar_ubicacion_Raptors()
print()
print('contar cuantos Diplodocus hay en el parque')
print(arbol.contar_cant_Diploducos())

