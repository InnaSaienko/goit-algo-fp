import heapq
from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    """Single linked list node"""
    value: int
    next: Optional["Node"] = None


def reverse_linked_list(head):
    """Reverse singly linked list"""
    prev = None
    current = head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev  # new head


def insertion_sort_linked_list(head):
    """Insertion sort singly linked list"""

    sorted_head = None
    current = head

    # Traverse the given linked list and
    # insert every node to sorted
    while current:
        next_node = current.next
        if sorted_head is None or current.value < sorted_head.value:
            current.next = sorted_head
            sorted_head = current
        else:
            s = sorted_head
            while s.next and s.next.value < current.value:
                s = s.next
            current.next = s.next
            s.next = current
        current = next_node
    return sorted_head


def merge_sorted_lists(list_1, list_2):
    """Merge two sorted singly linked lists"""

    temp_node = Node(0)
    tail = temp_node

    while list_1 and list_2:
        if list_1.value < list_2.value:
            tail.next = list_1
            list_1 = list_1.next
        else:
            tail.next = list_2
            list_2 = list_2.next
        tail = tail.next
    tail.next = list_1 if list_1 else list_2
    return temp_node.next


def print_linked_list(head):
    """Print linked list values"""

    values = []
    while head:
        values.append(head.value)
        head = head.next
    print(" -> ".join(map(str, values)))


if __name__ == "__main__":
    head = Node(4)
    head.next = Node(2)
    head.next.next = Node(1)
    head.next.next.next = Node(3)
    head.next.next.next.next = Node(5)

    print("Original list: ")
    print_linked_list(head)

    head = insertion_sort_linked_list(head)
    print("Sorted list:")
    print_linked_list(head)

    head = reverse_linked_list(head)
    print("Reversed list:")
    print_linked_list(head)
