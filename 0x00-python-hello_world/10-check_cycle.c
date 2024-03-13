#include "lists.h"

/**
 * check_cycle - check for loop in LinkedList
 * @head: head of linked list
 * Description - check for loops in LL
 * Return: 1 if cycled, 0 if not
*/

int check_cycle(listint_t *head)
{
/* Initially,pointers to the head of the linked list*/
listint_t *slow, *fast;
if (!head)
{
/*if there's no head, which means no list, return 0*/
return (0);
}
slow = head;/*1 step*/
fast = head->next;/*2 steps*/
while (fast && slow && fast->next)
{
if (slow == fast)
{
/*this means if fast next is pointinf to*/
/*a privious node, which is slow*/
return (1);/*it's a cycle!*/
}
slow = slow->next;/*slow moves 1 step*/
fast = fast->next->next;/*fast moves 2 steps*/
}
/*if they didn't met anywhere, it's not a cycle */
return (0);
}
