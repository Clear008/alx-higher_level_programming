#include<Phython.h>
/**
 * print_python_list_info - prints some info about Python lists
 * @p: a pointer to a python object
 */
void print_python_list_info(PyObject *p)
{
	int size, allocation, i;
	PhObject *obj;

	size = Py_SIZE(p);
	allocation = ((PyListObject *)p)-> allocated;
	printf("[*] Size of the Python List = %d\n",size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);
		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
