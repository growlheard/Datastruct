import unittest

from datastruct.custom_queue import Queue
from datastruct.struct import Node, Stack


class TestNode(unittest.TestCase):
    n1 = Node(5, None)
    n2 = Node('a', n1)

    def test_attributes(self):
        self.assertEqual(self.n1.data, 5)
        self.assertEqual(self.n2.data, 'a')
        self.assertEqual(self.n1, self.n1)
        self.assertEqual(self.n2.next_node, self.n1)


class TestPop(unittest.TestCase):
    stack = Stack()

    def test_pop(self):
        self.stack.push('data1')
        self.stack.push('data2')
        self.stack.push('data3')
        self.assertEqual(self.stack.pop(), 'data3')
        self.assertEqual(self.stack.pop(), 'data2')
        self.assertEqual(self.stack.pop(), 'data1')
        self.assertEqual(self.stack.pop(), None)


class TestQueue(unittest.TestCase):
    def test_enqueue_empty(self):
        q = Queue()
        q.enqueue(1)
        self.assertEqual(q.head.data, 1)
        self.assertEqual(q.tail.data, 1)

    def test_enqueue_nonempty(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual(q.head.data, 1)
        self.assertEqual(q.tail.data, 3)
        self.assertIsNone(q.tail.next_node)
        self.assertEqual(q.head.next_node.data, 2)