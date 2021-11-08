from arbol_binario_thomi import Arbol
from lista import Lista 

arbol = Arbol()

criaturas = {'name': 'Basiliscos', 'derrotado':'Zeus', 'descripcion':'', 'capturada': ''}
arbol = arbol.insertar_nodo(criaturas['name'], criaturas)
criaturas = {'name': 'Tifon', 'derrotado':'Zeus', 'descripcion':'', 'capturada': ''}
arbol = arbol.insertar_nodo(criaturas['name'], criaturas)
criaturas = {'name': 'Tifon', 'derrotado':'Argos Panoptes', 'descripcion':'', 'capturada': ''}
arbol = arbol.insertar_nodo(criaturas['name'], criaturas)
criaturas = {'name': 'Dino', 'derrotado':'', 'descripcion':'', 'capturada': ''}
arbol = arbol.insertar_nodo(criaturas['name'], criaturas)
criaturas = {'name': 'Pefredo', 'derrotado':'Zeus', 'descripcion':'', 'capturada': ''}
arbol = arbol.insertar_nodo(criaturas['name'], criaturas)
criaturas = {'name': 'Enio', 'derrotado':'Heracles', 'descripcion':'', 'capturada': ''}
arbol = arbol.insertar_nodo(criaturas['name'], criaturas)
criaturas = {'name': 'Medusa', 'derrotado':'Heracles', 'descripcion':'', 'capturada': ''}
arbol = arbol.insertar_nodo(criaturas['name'], criaturas)
criaturas = {'name': 'Aves del Estinfalo', 'derrotado':'', 'descripcion':'', 'capturada': ''}
arbol = arbol.insertar_nodo(criaturas['name'], criaturas)
criaturas = {'name': 'Ladon', 'derrotado':'Zeus', 'descripcion':'', 'capturada': 'Heracles'}
arbol = arbol.insertar_nodo(criaturas['name'], criaturas)


#arbol.inorden_criaturas() #PUNTO A
print()
#arbol.cargar_descripcion()#PUNTO B
print()
#arbol.mostrar_Talos() #PUNTO C
dic = {}
arbol.contar_heroes(dic)
def ordenar(item):
    return item[1]
lista = list(dic.items())
lista.sort(key=ordenar, reverse=True)
for elemento in lista:
    print(elemento)
print()
#arbol.derrotados_heracles()#PUNTO E
print()
#arbol.no_derrotados()#PUNTO F
print()
#arbol.mod_atrapar_criatura()#PUNTO H
print()
#arbol.eliminar_Sirena_Basilisco()#PUNTO J
print()
arbol.modificar_atrapados_Aves('Aves del Estinfalo')
print()
#arbol.mod_nombre_criatura()#PUNTO L
print()
#arbol.barrido_por_nivel()#PUNTO M
print()
#arbol.capturas_heracles() #PUNTO N
print()







