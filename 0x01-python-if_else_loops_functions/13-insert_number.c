#include "lists.h"

/**
 * insert_node - Inserts a node into a sorted linked list
 * @head: pointer to the start of a list
 * @number: number to add
 *
 * Return: A sorted linked list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *aux, *tmp;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	aux = *head;
	if (!*head || !head)
	{
		new->next = NULL;
		(*head) = new;
		return (*head);
	}
	while (aux->next)
	{
		if (number < aux->next->n || number < aux->n)
			break;
		aux = aux->next;
	}
	tmp = aux->next;
	new->next = tmp;
	aux->next = new;
	return (*head);
}
