#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer to the head of the linked list.
 * @number: The number to insert.
 * Return: If the function fails - NULL.
 *Otherwise - a pointer to the new node.
*/
listint_t *insert_node(listint_t **head, int number)
{
/* Declare pointers */
listint_t *node = *head, *new;

/* Allocate memory for the new node */
new = malloc(sizeof(listint_t));
/* Check if memory allocation was successful */
if (new == NULL)
return (NULL);
/* Set the value of the new node */
new->n = number;

/* Check if the list is empty or new node is to be inserted at the beginning */
if (node == NULL || node->n >= number)
{
/* Insert the new node at the beginning */
new->next = node;
*head = new;
return (new);
}

/* Traverse the list to find the correct position to insert the new node */
while (node && node->next && node->next->n < number)
node = node->next;

/* Insert the new node in the middle or at the end of the list */
new->next = node->next;
node->next = new;
/* Return a pointer to the newly inserted node */
return (new);
}
