from typing import Any, Union


class LinkedListNode:
    def __init__(self, value: Any = None, next_node: Union['LinkedListNode', None] = None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        formatted_list = ''
        temp_list = self
        while temp_list is not None:
            formatted_list += f'[{temp_list.value.__repr__()}]'
            temp_list = temp_list.next_node
            if temp_list is None:
                break
            formatted_list += ' -> '
        return formatted_list
