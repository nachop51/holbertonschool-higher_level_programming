#include <Python.h>
#include <listobject.h>

/**
 * print_python_list_info - Prints information about Python lists
 * @p: Python Object
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *obj = (PyListObject *)p;
	long int size = PyList_Size(p), i = 0;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", obj->allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
	}
}
