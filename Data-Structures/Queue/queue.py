class Queue:
    
    def __init__(self):
        self.data = []

    def __repr__(self):
        return str(self.data)

    def __len__(self):
        return len(self.data)

    def queue(self, value):
        self.data.append(value)

    def dequeue(self):
        return self.data.pop(0)
