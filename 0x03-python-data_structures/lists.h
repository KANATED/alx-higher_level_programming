#ifndef LISTS_H
#define LISTS_H

#include <stddef.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

/* Function prototypes */
void print_list_integer(listint_t *list);
int def element_at(my_list, idx)
int element_at(listint_t *list, int index);
listint_t *replace_in_list(listint_t *list, int index, int new_value);
void print_reversed_list_integer(listint_t *list);
listint_t *new_in_list(listint_t *list, int index, int value);
char *no_c(char *str);
void print_matrix_integer(listint_t **matrix);
listint_t *add_node_end(listint_t **head, int n);
void free_list(listint_t *head);
int is_palindrome(listint_t **head);

#endif /* LISTS_H */
