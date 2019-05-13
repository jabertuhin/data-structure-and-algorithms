from unittest import TestCase

from data_structures import Queue


class TestQueue(TestCase):
    def test_queue_object(self):
        q = Queue(1)
        self.assertEqual(len(q), 1)

    def test_blank_queue_object(self):
        q = Queue()
        self.assertEqual(len(q), 0)

    def test_enqueue(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)

        self.assertEqual(len(q), 3)

    def test_peek(self):
        q = Queue(1)
        q.enqueue(2)
        q.enqueue(5)

        self.assertEqual(q.peek(), 1)

        q = Queue()  # empty queue
        self.assertRaises(IndexError, q.peek)  # supposed to raise IndexError

    def test_dequeue(self):
        q = Queue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)

        self.assertEqual(len(q), 4)
        self.assertEqual(q.peek(), 1)
        q.dequeue()
        self.assertEqual(len(q), 3)
        self.assertEqual(q.peek(), 2)

        while q.storage:
            q.dequeue()

        self.assertRaises(IndexError, q.dequeue)
