import random


class Node:
    def __init__(self, color, number, next_node=None):
        self.color = color
        self.number = number
        self.next_node = next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def get_data(self):
        return self.color + "-" + str(self.number)


class Stack:
    def __init__(self, limit=1000):
        self.top_node = None
        self.size = 0
        self.limit = limit

    def is_full(self):
        return self.size == self.limit

    def is_empty(self):
        return self.size == 0

    def push(self, color, number):
        if not self.is_full():
            item = Node(color, number)
            item.set_next_node(self.top_node)
            self.top_node = item
            self.size += 1
        else:
            print("Nothing to see here, move along.")

    def pop(self):
        if not self.is_empty():
            popped = self.top_node
            self.top_node = popped.get_next_node()
            self.size -= 1
            return popped.get_data()
        else:
            print("WOW! Easy there buddy, it's a full house.")

    def peek(self):
        if not self.is_empty():
            return self.top_node.get_data()
        else:
            print("Nothing to see here, move along.")


colors = ["Red", "Blue", "Green", "Yellow"]
cards = Stack(20)
for i in range(20):
    cards.push(random.choice(colors), random.randint(1, 9))

print("-" * 30)
print("player 1:")
print("-" * 30)

for i in range(5):
    print(str(i + 1) + "- " + cards.pop())

print("-" * 30)
print("player 2:")
print("-" * 30)

for i in range(5):
    print(str(i + 1) + "- " + cards.pop())

print("\n\n")
print("-" * 30)
print("First card in deck:", cards.pop())
print("-" * 30)
