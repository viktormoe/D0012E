from stack import Stack
import time

start_time = time.time()

def sortStack(stackA):
    stackB = Stack()
    
    while not stackA.isEmpty():
        x = stackA.pop()
        
        while not stackB.isEmpty():
            y = stackB.pop()
            
            if y < x:
                stackA.push(y)
            else:
                stackB.push(y)
                break
            
        stackB.push(x)    
    
    return stackB

if __name__ == "__main__":
    stackA = Stack()
    
    with open("data_set_10000.txt", "r") as file:
        numbers = [int(x) for x in file.read().split()]

    for num in numbers:
        stackA.push(num)

    sortedStack = sortStack(stackA)

    while not sortedStack.isEmpty():
        print(sortedStack.pop())
        
print("--- %s seconds ---" % (time.time() - start_time))