
from stack import Stack
import time


def sortStack(stackA):
    stackB = Stack()

    pushes = 0
    pops = 0
    comparisons = 0

    while not stackA.isEmpty():
        x = stackA.pop()
        pops += 1

        while not stackB.isEmpty():
            y = stackB.pop()
            pops += 1

            comparisons += 1
            if y < x:
                stackA.push(y)
                pushes += 1
            else:
                stackB.push(y)
                pushes += 1
                break

        stackB.push(x)
        pushes += 1

    return stackB, pushes, pops, comparisons


if __name__ == "__main__":
    stackA = Stack()

    # Välj vilken datafil som ska testas
    # n = 100
    with open("data_set_100_best.txt", "r") as file:
    #with open("data_set_100_random.txt", "r") as file:
    #with open("data_set_100_worst.txt", "r") as file:

    # n = 500
    #with open("data_set_500_best.txt", "r") as file:
    #with open("data_set_500_random.txt", "r") as file:
    #with open("data_set_500_worst.txt", "r") as file:

    # n = 1000
    #with open("data_set_1000_best.txt", "r") as file:
    #with open("data_set_1000_random.txt", "r") as file:
    #with open("data_set_1000_worst.txt", "r") as file:

    # n = 2000
    #with open("data_set_2000_best.txt", "r") as file:
    #with open("data_set_2000_random.txt", "r") as file:
    #with open("data_set_2000_worst.txt", "r") as file:
        numbers = [int(x) for x in file.read().split()]

    for num in numbers:
        stackA.push(num)

    # Starta tidtagningen
    start_time = time.perf_counter()

    sortedStack, pushes, pops, comparisons = sortStack(stackA)

    # Stoppa tidtagningen
    elapsed_time = time.perf_counter() - start_time

    # Skriv ut resultaten
    print("Push:", pushes)
    print("Pop:", pops)
    print("Comparisons:", comparisons)
    print("Total operations:", pushes + pops + comparisons)
    print("Sorting time:", elapsed_time, "seconds")
