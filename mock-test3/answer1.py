class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            raise IndexError("Cannot pop from an empty stack")

    def isEmpty(self):
        return len(self.stack) == 0

# Creating an instance of the Stack class
my_stack = Stack()

# Pushing elements onto the stack
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

# Checking if the stack is empty
print(my_stack.isEmpty())  # Output: False

# Popping elements from the stack
top_element = my_stack.pop()
print(top_element)  # Output: 3

top_element = my_stack.pop()
print(top_element)  # Output: 2

# Checking if the stack is empty again
print(my_stack.isEmpty())  # Output: False

# Popping the remaining element
top_element = my_stack.pop()
print(top_element)  # Output: 1

# Checking if the stack is empty once more
print(my_stack.isEmpty())  # Output: True

# Trying to pop from an empty stack
# This will raise an IndexError
top_element = my_stack.pop()
