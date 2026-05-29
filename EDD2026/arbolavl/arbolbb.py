from arbolbin import ArbolBin

class ArbolBB(ArbolBin):

    @staticmethod
    def nulo():
        return ArbolBB()

    @staticmethod
    def nodo(izq, elem, der):
        return ArbolBB(izq, elem, der)

    def insertar(self, e):
        if self.es_nulo():
            return ArbolBB.nodo(ArbolBB.nulo(), e, ArbolBB.nulo())

        if e < self._elem:
            return ArbolBB.nodo(self._izq.insertar(e), self._elem, self._der)
        elif self._elem < e:
            return ArbolBB.nodo(self._izq, self._elem, self._der.insertar(e))
        else:
            return self

    def minimo(self):
        if self._izq.es_nulo():
            return self._elem
        return self._izq.minimo()

    def maximo(self):
        if self._der.es_nulo():
            return self._elem
        return self._der.maximo()

    def sustraer(self, e):
        if self.es_nulo():
            return self

        if e < self._elem:
            return ArbolBB.nodo(self._izq.sustraer(e), self._elem, self._der)

        elif self._elem < e:
            return ArbolBB.nodo(self._izq, self._elem, self._der.sustraer(e))

        else:
            if self._izq.es_nulo() and self._der.es_nulo():
                return ArbolBB.nulo()

            if self._izq.es_nulo():
                return self._der

            if self._der.es_nulo():
                return self._izq

            max_izq = self._izq.maximo()

            return ArbolBB.nodo(
                self._izq.sustraer(max_izq),
                max_izq,
                self._der
            )