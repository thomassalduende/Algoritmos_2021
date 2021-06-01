from pila import Pila
from random import randint

pila_cazarec1 = Pila()
pila_cazarec2 = Pila()
pila_aux_1 = Pila()
pila_aux_2 = Pila()

class Bitacoras(object):
    def __init__(self,planeta_visitado, captura, recompensa):
        self.planeta_visitado = planeta_visitado
        self.captura = captura
        self.recompensa = recompensa
    
    def __str__(self):
        return self.planeta_visitado+' - '+self.captura+' - '+self.recompensa



print('BOB FETT')
for i in range (0, 2):
    planeta_visitado = input('ingrese planeta visitado ')
    captura = input('ingrese a quien capturo ')
    recompensa = float(input('ingrese recompensa '))
    bitacoras = Bitacoras(planeta_visitado, captura, recompensa)
    pila_cazarec1.apilar(bitacoras)    
    
print('DIN DJARIN')
for i in range (0, 2):
    planeta_visitado = input('ingrese planeta visitado ')
    captura = input('ingrese a quien capturo ')
    recompensa = float(input('ingrese recompensa '))
    bitacoras = Bitacoras(planeta_visitado, captura, recompensa)
    pila_cazarec2.apilar(bitacoras)



#punto b
acu1 = 0
acu2 = 0
cont_1 = 0
cont_2 = 0
for i in range (0,2):
    x = pila_cazarec1.desapilar()
    x2 = pila_cazarec2.desapilar()

    acu1 = acu1 + x.recompensa
    acu2 = acu2 + x2.recompensa 

    cont_1 +=1
    cont_2 +=1

    pila_aux_1.apilar(x)
    pila_aux_2.apilar(x2)
if (acu1>acu2):
    print('Bob Fett obtuvo mayor recompensa que Din Djarin')
else:
    print('Din Djarin obtuvo mayor recompensa que Bob Fett')

print('El total de dinero que recaudo Bob Fett es: $', acu1)
print('El total de dinero que recaudo Din Djarin es: $', acu2)
#punto d
print('La cantidad de capturas que realizó BOB FETT  es: ',cont_1)
print('La cantidad de capturas que realizó DIN DJARIN es: ',cont_2)

#punto c
for i in range(1, pila_aux_1.tamanio()):
    x = pila_aux_1.desapilar()
    if (x.captura=='Han Solo'):
        print('Bob Fett capturo a Han Solo en la mision: ',i)
    pila_cazarec1.apilar(x)
    pila_cazarec2.apilar(x2)

#punto a
while(not pila_cazarec1.pila_vacia()):
    pila_aux_c1.apilar(pila_cazarec1.desapilar()) #Muestra en orden, ya que estan cargados ordenados por lugar visitado
    
print('LUGARES VISITADOS POR BOB FETT')  

while (not pila_aux_c1.pila_vacia()):
    x = pila_aux_c1.desapilar()
    print(x.planeta_visitado)

while(not pila_cazarec2.pila_vacia()):
    pila_aux_2.apilar(pila_cazarec2.desapilar())

print('LUGARES VISITADOS POR DIN DJARIN')

while(not pila_aux_2.pila_vacia()):
    x = pila_aux_2.desapilar()
    print(x.planeta_visitado)



    