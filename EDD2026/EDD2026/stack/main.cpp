#include <nanobind/nanobind.h>
#include <nanobind/stl/string.h>
#include <nanobind/stl/optional.h>
#include <sstream>
#include <exception>

// Incluir tu implementación de pila
#include "stack.hpp"

namespace nb = nanobind;

// Clase wrapper para manejar la plantilla y crear una interfaz amigable para Python
template<typename T>
class StackPython {
private:
    ed::Stack<T> stack;

public:
    StackPython() = default;

    void push(T elem) {
        stack.push(elem);
    }

    bool esta_vacia() const {
        return stack.isEmpty();
    }

    nb::object top() {
        try {
            T valor = stack.top();
            return nb::cast(valor);
        } catch (const std::underflow_error& e) {
            PyErr_SetString(PyExc_IndexError, e.what());
            return nb::object();
        }
    }

    void pop() {
        try {
            stack.pop();
        } catch (const std::underflow_error& e) {
            PyErr_SetString(PyExc_IndexError, e.what());
            throw nb::python_error();
        }
    }

    int tamano() const {
        return stack.getSize();
    }

    std::string a_string() const {
        std::ostringstream oss;
        oss << stack;
        return oss.str();
    }
};

// Módulo principal para Python
NB_MODULE(main, m) {
    m.doc() = "Implementación de Pila (Stack) del proyecto ListLS con bindings para Python";

    // Bind para pila de enteros
    nb::class_<StackPython<int>>(m, "StackEnteros")
        .def(nb::init<>())
        .def("push", &StackPython<int>::push,
             "Agrega un elemento al tope de la pila")
        .def("pop", &StackPython<int>::pop,
             "Elimina el elemento del tope de la pila")
        .def("top", &StackPython<int>::top,
             "Obtiene el elemento del tope de la pila sin eliminarlo")
        .def("esta_vacia", &StackPython<int>::esta_vacia,
             "Verifica si la pila está vacía")
        .def("tamano", &StackPython<int>::tamano,
             "Obtiene el numero de elementos en la pila")
        .def("__str__", &StackPython<int>::a_string)
        .def("__repr__", &StackPython<int>::a_string)
        .def("__len__", &StackPython<int>::tamano)
        .def("__bool__", [](const StackPython<int>& s) {
            return !s.esta_vacia();
        });

    // Bind para pila de números decimales (double)
    nb::class_<StackPython<double>>(m, "StackDecimales")
        .def(nb::init<>())
        .def("push", &StackPython<double>::push)
        .def("pop", &StackPython<double>::pop)
        .def("top", &StackPython<double>::top)
        .def("esta_vacia", &StackPython<double>::esta_vacia)
        .def("tamano", &StackPython<double>::tamano)
        .def("__str__", &StackPython<double>::a_string)
        .def("__repr__", &StackPython<double>::a_string)
        .def("__len__", &StackPython<double>::tamano)
        .def("__bool__", [](const StackPython<double>& s) {
            return !s.esta_vacia();
        });

    // Bind para pila de cadenas de texto
    nb::class_<StackPython<std::string>>(m, "StackCadenas")
        .def(nb::init<>())
        .def("push", &StackPython<std::string>::push)
        .def("pop", &StackPython<std::string>::pop)
        .def("top", &StackPython<std::string>::top)
        .def("esta_vacia", &StackPython<std::string>::esta_vacia)
        .def("tamano", &StackPython<std::string>::tamano)
        .def("__str__", &StackPython<std::string>::a_string)
        .def("__repr__", &StackPython<std::string>::a_string)
        .def("__len__", &StackPython<std::string>::tamano)
        .def("__bool__", [](const StackPython<std::string>& s) {
            return !s.esta_vacia();
        });
}
