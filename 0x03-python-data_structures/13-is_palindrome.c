#!/usr/bin/python3
#include <stddef.h>
#include <stdlib.h>
#include "lists.h"  /* Assuming the structure definition is present in lists.h */

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow, *fast, *prev = NULL, *temp, *middle = NULL;
    int is_palindrome = 1;

    if (*head == NULL || (*head)->next == NULL)
        return 1;  /* An empty list or a list with a single element is a palindrome */

    slow = *head;
    fast = *head;

    /* Use Floyd's algorithm to find the middle of the linked list */
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        temp = slow;
        slow = slow->next;
        temp->next = prev;
        prev = temp;
    }

    /* If the length of the linked list is odd, move slow to the next node */
    if (fast != NULL)
    {
        middle = slow;
        slow = slow->next;
    }

    /* Compare the first half and the reversed second half of the linked list */
    while (slow != NULL)
    {
        if (slow->n != prev->n)
        {
            is_palindrome = 0;
            break;
        }
        slow = slow->next;
        prev = prev->next;
    }

    /* Restore the original linked list (reversing it back) */
    temp = NULL;
    while (middle != NULL)
    {
        struct listint_s *next_node = middle->next;
        middle->next = temp;
        temp = middle;
        middle = next_node;
    }

    return is_palindrome;
}
