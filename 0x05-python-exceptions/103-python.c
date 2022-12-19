#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - prints information about a Python list object
 * @p: pointer to a Python object
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *item;

    if (!p || !PyList_Check(p))
    {
        printf("Error: Invalid list object\n");
        return;
    }

    size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

/**
 * print_python_bytes - prints information about a Python bytes object
 * @p: pointer to a Python object
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *data;

    if (!p || !PyBytes_Check(p))
    {
        printf("Error: Invalid bytes object\n");
        return;
    }

    size = PyBytes_Size(p);
    data = PyBytes_AsString(p);
    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", data);
    printf("  first 10 bytes: ");
    for (i = 0; i < 10 && i < size; i++)
        printf("%02hhx%c", data[i], i + 1 < 10 ? ' ' : '\n');
}

/**
 * print_python_float - prints information about a Python float object
 * @p: pointer to a Python object
 */
void print_python_float(PyObject *p)
{
    if (!p || !PyFloat_Check(p))
    {
        printf("Error: Invalid float object\n");
        return;
    }

    printf("[.] float object info\n");
    printf("  value: %f\n", PyFloat_AsDouble(p));
}
