import unittest

from datastruct.custom_queue import Queue
from datastruct.linked_list import LinkedList, ll
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


class Test_dequeue(unittest.TestCase):
    def test_dequeue_empty_queue(self):
        queue = Queue()
        self.assertIsNone(queue.dequeue())

    def test_dequeue_single_element_queue(self):
        queue = Queue()
        queue.enqueue(1)
        self.assertEqual(queue.dequeue(), 1)
        self.assertTrue(queue.dequeue() is None)

    def test_dequeue_multiple_element_queue(self):
        queue = Queue()
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)
        self.assertEqual(queue.dequeue(), 4)
        self.assertTrue(queue.dequeue() is None)


class Test_linkedList(unittest.TestCase):
    def test_linkedList(self):
        ll = LinkedList()
        ll.insert_beginning({"id": 1})
        ll.insert_at_end({"id": 2})
        ll.insert_at_end({"id": 3})
        ll.insert_beginning({"id": 0})

        self.assertEqual(ll.head.data, {"id": 0})
        self.assertEqual(ll.tail.data, {"id": 3})
        self.assertEqual(ll.head.next_node.data, {"id": 1})
        self.assertEqual(ll.head.next_node.next_node.data, {"id": 2})


class TestToList(unittest.TestCase):
    def test_to_list_returns_correct_list(self):
        ll = LinkedList()
        ll.insert_beginning(1)
        ll.insert_at_end(2)
        ll.insert_beginning(3)
        self.assertEqual(ll.to_list(), [3, 1, 2])

    def test_to_list_returns_empty_list(self):
        ll = LinkedList()
        self.assertEqual(ll.to_list(), [])

    def test_get_data_by_id_returns_correct_data(self):
        ll = LinkedList()
        data_1 = {'id': 1, 'name': 'Alice'}
        data_2 = {'id': 2, 'name': 'Bob'}
        ll.insert_beginning(data_1)
        ll.insert_at_end(data_2)
        self.assertEqual(ll.get_data_by_id(1), data_1)
        self.assertEqual(ll.get_data_by_id(2), data_2)

    def test_get_data_by_id(self):
        self.assertEqual(ll.get_data_by_id(0), None)
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end('idusername')
        ll.insert_at_end([1, 2, 3])
        ll.insert_at_end({'id': 2, 'username': 'mosh_s'})
        self.assertEqual(ll.get_data_by_id(1), {'id': 1, 'username': 'lazzy508509'})
        self.assertEqual(ll.get_data_by_id(2), None)
