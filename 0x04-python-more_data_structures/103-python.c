#include <Python.h>

void print_python_list(PyObject *p) {
    PyObject *item;
    Py_ssize_t size, i;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    size = PyList_Size(p);
    for (i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

void print_python_bytes(PyObject *p) {
    PyBytesObject *bytes = (PyBytesObject *)p;
    Py_ssize_t size, i;

    printf("[.] bytes object info\n");
    printf("  [.] address of the object: %p\n", (void *)p);
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    printf("  [.] size: %ld\n", size);
    printf("  [.] trying string: %s\n", PyBytes_AsString(p));

    printf("  [.] first %ld bytes: ", size < 10 ? size : 10);
    for (i = 0; i < size && i < 10; i++) {
        printf("%02x", bytes->ob_sval[i] & 0xff);
        if (i < size - 1 && i < 9)
            printf(" ");
    }
    printf("\n");
}
