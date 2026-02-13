class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    def merge(self, list2):
        if not self.head:
            self.head = list2.head
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = list2.head


# Program utama
ll1 = LinkedList()
ll2 = LinkedList()

data1 = [1, 3, 5, 7]
data2 = [2, 4, 6, 8]

for item in data1:
    ll1.insert_at_end(item)

for item in data2:
    ll2.insert_at_end(item)

print("Linked List 1:")
ll1.display()

print("Linked List 2:")
ll2.display()

ll1.merge(ll2)

print("Linked List setelah digabungkan:")
ll1.display()
