#include <nanobind/nanobind.h>
#include <nanobind/stl/string.h>
#include <iostream>
#include <string>
#include <sstream>
#include "array.h"

namespace nb = nanobind;

template <typename T>
void bind_array(nb::module_ &m, const char *name) {
    nb::class_<ed::Array<T>>(m, name)
        .def(nb::init<>())
        .def(nb::init<int, int>())
        // Map C++ operator[] to Python __getitem__
        .def("__getitem__", [](const ed::Array<T> &v, size_t i) {
            return v[i];
        })
        // Map C++ operator[] to Python __setitem__
        .def("__setitem__", [](ed::Array<T> &v, size_t i, T value) {
            v[i] = value;
        })
        .def("__len__", [](const ed::Array<T> &v) {
            return v.getLength();
        })
        .def("assign", [](ed::Array<T> &v, const ed::Array<T> &other) {
            v = other; // Llama al operator= de C++
            return &v;
        }, nb::rv_policy::reference)
        .def("__repr__", [](const ed::Array<T> &obj) {
            std::stringstream ss;
            ss << obj; // Usa tu operator<< de C++
            return ss.str();
        });
}

NB_MODULE(m_array, m) {
    bind_array<int>(m, "IntArray");
}
