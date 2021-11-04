"""Implementation of Queue and Stack"""


class Container:
    """Container superclass to help implement Queue and Stack"""
    def __init__(self):
        self._items = []

    def size(self):
        """Returns # elements in self.items"""
        _size = len(self._items)
        return _size

    def is_empty(self):
        """Checks if self.items is empty"""
        if len(self._items) == 0:
            return True

    def push(self, item):
        """Add item to end of self.items"""
        return self._items.append(item)

    def pop(self):
        """Pop off correct element of self.items and return it
            Differs between subclasses, hence not implemented in superclass
        """
        raise NotImplementedError

    def peek(self):
        """Returns top element without removing it
            Differs between subclasses, hence not implemented in superclass
        """
        raise NotImplementedError


class Queue(Container):
    """Container subclass: Implements Queue(LIFO)"""
    def __init__(self):
        super(Queue, self).__init__()

    def peek(self):
        """Returns first element of list without deleting it"""
        assert not self.is_empty()
        return self._items[0]

    def pop(self):
        """Pop off first element"""
        assert not self.is_empty()
        return self._items.pop(0)


class Stack(Container):
    """Container subclass: Implements Stack(FIFO)"""
    def __init__(self):
        super(Stack, self).__init__()

    def peek(self):
        """Returns first element of list without deleting it"""
        assert not self.is_empty()
        return self._items[-1]

    def pop(self):
        """Pop off first element"""
        assert not self.is_empty()
        return self._items.pop()
