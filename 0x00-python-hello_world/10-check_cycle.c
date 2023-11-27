#include "lists.h"

/**
 * check_cycle - check for cycle in singly linked list
 * @list: pointer to the list.
 *
 * Return: 0 cycle abscent, 1 cycle present
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
