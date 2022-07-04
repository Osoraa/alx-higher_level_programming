#include "lists.h"

/**
 * is_palindrome - Checks if a singly-linked list is a palindrome.
 * @head: List beginning.
 *
 * Return: 1 if list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int list_len = 1, *num_list, i;

	/* Empty list is a Palindrome */
	if (!current)
		return (1);

	/* Find length of list */
	while(current->next)
	{
		list_len++;
		current = current->next;
	}
	current = *head;

	/* Store reversed linked-list items in an array */
	num_list = malloc(sizeof(int) * list_len);
	if (!num_list)
		return (0);
	for (i = 1; i <= list_len; i++)
	{
		num_list[list_len - i] = current->n;
		current = current->next;
	}
	current = *head;
	i = 0;

	/* Compare linked-list and resulting array */
	while(i < list_len)
	{
		if (num_list[i++] != current->n)
			return (0);
		current = current->next;
	}
	return (1);
}





