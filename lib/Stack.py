class Stack:
    def __init__(self, items=None, max_size=None):
        self.items = items if items is not None else []
        self.max_size = max_size

    def push(self, item):
        if self.max_size is None or len(self.items) < self.max_size:
            self.items.append(item)
        else:
            print("Stack is full. Cannot push item.")

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            print("Stack is empty. Cannot pop item.")
            return None

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def full(self):
        return self.max_size is not None and len(self.items) >= self.max_size

    def search(self, item):
        for index, value in enumerate(self.items):
            if value == item:
                return len(self.items) - 1 - index
        return -1
