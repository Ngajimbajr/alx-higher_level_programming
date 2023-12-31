#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

/**
 * is_palindrome - a function that checks if a singly
 * linked list is a palindrome.
 * @head: a double pointer to the head of the list.
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr = *head;
	listint_t *p1, *p2;
	listint_t *slow = *head, *prev_slow = *head, *fast = *head;

	if (head == NULL)
		return (0);

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast && fast->next)
	{
		prev_slow = slow;
		fast = fast->next->next;
		slow = slow->next;
	}

	p1 = prev_slow;

	if (fast)
		p2 = slow->next;
	else
		p2 = slow;
	if ((p1->n) != (p2->n))
		return (0);

	ptr = *head;

	while (1)
	{
		while (ptr->next->n != p1->n)
		{
			ptr = ptr->next;
		}
		p1 = ptr;
		p2 = p2->next;

		if (p1->n != p2->n)
			break;
		ptr = *head;

		if (p1 = *head)
			return (1);
	}
	return (0);
}
