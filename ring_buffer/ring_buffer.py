from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # length should be less than capacity
        if self.storage.length == self.capacity:
            if self.current is None:
                self.current = self.storage.tail
            self.current.value = item
            self.current = self.current.prev
        else:
            self.storage.add_to_head(item)
    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        # TODO: Your code here
        current = self.storage.tail
        if self.storage.length == 0:
            return list_buffer_contents
        while current:
            list_buffer_contents.append(current.value)
            current = current.prev
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
