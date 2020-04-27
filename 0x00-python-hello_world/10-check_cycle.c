#include "lists.h"
/**
 * check_cycle - check if there is a cycle on a list
 * @list: pointer to the head of the data struck
 * Return: 0 if there is not cycle, 1 for a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *fast;
	listint_t *slow;

	slow = list;
	fast = list;

	while (fast != NULL)
	{
		slow  = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
