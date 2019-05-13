"""
This code was a part of a Udacity course[DS and Algorithms in python] Quiz.
"""


class Queue:
    def __init__(self, head=None):
        self.storage = [head] if head is not None else []  # no need to insert when head is None

    def enqueue(self, new_element):
        """"
        This method inserts object in the queue.
        """
        self.storage.append(new_element)

    def peek(self):
        if len(self.storage) > 0:
            return self.storage[0]
        raise IndexError("queue is empty")

    def dequeue(self):
        if len(self.storage) > 0:
            return self.storage.pop(0)
        raise IndexError("queue is empty")

    def __len__(self):
        return len(self.storage)

    def __str__(self):
        return str(self.storage)

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    # Setup
    q = Queue(1)
    q.enqueue(2)
    q.enqueue(3)

    # Test peek
    # Should be 1
    print(q.peek())

    # Test dequeue
    # Should be 1
    print(q.dequeue())

    # Test enqueue
    q.enqueue(4)
    # Should be 2
    print(q.dequeue())
    # Should be 3
    print(q.dequeue())
    # Should be 4
    print(q.dequeue())
    q.enqueue(5)
    # Should be 5
    print(q.peek())
