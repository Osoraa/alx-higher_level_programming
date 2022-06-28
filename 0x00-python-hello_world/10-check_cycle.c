#include "lists.h"

/**
 * check_cycle - Checks if theres a cycle in a linked list.
 * @list: list head.
 *
 * Return: 1 if theres a cycle, 0 otherwise.
 */
int check_cycle(listint_t *list)
{
	listint_t *trav = list->next;

	if (list == NULL)
		return (0);

	while (trav != NULL)
	{
		if (trav == list || trav->next == trav)
			return (1);

		trav = trav->next;
	}

	return (0);
}
