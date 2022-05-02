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
	int length = 0, *array = NULL, i = 0, j = 0;

	if (!head || !*head)
		return (1);
	length = listint_len(*head);
	array = malloc(sizeof(int) * length);
	if (!array)
		return (-1);
	while (i < length)
	{
		array[i] = aux->n;
		aux = aux->next;
		i++;
	}
	j = length - 1;
	for (i = 0; i < (length -1) / 2; i++, j--)
	{
		if (array[i] != array[j])
		{
			free(array);
			return (0);
		}
	}
	free(array);
	return (1);
}

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
