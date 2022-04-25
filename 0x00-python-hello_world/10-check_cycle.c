#include "lists.h"

/**
 * check_cycle - Takes a linked list and checks if there is a cycle in it
 * @list: Linked list
 *
 * Return:0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast_p = list;
	listint_t *slow_p = list;

	if (!list)
		return (0);

	while (slow_p && fast_p && fast_p->next)
	{
		slow_p = slow_p->next;
		fast_p = fast_p->next->next;
		if (slow_p == fast_p)
			return (1);
	}
	return (0);
}
