#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * insert_node - Insert node in a sorted linked list
 * @head: Pointer to head of the linked list
 * @number: Data of the struct
 * Return: Pointer to the new inserted element
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp, *new, *prev = NULL;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	tmp = *head;
	if (tmp->n > number)
	{
		new->n = number;
		new->next = tmp;
		*head = new;
		return (new);
	}
	for (; tmp != NULL && tmp->n < number;)
	{
		prev = tmp;
		tmp = tmp->next;
	}
	new->n = number;
	prev->next = new;
	new->next = tmp;
	return (new);
}
