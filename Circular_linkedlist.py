class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert node at the end
    def insert(self, data):
        new_node = Node(data)

        # If list is empty
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head

        # Traverse to last node
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    # Print circular linked list
    def print_list(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            if temp == self.head:
                break

        print("(head)")


# Driver Code
cll = CircularLinkedList()

cll.insert(1)
cll.insert(2)
cll.insert(3)
cll.insert(4)

cll.print_list()