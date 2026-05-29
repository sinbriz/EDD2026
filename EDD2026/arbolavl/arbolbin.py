class ArbolBin:
    def __init__(self, izq=None, elem=None, der=None):
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
    # Predicados
    # =====================
    def es_nulo(self):
        return self._elem is None and self._izq is None and self._der is None

    # =====================
    # Funciones
    # =====================
    def altura(self):
        if self.es_nulo():
            return 0
        return 1 + max(self._izq.altura(), self._der.altura())

    def imprimir_arbol(self, prefijo="", es_izq=True):
        if self.es_nulo():
            return

        if not self._der.es_nulo():
            self._der.imprimir_arbol(prefijo + ("│   " if es_izq else "    "), False)

        print(prefijo + ("└── " if es_izq else "┌── ") + str(self._elem))

        if not self._izq.es_nulo():
            self._izq.imprimir_arbol(prefijo + ("    " if es_izq else "│   "), True)


# 🔒 IMPORTANTE: solo se ejecuta si corres este archivo
if __name__ == "__main__":
    n = ArbolBin.nulo()

    arbol = ArbolBin.nodo(
        ArbolBin.nodo(ArbolBin.nodo(n, 2, n), 8, n),
        3,
        ArbolBin.nodo(
            ArbolBin.nodo(n, 1, n),
            5,
            ArbolBin.nodo(ArbolBin.nodo(n, 9, n), 6, n)
        )
    )

    arbol.imprimir_arbol()