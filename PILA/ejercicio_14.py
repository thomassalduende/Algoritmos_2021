from pila import Pila
from random import randint

pila = Pila()
pila_aux = Pila()

#for i in range(0, 10):
 #   num = randint(1, 100)
 #   print(num)
 #   pila_datos.apilar(num)

#while(not pila_datos.pila_vacia()):
 #   x = pila_datos.desapilar()
 #   pila_aux.apilar(x)
#print()
#while (not pila_aux.pila_vacia()):
 #   x = pila_aux.desapilar
  #  if (x % 2 == 0):
   #     pila_datos.apilar(x)
    #    print(x)

#while (not pila_aux.pila_vacia()):
 #   x = pila_aux.desapilar


#Ejercicio 14

numeros = [0, 3, 1, 7, 2]

for i in range(0, len(numeros)):
    num = numeros[i]

    if(pila.pila_vacia()):
         pila.apilar(num)
    else:
        if(num >= pila.elemento_cima()):
             pila.apilar(num)
        else:
            while(not pila.pila_vacia() and pila.elemento_cima() > num):
                pila_aux.apilar(pila.desapilar())
            
            pila.apilar(num)

            while(not pila_aux.pila_vacia()):
                 pila.apilar(pila_aux.desapilar())


while(not pila.pila_vacia()):
    print(pila.desapilar())

#print()
            

    
        
        






    
        
