#include <Python.h>

/**
 * print_python_string - Prints information about Python strings.
 * @p: A PyObject string object.
 */
void print_python_string(PyObject *p)
/* Define the function to print Python string info */
{
long int length;
/* Declare a variable to store string length */

fflush(stdout);
/* Flush the standard output buffer */

printf("[.] string object info\n");
/* Print header for string object info */

if (strcmp(p->ob_type->tp_name, "str") != 0)
/* Check if object is a string */
{
printf("  [ERROR] Invalid String Object\n");
/* Print error message for invalid object */
return;
/* Exit the function */
}

length = ((PyASCIIObject *)(p))->length;
/* Get the length of the string */

if (PyUnicode_IS_COMPACT_ASCII(p))
/* Check if the string is compact ASCII */
printf("  type: compact ascii\n");
/* Print type as compact ASCII */
else
printf("  type: compact unicode object\n");
/* Print type as compact Unicode */

printf("  length: %ld\n", length);
/* Print the length of the string */

printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &length));
/* Print the string value */
}
