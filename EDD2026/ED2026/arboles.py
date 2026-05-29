class ArbolBin:
    def __init__(self, izq=None, elem=None, der=None):
        # Si todos son None → nulo
        self._izq = izq
        self._elem = elem
        self._der = der

    # =====================
    # Constructores
    # =====================
    @staticmethod
    def nulo():
        return ArbolBin()

    @staticmethod
    def nodo(izq, elem, der):
        return ArbolBin(izq, elem, der)

    # =====================
    # Selectores
    # =====================
    def izq(self):
        if self.es_nulo():
            raise Exception("error: árbol nulo")
        return self._izq

    def der(self):
        if self.es_nulo():
            raise Exception("error: árbol nulo")
        return self._der

    def elem(self):
        if self.es_nulo():
            raise Exception("error: árbol nulo")
        return self._elem

    # =====================
    # Predicados
    # =====================
    def es_nulo(self):
        return self._elem is None and self._izq is None and self._der is None

    def es_hoja(self):
        if self.es_nulo():
            return False
        return self._izq.es_nulo() and self._der.es_nulo()

    def es_ult(self):
        if self.es_nulo():
            return False
        return self._izq.es_nulo() or self._der.es_nulo()

    def es_completo(self):
        return self.altura() == self.camino_min()

    # =====================
    # Funciones
    # =====================
    def num_nodos(self):
        if self.es_nulo():
            return 0
        return 1 + self._izq.num_nodos() + self._der.num_nodos()

    def altura(self):
        if self.es_nulo():
            return 0
        return 1 + max(self._izq.altura(), self._der.altura())

    def camino_min(self):
        if self.es_nulo():
            return 0
        return 1 + min(self._izq.camino_min(), self._der.camino_min())

    def num_hojas(self):
        if self.es_nulo():
            return 0
        if self._izq.es_nulo() and self._der.es_nulo():
            return 1
        return self._izq.num_hojas() + self._der.num_hojas()

    # =====================
    # Métodos de Recorrido
    # =====================
    def prefijo(self):
        """
        Recorrido en prefijo: raíz, izquierdo, derecho
        Retorna una lista con los elementos en orden de prefijo
        """
        if self.es_nulo():
            return []
        # Raíz, luego izquierdo, luego derecho
        return [self._elem] + self._izq.prefijo() + self._der.prefijo()

    def infijo(self):
        """
        Recorrido en infijo: izquierdo, raíz, derecho
        Retorna una lista con los elementos en orden de infijo
        """
        if self.es_nulo():
            return []
        # Izquierdo, luego raíz, luego derecho
        return self._izq.infijo() + [self._elem] + self._der.infijo()

    def sufijo(self):
        """
        Recorrido en sufijo (posfijo): izquierdo, derecho, raíz
        Retorna una lista con los elementos en orden de sufijo
        """
        if self.es_nulo():
            return []
        # Izquierdo, luego derecho, luego raíz
        return self._izq.sufijo() + self._der.sufijo() + [self._elem]

    # =====================
    # Representación
    # =====================
    def __repr__(self):
        if self.es_nulo():
            return "nulo"
        return f"nodo({self._izq}, {self._elem}, {self._der})"

    def imprimir_arbol(self, prefijo="", es_izq=True):
        if self.es_nulo():
            return

        # Primero derecho (arriba)
        if not self._der.es_nulo():
            self._der.imprimir_arbol(prefijo + ("│   " if es_izq else "    "), False)

        # Nodo actual
        print(prefijo + ("└── " if es_izq else "┌── ") + str(self._elem))

        # Luego izquierdo (abajo)
        if not self._izq.es_nulo():
            self._izq.imprimir_arbol(prefijo + ("    " if es_izq else "│   "), True)


# ============================================
# EJEMPLO DE USO Y CORRIDAS
# ============================================

if __name__ == "__main__":
    n = ArbolBin.nulo()

    arbol = ArbolBin.nodo(
        ArbolBin.nodo(
            ArbolBin.nodo(n, 2, n),   
            8,                        
            n                        
        ),
        3,                            # raíz
        ArbolBin.nodo(
            ArbolBin.nodo(n, 1, n),  
            5,                       
            ArbolBin.nodo(
                ArbolBin.nodo(n, 9, n), 
                6,                    
                n                      
            )
        )
    )

    print("=" * 60)
    print("Árbol Binario")
    print("=" * 60)
    print("\nEstructura del árbol:")
    arbol.imprimir_arbol()
    
    print("\n" + "=" * 60)
    print("Recorridos del Árbol")
    print("=" * 60)
    
    # Recorrido en prefijo
    print("\n1. Prefijo:")
    print(f"   {arbol.prefijo()}")
    
    # Recorrido en infijo
    print("\n2. Infijo:")
    print(f"   {arbol.infijo()}")
    
    # Recorrido en sufijo
    print("\n3. Sufijo:")
    print(f"   {arbol.sufijo()}")