class Node:
    def __init__(self, value):
            self.value = value
            self.next = None

class Stack:    
    def __init__(self):
        self.head = None
        self.size = 0
   
    def push(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1
        
    def pop(self):
        if self.isEmpty():
            raise IndexError("pop from empty stack")
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.value
        
        
    def isEmpty(self):
        return self.size == 0
    
    def stackSize(self):
        return self.size

    def run(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value, end=" - ")
            currentNode = currentNode.next
        print()

    def peek(self):
        if self.isEmpty():
            raise IndexError("peek from empty stack")
        return self.head.value
