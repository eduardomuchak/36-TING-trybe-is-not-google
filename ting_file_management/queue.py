class Queue:
    def __init__(self):
        self.queue = []

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0)

    def search(self, index):
        if index < len(self.queue) and index >= 0:
            return self.queue[index]
        else:
            raise IndexError

    def values(self):
        return str(self.queue)
