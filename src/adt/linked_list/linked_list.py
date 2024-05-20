class LinkedListNode:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        formatted_list = ''
        temp_list = self
        while temp_list is not None:
            formatted_list += f'[{temp_list.value.__repr__()}]'
            temp_list = temp_list.next
            if temp_list is None:
                break
            formatted_list += ' -> '
        return formatted_list
