from typing import Union


def print_all_list(linked_list: Union['LinkedListNode', 'DoubleLinkedListNode']):
    formatted_list = ''
    temp_list = linked_list
    while temp_list is not None:
        formatted_list += f'[{temp_list.value.__repr__()}]'
        temp_list = temp_list.next_node
        if temp_list is None:
            break
        formatted_list += ' -> '
    return formatted_list
