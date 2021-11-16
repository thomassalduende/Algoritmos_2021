from cola import Cola


class Arbol(object):

    def __init__(self, info=None, datos=None, frecuencia= None):
        self.info = info
        self.datos = datos
        self.frecuencia = frecuencia
        self.der = None
        self.izq = None
        self._altura = 0

    def arbol_vacio(self):
        return self.info is None
    
    def altura(self, arbol):
        if(arbol is None):
            return -1
        else:
            return arbol._altura

    def actualizar_altura(self):
        if(self is not None):
            altura_izq = self.altura(self.izq)
            altura_der = self.altura(self.der)
            self._altura = (altura_izq if altura_izq > altura_der else altura_der) + 1
    
    def rotacion_simple(self, control):
        if(control):
            aux = self.izq
            self.izq = aux.der
            aux.der = self
        else:
            aux = self.der
            self.der = aux.izq
            aux.izq = self
        self.actualizar_altura()
        aux.actualizar_altura()
        return aux

    def rotacion_doble(self, control):
        if(control):
            self.izq = self.izq.rotacion_simple(False)
            self = self.rotacion_simple(True)
        else:
            self. der = self.der.rotacion_simple(True)
            self = self.rotacion_simple(False)
        return self

    def balancear(self):
        if(self is not None):
            if(self.altura(self.izq)-self.altura(self.der) == 2):
                if(self.altura(self.izq.izq) >= self.altura(self.izq.der)):
                    self = self.rotacion_simple(True)
                else:
                    self = self.rotacion_doble(True)
            elif(self.altura(self.der)-self.altura(self.izq) == 2):
                if(self.altura(self.der.der) >= self.altura(self.der.izq)):
                    self = self.rotacion_simple(False)
                else:
                    self = self.rotacion_doble(False)
        return self

    def insertar_nodo(self, dato, datos=None):
        if(self.info is None):
            self.info = dato
            self.datos = datos
        elif(dato < self.info):
            if(self.izq is None):
                self.izq = Arbol(dato, datos)
            else:
                self.izq = self.izq.insertar_nodo(dato, datos)
        else:
            if(self.der is None):
                self.der = Arbol(dato, datos)
            else:
                self.der = self.der.insertar_nodo(dato, datos)
        self = self.balancear()
        self.actualizar_altura()
        return self

    def inorden(self):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.inorden()
            print(self.info, self.datos)
            if(self.der is not None):
                self.der.inorden()

    def postorden(self):
        if(self.info is not None):
            if(self.der is not None):
                self.der.postorden()
            print(self.info)
            if(self.izq is not None):
                self.izq.postorden()

    def preorden(self):
        if(self.info is not None):
            print(self.info, self._altura)
            if(self.izq is not None):
                self.izq.preorden()
            if(self.der is not None):
                self.der.preorden()

    def busqueda(self, clave):
        pos = None
        if(self.info is not None):
            if(self.info == clave):
                pos = self
            elif(clave < self.info and self.izq is not None):
                pos = self.izq.busqueda(clave)
            elif(self.der is not None):
                pos = self.der.busqueda(clave)
        return pos
    
    def busqueda_proximidad(self, clave):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.busqueda_proximidad(clave)
            if(self.info[0:len(clave)] == clave):
                print(self.info)
            if(self.der is not None):
                self.der.busqueda_proximidad(clave)

    def remplazar(self):
        """Determina el nodo que remplazará al que se elimina."""
        info, datos = None, None
        if(self.der is None):
            info = self.info
            datos = self.datos
            if(self.izq is not None):
                self.info = self.izq.info
                self.der = self.izq.der
                self.izq = self.izq.izq
                self.datos = self.izq.datos
            else:
                self.info = None
                self.datos = None
        else:
            info, datos = self.der.remplazar()
        return info, datos

    def eliminar_nodo(self, clave):
        """Elimina un elemento del árbol y lo devuelve si lo encuentra."""
        info, datos = None, None
        if(self.info is not None):
            if(clave < self.info):
                if(self.izq is not None):
                    info, datos = self.izq.eliminar_nodo(clave)
            elif(clave > self.info):
                if(self.der is not None):
                    info, datos = self.der.eliminar_nodo(clave)
            else:
                info = self.info
                datos = self.datos
                if(self.der is None and self.izq is None):
                    self.info = None
                    self.datos = None
                elif(self.izq is None):
                    self.info = self.der.info
                    self.izq = self.der.izq
                    self.der = self.der.der
                    self.datos = self.datos
                elif(self.der is None):
                    self.info = self.izq.info
                    self.der = self.izq.der
                    self.izq = self.izq.izq
                    self.datos = self.datos
                else:
                    info_aux, datos_aux = self.izq.remplazar()
                    self.info = info_aux
                    self.datos = datos_aux
                    # raiz.info, raiz.nrr = aux.info, aux.nrr
        # self = self.balancear()
        self.actualizar_altura()
        return info, datos
    
    def contar_ocurrencias(self, buscado):
        cantidad = 0
        if(self.info is not None):
            if(self.info == buscado):
                cantidad += 1
            if(self.izq is not None):
                cantidad += self.izq.contar_ocurrencias(buscado)
            if(self.der is not None):
                cantidad += self.der.contar_ocurrencias(buscado)
        return cantidad
    
    def contar_pares_impares(self):
        pares, impares = 0, 0
        if(self.info is not None):
            if(self.info % 2 == 0):
                pares += 1
            else:
                impares += 1
            if(self.izq is not None):
                par, impar = self.izq.contar_pares_impares()
                pares += par
                impares += impar
            if(self.der is not None):
                par, impar = self.der.contar_pares_impares()
                pares += par
                impares += impar
        return pares, impares

    def barrido_por_nivel(self):
        pendientes = Cola()
        pendientes.arribo(self)
        while(not pendientes.cola_vacia()):
            nodo = pendientes.atencion()
            print(nodo.info)
            if(nodo.izq is not None):
                pendientes.arribo(nodo.izq)
            if(nodo.der is not None):
                pendientes.arribo(nodo.der)    

    def barrido_por_nivel_huff(self):
        pendientes = Cola()
        pendientes.arribo(self)
        while(not pendientes.cola_vacia()):
            nodo = pendientes.atencion()
            print(nodo.info, nodo.frecuencia)
            if(nodo.izq is not None):
                pendientes.arribo(nodo.izq)
            if(nodo.der is not None):
                pendientes.arribo(nodo.der)



    def empiezan_C(self):
        if (self.info is not None):
            if(self.datos['superheroe'] == True):
                if(self.info[0]== 'C'):
                    print(self.datos['name'], "empieza con C y es superheroe")
            if(self.izq is not None):
                self.izq.empiezan_C() 
            if(self.der is not None):
                self.der.empiezan_C()
        
                     
    def cant_super(self):
        cant = 0
        if(self.info is not None):
            if(self.datos['superheroe']== True):
                cant +=1
            if(self.izq is not None):
                cant += self.izq.cant_super()
            if(self.der is not None):
                cant += self.der.cant_super()     
        return cant

    def mod_nombre(self):
        self.inorden()
        buscado = input('ingrese lo que desa buscar ')
        self.busqueda_proximidad(buscado)
        print()
        buscado = input('ingrese el nombre que desea modificar ')
        pos = self.busqueda(buscado)
        if(pos):
            nuevo_nombre = input('ingrese el nuevo nombre ')
            nombre, superheroe = self.eliminar_nodo(buscado)
            superheroe['name'] = nuevo_nombre
            arbol = self.insertar_nodo(nuevo_nombre, superheroe)
            print()
            arbol.inorden()

    def arboles(self, arbol_superheroes, arbol_villanos):
        if(self.info is not None):
                if(self.datos['superheroe'] == True):
                    arbol_superheroes = arbol_superheroes.insertar_nodo(self.info, self.datos)
                else:
                    arbol_villanos = arbol_villanos.insertar_nodo(self.info, self.datos)
                if(self.izq is not None):
                    self.izq.arboles(arbol_superheroes, arbol_villanos)
                if(self.der is not None):
                    self.der.arboles(arbol_superheroes, arbol_villanos)
    
    def inorden_villanos(self):
        if(self.info is not None):
            if (self.datos['superheroe']== False):
                print(self.info)
            if(self.izq is not None):
                self.izq.inorden_villanos()
            if(self.der is not None):
                self.der.inorden_villanos()

    def inorden_super(self):
        if(self.info is not None):
            if (self.datos['superheroe'] == True):
                print(self.info)
            if(self.izq is not None):
                self.izq.inorden_super()
            if(self.der is not None):
                self.der.inorden_super()
    
    def cantidad_nodos(self):
        cant_super = 0
        cant_vill = 0
        if(self.info is not None):
            if (self.datos['superheroe'] == True):
                cant_super +=1
            else:
                cant_vill +=1
            if(self.izq is not None):
                self.izq.cantidad_nodos()
            if(self.der is not None):
                self.der.cantidad_nodos()
        return cant_vill, cant_super
    

    def inorden_criaturas(self):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.inorden_criaturas()
            print(self.info, self.datos)
            if(self.der is not None):
                self.der.inorden_criaturas()    

    def mostrar_Talos(self):
        if(self.info is not None):
            if(self.datos['name'] == "Talos"):
                print(self.info, self.datos)
            if(self.izq is not None):
                self.izq.mostrar_Talos()
            if(self.der is not None):
                self.der.mostrar_Talos()


    def derrotados_heracles(self):
        if(self.info is not None):
            if (self.datos['derrotado'] == "Heracles"):
                print(self.info)
            if(self.izq is not None):
                self.izq.derrotados_heracles()
            if(self.der is not None):
                self.der.derrotados_heracles()  

    def no_derrotados(self):
        if(self.info is not None):
            if(self.datos['derrotado'] == "-"):
                print(self.info)
            if(self.izq is not None):
                self.izq.no_derrotados()
            if(self.der is not None):
                self.der.no_derrotados() 

    
    def mod_nombre_criatura(self):
        self.inorden()
        buscado = input('ingrese lo que desa buscar ')
        self.busqueda_proximidad(buscado)
        print()
        buscado = input('ingrese el nombre que desea modificar ')
        pos = self.busqueda(buscado)
        if(pos):
            nuevo_nombre = input('ingrese el nuevo nombre ')
            nombre, criatura = self.eliminar_nodo(buscado)
            criatura['name'] = nuevo_nombre
            arbol = self.insertar_nodo(nuevo_nombre, criatura)
            print()
            arbol.inorden()

    def capturas_heracles(self):
        if(self.info is not None):
            if (self.datos['capturada'] == "Heracles"):
                print(self.info)
            if(self.izq is not None):
                self.izq.capturas_heracles()
            if(self.der is not None):
                self.der.capturas_heracles() 
    
    def mod_atrapar_criatura(self):
        self.inorden()
        buscado = input('ingrese lo que desea buscar: ')
        self.busqueda_proximidad(buscado)
        print()
        buscado = input('ingrese el nombre que desea modificar: ')
        pos = self.busqueda(buscado)
        if(pos):
            nueva_criatura = input('ingrese el nuevo nombre que lo atrapó:  ')
            nombre, criatura = self.eliminar_nodo(buscado)
            criatura['atrapada'] = nueva_criatura
            arbol = self.insertar_nodo(nombre, nueva_criatura)
            print()
            arbol.inorden()

    def eliminar_Sirena_Basilisco(self):
        self.eliminar_nodo('Las Sirenas')
        self.eliminar_nodo('Basilisco')

        self.inorden()

        

    def cargar_descripcion(self): #PUNTO B EJER 23

        if( self.info is not None):
            #nodo=descripciones.atencion()
            print(self.info, self.datos)
            self.datos['descripcion'] = input('Cargar una brebe descripcion de la criatura: ')
            if(self.izq is not None):
                self.der.cargar_descripcion()
            if(self.der is not None):
                self.der.cargar_descripcion()
                
        self.inorden()

    def contar_heroes(self, dic):#PUNTO D EJER 23
        if(self.info is not None):
            if(self.datos['derrotado'] and self.datos['derrotado'] in dic):
                dic[self.datos['derrotado']]+= 1
            elif(self.datos['derrotado'] and self.datos['derrotado'] not in dic):
                dic[self.datos['derrotado']] = 1
            if(self.izq is not None):
                self.izq.contar_heroes(dic) 
            if(self.der is not None):
                self.der.contar_heroes(dic) 


    def modificar_atrapados_Aves(self, criaturas):
        self.inorden()
        print()
        buscado = criaturas
        pos = self.busqueda(buscado)
        if(pos):
            nombre, nuevos_Datos = self.eliminar_nodo(criaturas)
            nuevos_Datos['derrotado'] = 'Heracles'
            nuevos_Datos['capturada'] = 'varias'
            arbol= self.insertar_nodo(nombre, nuevos_Datos)
            print()
            arbol.inorden()



#SEGUNDO PARCIAL

    def mostrar_info_792(self):
        if(self.info is not None):
            if(self.datos['codigo'] == '792'):
                print(self.info, self.datos)
            if(self.izq is not None):
                self.izq.mostrar_info_792()
            if(self.der is not None):
                self.der.mostrar_info_792() 

    def mostrar_info_TRex(self):
        if (self.info is not None):
            if (self.datos['name'] == 'T-Rex'):
                print(self.info, self.datos)
            if(self.izq is not None):
                self.izq.mostrar_info_TRex()
            if(self.der is not None):
                self.der.mostrar_info_TRex()


    def modificar_donosaurio(self, dino):
        self.inorden()
        print()
        buscado = dino
        pos = self.busqueda(buscado)
        if(pos):
            nuevo_nombre = 'Stygimoloch'
            nombre, dionosaurio = self.eliminar_nodo(buscado)
            dionosaurio['name'] = nuevo_nombre
            arbol = self.insertar_nodo(nuevo_nombre, dionosaurio)
            print()
            arbol.inorden()


    def mostrar_ubicacion_Raptors(self):
        if (self.info is not None):
            if (self.datos['name'] == 'Raptor'):
                print(self.info, self.datos['caracter'])
            if(self.izq is not None):
                self.izq.mostrar_ubicacion_Raptors()
            if(self.der is not None):
                self.der.mostrar_ubicacion_Raptors()

    def contar_cant_Diploducos(self):
        cantidad = 0 
        if (self.info is not None):
            if (self.datos['name'] == "Diplodocus"):
                cantidad +=1
            if(self.izq is not None):
                cantidad+= self.izq.contar_cant_Diploducos()
            if(self.der is not None):
                 cantidad+=self.der.contar_cant_Diploducos()
        return cantidad

