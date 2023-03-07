from datastruct.struct import Node


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.tail is not None:
            self.tail.next_node = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def dequeue(self):
        if self.head is None:
            return None
        value = self.head.data
        self.head = self.head.next_node
        return value


queue = Queue()
queue.enqueue('data1')
queue.enqueue('data2')
queue.enqueue('data3')
print(queue.dequeue())

print(queue.dequeue())

print(queue.dequeue())

print(queue.dequeue())