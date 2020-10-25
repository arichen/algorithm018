class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.size = k
        self.data = [None] * k
        self.start = 0
        self.length = 0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.length == self.size:
            return False

        if self.length == 0:
            self.data[self.start] = value
        else:
            self.start = (self.start + self.size - 1) % self.size
            self.data[self.start] = value
        self.length += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.length == self.size:
            return False

        end = (self.start + self.length) % self.size
        self.data[end] = value
        self.length += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.length == 0:
            return False

        self.start = (self.start + 1) % self.size
        self.length -= 1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.length == 0:
            return False

        self.length -= 1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.length == 0:
            return -1
        return self.data[self.start]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.length == 0:
            return -1
        return self.data[(self.start + self.length - 1) % self.size]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.length == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.length == self.size
