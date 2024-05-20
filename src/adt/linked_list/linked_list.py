from typing import Any, Union

from adt.linked_list.utils import print_all_list


class LinkedListNode:
    def __init__(self, value: Any = None, next_node: Union['LinkedListNode', None] = None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return print_all_list(self)
