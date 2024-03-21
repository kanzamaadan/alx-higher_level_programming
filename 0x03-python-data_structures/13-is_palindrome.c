#include "lists.h"
#include <stddef.h>

/**
 * reverse - reverses the second half of the list
 *
 * @h_r: head of the second half
 * Return: no return
 */
void reverse(listint_t **h_r)
{
listint_t *prv;/* Pointer to the previous node */
listint_t *crr;/* Pointer to the current node */
listint_t *nxt;/* Pointer to the next node */
prv = NULL;/* Initialize the previous node to NULL */
crr = *h_r;/* Start from the head of the second half */
while (crr != NULL)
{
nxt = crr->next;/* Store the next node */
crr->next = prv;/* Reverse the pointer */
prv = crr;/* Move pointers forward */
crr = nxt;
}
*h_r = prv;/* Update the head of the second half */
}
/**
 * compare - compares each int of the list
 *
 * @h1: head of the first half
 * @h2: head of the second half
 * Return: 1 if are equals, 0 if not
 */
int compare(listint_t *h1, listint_t *h2)
{
listint_t *tmp1;/* Temporary pointer for the first half */
listint_t *tmp2;/* Temporary pointer for the second half */

tmp1 = h1;/* Start from the head of the first half */
tmp2 = h2;/* Start from the head of the second half */

while (tmp1 != NULL && tmp2 != NULL)
{
if (tmp1->n == tmp2->n)/* Compare the data of each node */
{
tmp1 = tmp1->next;/* Move to the next node */
tmp2 = tmp2->next;
}
else
{
return (0);/* If data doesn't match, return 0 */
}
}

if (tmp1 == NULL && tmp2 == NULL)/* Both lists reach the end */
{
return (1);/* Return 1 if all nodes are equal */
}

return (0);/* Return 0 if lists have different lengths */
}

/**
 * is_palindrome - checks if a singly linked list
 * is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome,
 * 1 if it is a palndrome
 */
int is_palindrome(listint_t **head)
{
listint_t *slow, *fast, *prev_slow;
listint_t *scn_half, *middle;
int isp;
slow = fast = prev_slow = *head;/* Initialize pointers */
middle = NULL;
isp = 1;/* Assume the list is a palindrome */
if (*head != NULL && (*head)->next != NULL)
{
while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;/* Move fast pointer two steps */
prev_slow = slow;/* Keep track of previous of slow */
slow = slow->next;/* Move slow pointer one step */
}
if (fast != NULL)
{
middle = slow;/* Save the middle node */
slow = slow->next;/* Move slow pointer to the second half */
}
scn_half = slow;/* Save the head of the second half */
prev_slow->next = NULL;
reverse(&scn_half);/* Reverse the second half */
/* Compare the first half with the reversed second half */
isp = compare(*head, scn_half);
if (middle != NULL)/* If there was a middle node */
{
/* Reconnect the first half with the middle node */
prev_slow->next = middle;
/* Reconnect the middle node with the reversed second half */
middle->next = scn_half;
}
else
{
prev_slow->next = scn_half;
}
}
return (isp);/* Return the result */
}
