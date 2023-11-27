#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lists.h"

/**
 * check_cycle - checks if list has a cycle in it
 * @list: pointer to list
 * Return: 1 if there is a cycle, 0 if not
 */

int check_cycle(listint_t *list)
{
listint_t *slow = list;
listint_t *fast = list;

while (slow && fast && fast->next)
{
slow = slow->next;
fast = fast->next->next;
if (slow == fast)
{
return (1);
}
}
return (0);
}
