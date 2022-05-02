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
}
