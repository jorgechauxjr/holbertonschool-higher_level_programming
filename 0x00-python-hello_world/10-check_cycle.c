#include "lists.h"
/**
 * check_cycle -fnction.
 *Description: Function checks if a singly linked list has a cycle in it.
 * @list: pointer of type listint_t
 * Return: 0 if there is no cycle, 1 if there is a cycle
 **/
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

/* "slow" will go 1 by 1  "fast" will go 2 by 2 through the list*/
	while ((slow && fast != NULL) && (fast->next != NULL))
	{
		slow = slow->next;
		fast = fast->next->next;
/*if slow is equal to fast it means they are in the same place of the list*/
/* as result it means there is a cycle in the list*/
		if (slow == fast)
			return (1);
			}
/*if not, the list have no cycle*/
	return (0);
}
