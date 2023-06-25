class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        else:
            raise IndexError("Cannot dequeue from an empty queue")

    def isEmpty(self):
        return len(self.queue) == 0
# Creating an instance of the Queue class
my_queue = Queue()

# Enqueueing elements into the queue
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

# Checking if the queue is empty
print(my_queue.isEmpty())  # Output: False

# Dequeueing elements from the queue
front_element = my_queue.dequeue()
print(front_element)  # Output: 1

front_element = my_queue.dequeue()
print(front_element)  # Output: 2

# Checking if the queue is empty again
print(my_queue.isEmpty())  # Output: False

# Dequeueing the remaining element
front_element = my_queue.dequeue()
print(front_element)  # Output: 3

# Checking if the queue is empty once more
print(my_queue.isEmpty())  # Output: True

# Trying to dequeue from an empty queue
# This will raise an IndexError
front_element = my_queue.dequeue()
