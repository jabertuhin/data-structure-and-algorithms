from typing import List, Any, Optional


class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head: Node):
        self.head = head
        self.tail = head.next

    def __iter__(self):
        self.temp_head = self.head
        return self

    def __next__(self):
        if self.temp_head is not None:
            temp = self.temp_head
            self.temp_head = self.temp_head.next
            return temp
        else:
            raise StopIteration

    def append(self, node: Node):
        if self.tail is None:
            self.tail = node
            self.head.next = self.tail
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def remove_first(self):
        temp = self.head
        del temp
        self.head = self.head.next

    def remove_last(self):
        head = self.head
        prev = None
        while head.next:
            prev = head
            head = head.next
        prev.next = None
        del head

    def remove(self, value) -> bool:
        head = self.head
        prev = None
        while True:
            if head is None or head.val == value:
                break
            prev = head
            head = head.next
        if head is not None:
            prev.next = head.next
            del head
            return True
        return False

    def to_list(self) -> List:
        lst = []
        for node in self:
            lst.append(node.val)
        return lst

    def max_val(self) -> Any:
        max_value = self.head.val
        for node in self:
            if node.val > max_value:
                max_value = node.val
        return max_value

    def min_val(self) -> Any:
        min_value = self.head.val
        for node in self:
            if node.val < min_value:
                min_value = node.val
        return min_value

    def search(self, value) -> Optional[Node]:
        for node in self:
            if node.val == value:
                return node
        return None


if __name__ == '__main__':
    n = Node(1, None)
    l = LinkedList(n)
    l.append(Node(2, None))
    l.append(Node(3, None))
    l.append(Node(4, None))
    l.append(Node(-1, None))
    l.append(Node(10, None))
    l.append(Node(5, None))

    # print [1, 2, 3, 4, -1, 10, 5]
    print(l.to_list())

    # print 10
    print(l.max_val())

    # print -1
    print(l.min_val())

    # print 4
    print(l.search(4).val)

    # print None
    print(l.search(12))

    l.remove_first()
    # print [2, 3, 4, -1, 10, 5]
    print(l.to_list())

    l.remove_last()
    # print [2, 3, 4, -1, 10]
    print(l.to_list())

    l.remove(4)
    # [2, 3, -1, 10]
    print(l.to_list())
    l.remove(10)
    # print [2, 3, -1]
    print(l.to_list())
    l.remove(20)
    # print [2, 3, -1]
    print(l.to_list())
