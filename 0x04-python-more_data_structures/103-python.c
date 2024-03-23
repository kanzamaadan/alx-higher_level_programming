#include <Python.h>

/**
 * print_python_bytes - Prints information about Python bytes objects
 * @p: PyObject pointer to the Python bytes object
 */
void print_python_bytes(PyObject *p)
{
Py_ssize_t size, i;
char *str;
/* Check if p is a valid bytes object */
if (!PyBytes_Check(p))
{
printf("[ERROR] Invalid Bytes Object\n");
return;
}
/* Get the size (length) of the bytes object */
size = PyBytes_Size(p);
/* Print bytes object info */
printf("[.] bytes object info\n  size: %ld\n", size);
/* Try to convert the bytes object to a string */
str = PyBytes_AsString(p);
printf("  trying string: %s\n", str);
/* Print the first 10 bytes of bytes object in hexadecimal format */
printf("  first 10 bytes:");
for (i = 0; i < size && i < 10; i++)
printf(" %02x", (unsigned char)str[i]);
printf("\n");
}

/**
 * print_python_list - Prints information about Python lists
 * @p: PyObject pointer to the Python list
 */
void print_python_list(PyObject *p)
{
Py_ssize_t size, alloc, i;
PyObject *item;

/* Check if p is a valid Python object */
if (!PyList_Check(p))
{
printf("[ERROR] Invalid Python Object\n");
return;
}
/* Get the size and allocated memory of the list */
size = PyList_Size(p);
alloc = ((PyListObject *)p)->allocated;
/* Print list info */
printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", alloc);
/* Iterate through each element of the list */
for (i = 0; i < size; i++)
{
/* Get the current item */
item = PyList_GetItem(p, i);
/* Print the element type */
if (PyBytes_Check(item))
printf("Element %ld: bytes\n", i);
else if (PyFloat_Check(item))
printf("Element %ld: float\n", i);
else if (PyTuple_Check(item))
printf("Element %ld: tuple\n", i);
else if (PyList_Check(item))
printf("Element %ld: list\n", i);
else if (PyLong_Check(item))
printf("Element %ld: int\n", i);
else if (PyUnicode_Check(item))
printf("Element %ld: str\n", i);
else
printf("Element %ld: Unknown type\n", i);
/* If the element is bytes, print its info */
if (PyBytes_Check(item))
print_python_bytes(item);
}
}
