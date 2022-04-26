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

	if (!*head || !head)
		return (NULL);
	aux = *head;
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	while (aux->next)
	{
		if (number < aux->next->n)
			break;
		aux = aux->next;
	}
	tmp = aux->next;
	new->n = number;
	new->next = tmp;
	aux->next = new;
	return (*head);
}
