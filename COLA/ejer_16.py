from heap import HeapMax



h = HeapMax()

h.arribo('Thomas', 1)
h.arribo('Victoria', 1)
h.arribo('Valentin', 1)

print('el primer documento de la cola')

print(h.atencion()[0:2])

h.arribo('Guadalupe', 2)
h.arribo('Claudia', 2)
h.arribo('Emiliano', 3)

print('dos primeros documentos de la cola')
for i in range (2):
    print(h.atencion()[0:2])

h.arribo('Mayra', 1)
h.arribo('Josefina', 1)
h.arribo('Luisana', 3)

print('todos los documentos de la cola')

for i in range(h.tamanio):
    print(h.atencion()[0:2])