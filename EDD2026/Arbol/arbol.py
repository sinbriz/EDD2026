class ArbolBin:
    def __init__(self, izq=None, elem=None, der=None):
        """Constructor nodo: recibe subárbol izquierdo, elemento, subárbol derecho"""
        self.izq = izq
        self.elem = elem
        self.der = der

    @classmethod
    def nulo(cls):
        """Constructor del árbol vacío"""
        return cls(None, None, None)

    def es_nulo(self):
        return self.elem is None

    def es_hoja(self):
        if self.es_nulo():
            return False
        return self.izq is None and self.der is None

    def es_ult(self):
        """Es último? (al menos un hijo es nulo)"""
        if self.es_nulo():
            return False
        return self.izq is None or self.der is None

    def num_nodos(self):
        if self.es_nulo():
            return 0
        izquierda = self.izq.num_nodos() if self.izq else 0
        derecha = self.der.num_nodos() if self.der else 0
        return 1 + izquierda + derecha

    def altura(self):
        if self.es_nulo():
            return 0
        izquierda = self.izq.altura() if self.izq else 0
        derecha = self.der.altura() if self.der else 0
        return 1 + max(izquierda, derecha)

    def camino_min(self):
        if self.es_nulo():
            return 0
        izquierda = self.izq.camino_min() if self.izq else 0
        derecha = self.der.camino_min() if self.der else 0
        return 1 + min(izquierda, derecha)

    def es_completo(self):
        return self.altura() == self.camino_min()

    def num_hojas(self):
        if self.es_nulo():
            return 0
        if self.es_hoja():
            return 1
        izquierda = self.izq.num_hojas() if self.izq else 0
        derecha = self.der.num_hojas() if self.der else 0
        return izquierda + derecha

    def preorden(self):
        """Recorrido en preorden (mostrando nulos)"""
        if self.es_nulo():
            return ["null"]
        resultado = [self.elem]
        if self.izq:
            resultado += self.izq.preorden()
        else:
            resultado += ["null"]
        if self.der:
            resultado += self.der.preorden()
        else:
            resultado += ["null"]
        return resultado


# Construcción del árbol usando la expresión algebraica:
# nodo(nodo(nodo(nulo,2,nulo),8,nulo),3,nodo(nodo(nulo,1,nulo),5,nodo(nodo(nulo,9,nulo),6,nulo)))

nulo = ArbolBin.nulo()

# Construcción desde abajo hacia arriba
nodo2 = ArbolBin(nulo, 2, nulo)
nodo8 = ArbolBin(nodo2, 8, nulo)

nodo9 = ArbolBin(nulo, 9, nulo)
nodo1 = ArbolBin(nulo, 1, nulo)
nodo6 = ArbolBin(nodo9, 6, nulo)
nodo5 = ArbolBin(nodo1, 5, nodo6)

arbol = ArbolBin(nodo8, 3, nodo5)

# Demostración
print("=== ÁRBOL BINARIO ===")
print("Preorden:", arbol.preorden())
print("¿Es nulo?", arbol.es_nulo())
print("Número de nodos:", arbol.num_nodos())
print("Número de hojas:", arbol.num_hojas())
print("Altura:", arbol.altura())
print("Camino mínimo:", arbol.camino_min())
print("¿Es completo?", arbol.es_completo())
print("¿Es último? (raíz):", arbol.es_ult())