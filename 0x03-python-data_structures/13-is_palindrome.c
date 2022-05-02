#include "lists.h"
#include <stdio.h>

/**
 * is_palindrome - Checks if a linked list is palindrome or not
 * @head: Linked list
 *
 * Return: 0 if is not palindrome or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *aux = *head;
	int length = 0, *array = NULL, i = 0;

	if (!head || !*head)
		return (1);
	length = listint_len(*head);
	array = malloc(sizeof(int) * length);
	if (!array)
		return (-1);
	while (aux != NULL)
	{
		array[i] = aux->n;
		printf("\n\nAUX[%d]:%d\n", i, aux->n);
		aux = aux->next;
		i++;
	}
	for (i = 0; i < length; i++)
	{
		printf("%d\n", array[i]);
	}
	return (1);
}

/*

listint_t *len, *end, *str;
	int length = 0, tail = 0, lengthcopy;

	if (!head)
		return (1);
	len = *head, str = *head;
	while (len->next != NULL)
		len = len->next, length++;
	lengthcopy = length;
	while (length > lengthcopy / 2)
	{
		end = *head, tail = 0;
		while (tail < length)
		{
			end = end->next;
			tail++;
		}
		if (str->n == end->n)
			str = str->next;
		else
			return (0);
		length--;
	}
	return (1);

*/

/**
 * listint_len -  function that returns the number of elements in a linked list
 * @h: list
 *
 * Return: Number of nodes
 */
size_t listint_len(const listint_t *h)
{
	int i = 0;

	for (i = 0; h != NULL; i++)
		h = h->next;
	return (i);
}
