#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * main - check the code for
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head, *head2;

    head = NULL;
    add_nodeint_end(&head, 1);
    add_nodeint_end(&head, 17);
    add_nodeint_end(&head, 972);
    add_nodeint_end(&head, 50);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 50);
    add_nodeint_end(&head, 972);
    add_nodeint_end(&head, 17);
    add_nodeint_end(&head, 1);
    print_listint(head);

    head2 = NULL;
    add_nodeint_end(&head2, 1);
    add_nodeint_end(&head2, 17);
    add_nodeint_end(&head2, 972);
    add_nodeint_end(&head2, 50);
    add_nodeint_end(&head2, 982);
    add_nodeint_end(&head2, 501);
    add_nodeint_end(&head2, 972);
    add_nodeint_end(&head2, 17);
    add_nodeint_end(&head2, 1);
    print_listint(head2);
    if (is_palindrome(&head) == 1)
        printf("Linked list is a palindrome\n");
    else
        printf("Linked list is not a palindrome\n");
    if (is_palindrome(&head2) == 1)
        printf("Linked list is a palindrome\n");
    else
        printf("Linked list is not a palindrome\n");
    free_listint(head);
    free_listint(head2);

    return (0);
}