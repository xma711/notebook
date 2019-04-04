/* practising on link list and pointers */
/* some notes: need to pass in reference to a reference (x) if i want a function to modify the reference x */

#include <stdlib.h>
#include <stdio.h>
#include <assert.h>

struct LINK_LIST {
	int i;
	struct LINK_LIST *next;
};

// cannot do this: pass in a reference, and then reference = malloc()
// why? because i need to pass in the pointer to the pointer! 
// otherwise the pointer itself cannot be changed, just like a value
struct LINK_LIST* create_new_element() {
	return (struct LINK_LIST*) malloc(sizeof(struct LINK_LIST));
};

void create_new_element_by_ref(struct LINK_LIST** ele) {
        *ele = (struct LINK_LIST*) malloc(sizeof(struct LINK_LIST));
	return;
};

int num_elements(struct LINK_LIST *head) {
	int num = 0;
	struct LINK_LIST * next;
	next = head;

	while (next) {
		num++;
		next = next->next;
	}

	return num;
};

struct LINK_LIST* get_tail(struct LINK_LIST* head) {
	struct LINK_LIST* cur = head;
	assert(head);

	// if the cur->next is null, then cur must be the tail
        while (cur->next) { 
                cur = cur->next;
        }
	return cur;

}

void insert_to_tail(struct LINK_LIST *head, struct LINK_LIST *element) {
	struct LINK_LIST* tail = get_tail(head);
	tail->next = element;
};

// n starts from 0
struct LINK_LIST* get_nth_element(struct LINK_LIST* head, int n, int size_link_list) { 
        struct LINK_LIST* cur = head;
        assert(head);
	assert(n < size_link_list);
	int i = 0;

        // if the cur->next is null, then cur must be the tail
        while (i < n) {
		i++;
                cur = cur->next;
        }
        return cur;

}


// n starts from 0
// note that head will be changed if n = 0; so need to pass in the reference to head, instead of head
// if passing in head directly, when n=0, head cannot be changed! which is wrong. -> need to be careful about this part!
void remove_nth_element(struct LINK_LIST **head__, int n){
	struct LINK_LIST* head = *head__; // get the real head, which can be changed too

	int len = num_elements(head);
	if (n >= len)
		return; // no need to remove anything

	if (n == 0){
		*head__ = head->next;
		free(head);
		assert( num_elements(*head__) == len - 1 );
		return;
	}

	// from this point onward, n is not the head
	assert(head);
        int i = 0;
        struct LINK_LIST* cur = head;
	struct LINK_LIST* pre = NULL;
        // if the cur->next is null, then cur must be the tail
        while (i < n) {
                i++;
		pre = cur;
                cur = cur->next;
        }
	assert(pre);
	assert(cur);

	// cur is the element to delete
	pre->next = cur->next;
	free(cur);
	assert( num_elements(head) == len - 1 );
};

void print_link_list(struct LINK_LIST *head) {
	int i = 0;
	struct LINK_LIST* cur = head;
	while (cur != NULL) {
		printf("%d:\t%d\n", i, cur->i);
		fflush(stdout);
		i++;
		cur = cur->next;
	}
	printf("\n");
};

int main () {
	int i = 0;
	struct LINK_LIST* head;
	create_new_element_by_ref(&head); // this works!
//	head = (struct LINK_LIST*) calloc(1, sizeof(struct LINK_LIST)); // of course this works
//	head = create_new_element(); // this also works
	assert(head);
	head->i = i;
	i++;

	print_link_list(head);

	int j;
	for (j = 0; j < 9; j++) {
        	struct LINK_LIST* ele;
		//ele = (struct LINK_LIST*) calloc(1, sizeof(struct LINK_LIST));
		//ele->next = NULL; // is this necessary?
		ele = create_new_element();
		ele->i = i;
		i++;
		insert_to_tail(head, ele);
		ele = NULL;
	}
	print_link_list(head);

	// now remove 3 elements
	printf("remove element 0, 5 and 7\n");
	// need to be careful here. after removing one element, the element number is different
	remove_nth_element(&head, 7);
        remove_nth_element(&head, 5);
        remove_nth_element(&head, 0); // it doesn't change the head's value!
	print_link_list(head);

	return 0;

}
