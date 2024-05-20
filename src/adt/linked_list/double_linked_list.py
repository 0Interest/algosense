from typing import Any

from adt.linked_list.utils import print_all_list


class DoubleLinkedListNode:
    def __init__(self, value: Any = None,
                 prev_node: 'DoubleLinkedListNode' = None,
                 next_node: 'DoubleLinkedListNode' = None):
        self.value = value
        self.prev_node = prev_node
        self.next_node = next_node

    def __str__(self):
        return print_all_list(self)
