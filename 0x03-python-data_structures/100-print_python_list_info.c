#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints information about a Python list
 * @p: PyObject pointer representing the Python list
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
long int size, i;/* Declaration of variables */
PyListObject *list;/* Pointer to a Python list object */
PyObject *item;/* Pointer to a Python object */

size = Py_SIZE(p);/* Get the size of the list */
/* Print list size */
printf("[*] Size of the Python List = %ld\n", size);
/* Cast the PyObject pointer to PyListObject */
list = (PyListObject *)p;
/* Print allocated memory */
printf("[*] Allocated = %ld\n", list->allocated);

/* Loop through each element of the list */
for (i = 0; i < size; i++)
{
/* Get the i-th item from the list */
item = PyList_GetItem(p, i);
/* Print element index and its type name */
printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
}
}
