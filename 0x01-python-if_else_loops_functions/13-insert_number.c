#include "lists.h"

/**
 * insert_node - Inserts a number in a sorted linked list.
 * 
 * @head: List beginning.
 * @number: Integer value of the node to insert in the list.
 *
 * Return: NULL on failure, or Node address.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *prev, *node;

	node = malloc(sizeof(listint_t));
	if (!node || !current)
		return (NULL);
	node->n = number;
	node->next = NULL;

	if (!(current))
	{
		*head = node;
		return (node);
	}

	if (current->n > number)
	{
		node->next = current;
		head = &node;
		return (node);
	}

	while (current->n < number)
	{
		if (current->next != NULL)
		{
			prev = current;
			current = current->next;
			continue;
		}
		current->next = node;
		return (node);
	}

	node->next = current;
	prev->next = node;
	return (node);
}