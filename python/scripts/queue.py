class queue:
    def __init__(self):
        self.queue_size = 1000
        self.queue = []

    def getQueueLenght(self):
        return len(self.queue)

    def push(self,value):
        if self.getQueueLenght() + 1 > self.queue_size:
            raise Exception("Error: Queue Overflow")
        self.queue.append(value)
        return self.queue

    def pop():
        if (self.getQueueLenght()) == 0:
            raise Exception("Error: Queue Underflow")
        del self.queue[0]
        return self.queue
