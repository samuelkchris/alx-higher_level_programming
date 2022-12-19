#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        printf("Error: Invalid PyListObject\n");
        return;
    }
    Py_ssize_t size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        printf("Error: Invalid PyBytesObject\n");
        return;
    }
    Py_ssize_t size = PyBytes_Size(p);
    printf("[.] Python bytes info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", PyBytes_AsString(p));
    printf("  first %ld bytes: ", size < 10 ? size : 10);
    for (Py_ssize_t i = 0; i < (size < 10 ? size : 10); i++) {
        printf("%02x ", (unsigned char) PyBytes_AsString(p)[i]);
    }
    printf("\n");
}

void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        printf("Error: Invalid PyFloatObject\n");
        return;
    }
    printf("[.] Python float info\n");
    double value = PyFloat_AS_DOUBLE(p);
    printf("  value: %.16g\n", value);
}
