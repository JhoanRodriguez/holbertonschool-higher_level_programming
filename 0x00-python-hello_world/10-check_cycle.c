#include "lists.h"
/**
 * check_cycle - check if there is a cycle on a list
 * @list: pointer to the head of the data struck
 * Return: 0 if there is not cycle, 1 for a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (list == NULL || list->next == NULL)
		return (0);

	slow = list;
	fast = list;

	while (fast != NULL && slow != NULL && fast->next != NULL)
	{
		slow  = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
