from arbolbb import ArbolBB

class ArbolAVL(ArbolBB):

    @staticmethod
    def nulo():
        return ArbolAVL()

    @staticmethod
    def nodo(izq, elem, der):
        return ArbolAVL(izq, elem, der)

    def balance(self):
        if self.es_nulo():
            return 0
        return self._izq.altura() - self._der.altura()

    def rotar_izq(self):
        if self.es_nulo() or self._der.es_nulo():
            return self

        nuevo = self._der

        return ArbolAVL.nodo(
            ArbolAVL.nodo(self._izq, self._elem, nuevo._izq),
            nuevo._elem,
            nuevo._der
        )

    def rotar_der(self):
        if self.es_nulo() or self._izq.es_nulo():
            return self

        nuevo = self._izq

        return ArbolAVL.nodo(
            nuevo._izq,
            nuevo._elem,
            ArbolAVL.nodo(nuevo._der, self._elem, self._der)
        )

    def balancear(self):
        if self.es_nulo():
            return self

        fb = self.balance()

        if fb > 1:
            if self._izq.balance() < 0:
                return ArbolAVL.nodo(
                    self._izq.rotar_izq(),
                    self._elem,
                    self._der
                ).rotar_der()
            return self.rotar_der()

        if fb < -1:
            if self._der.balance() > 0:
                return ArbolAVL.nodo(
                    self._izq,
                    self._elem,
                    self._der.rotar_der()
                ).rotar_izq()
            return self.rotar_izq()

        return self

    def insertar(self, e):
        if self.es_nulo():
            return ArbolAVL.nodo(ArbolAVL.nulo(), e, ArbolAVL.nulo())

        if e < self._elem:
            nuevo = ArbolAVL.nodo(self._izq.insertar(e), self._elem, self._der)
        elif self._elem < e:
            nuevo = ArbolAVL.nodo(self._izq, self._elem, self._der.insertar(e))
        else:
            return self

        return nuevo.balancear()

    def sustraer(self, e):
        if self.es_nulo():
            return self

        if e < self._elem:
            nuevo = ArbolAVL.nodo(self._izq.sustraer(e), self._elem, self._der)

        elif self._elem < e:
            nuevo = ArbolAVL.nodo(self._izq, self._elem, self._der.sustraer(e))

        else:
            if self._izq.es_nulo() and self._der.es_nulo():
                return ArbolAVL.nulo()

            if self._izq.es_nulo():
                return self._der

            if self._der.es_nulo():
                return self._izq

            max_izq = self._izq.maximo()

            nuevo = ArbolAVL.nodo(
                self._izq.sustraer(max_izq),
                max_izq,
                self._der
            )

        return nuevo.balancear()

if __name__ == "__main__":
    avl = ArbolAVL.nulo()

    for x in [10, 20, 30, 40, 50, 25]:
        avl = avl.insertar(x)

    avl.imprimir_arbol()