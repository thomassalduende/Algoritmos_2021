from arbol_binario_thomi import Arbol

arbol = Arbol()
arbol_superheroes = Arbol()
arbol_villanos = Arbol()


#def cargar_teclado():
#    for i in range (2):
#        info = input("ingrese nombre: ")
#        super = input("es super heroe: ")

 #       arbol.insertar_nodo (info, super)

#cargar_teclado()


#def cargar(arbol):

superheroes = {'name': "Doctor Strange", 'superheroe': True}
arbol = arbol.insertar_nodo(superheroes['name'], superheroes)
superheroes = {'name': "Hulk", 'superheroe': False}
arbol = arbol.insertar_nodo(superheroes['name'], superheroes)
superheroes = {'name': "Iron Man", 'superheroe': True}
arbol = arbol.insertar_nodo(superheroes['name'], superheroes)
superheroes = {'name': "Super-Man", 'superheroe': False}
arbol = arbol.insertar_nodo(superheroes['name'], superheroes)
superheroes = {'name': "Spider-Man", 'superheroe': True}
arbol = arbol.insertar_nodo(superheroes['name'], superheroes)
superheroes = {'name': "Caperucita", 'superheroe': True}
arbol = arbol.insertar_nodo(superheroes['name'], superheroes)
superheroes = {'name': "Caballo", 'superheroe': False}
arbol = arbol.insertar_nodo(superheroes['name'], superheroes)






#cargar(arbol)
print('listar los villanos ordenados alfabéticamente')
arbol.inorden() #PUNTO B
print()
print('mostrar todos los superhéroes que empiezan con C')
arbol.empiezan_C()#PUNTO C
print()
print('determinar cuántos superhéroes hay el árbol')
print("La cantidad de superheroes es: ", arbol.cant_super())#PUNTO D  
print()
print('Modificar nombre de Doctor Strange')
#arbol.mod_nombre()#PUNTO E
print()
print('determinar cuántos superhéroes hay el árbol')
arbol.postorden()#PUNTO F 
print()
print('Generar un arbol donde separe los villanos y superheroes')
arbol.arboles(arbol_superheroes, arbol_villanos)#PUNTO G
print()
print('listado de villanos')
arbol.inorden_villanos()
print()
print('listado de superheroes')
arbol.inorden_super()


#arbol.inorden()

#    def inorden_villanos(self):
#        if(self.info is not None):
#            if (self.datos['superheroe']== False):
#                print(self.info)
#            if(self.izq is not None):
#                self.izq.inorden_villanos()
#            if(self.der is not None):
#                self.der.inorden_villanos()

#    def inorden_super(self):
#        if(self.info is not None):
#            if (self.datos['superheroe'] == True):
#                print(self.info)
#            if(self.izq is not None):
#                self.izq.inorden_super()
#            if(self.der is not None):
#                self.der.inorden_super()


#    def arboles(self, arbol_superheroes, arbol_villanos):
#        if(self.info is not None):
#                if(self.datos['superheroe'] == True):
#                    arbol_superheroes = arbol_superheroes.insertar_nodo(self.info, self.datos)
#                else:
#                    arbol_villanos = arbol_villanos.insertar_nodo(self.info, self.datos)
#                if(self.izq is not None):
#                    self.izq.arboles(arbol_superheroes, arbol_villanos)
#                if(self.der is not None):
#                    self.der.arboles(arbol_superheroes, arbol_villanos)


#   def empiezan_C(self):
#        if (self.info is not None):
#            if(self.datos['superheroe'] == True):
#                if(self.info[0]== 'C'):
#                    print(self.datos['name'], "empieza con C y es superheroe")
#            if(self.izq is not None):
#                self.izq.empiezan_C() 
#            if(self.der is not None):
#                self.der.empiezan_C()
        
                     
#    def cant_super(self):
#        cant = 0
#        if(self.info is not None):
#            if(self.datos['superheroe']== True):
#                cant +=1
#            if(self.izq is not None):
#                cant += self.izq.cant_super()
#            if(self.der is not None):
#                cant += self.der.cant_super()     
#        return cant

