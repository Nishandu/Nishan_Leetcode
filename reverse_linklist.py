class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

def reverseList(head):
    curr = head
    prev = None
    
    while curr:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode
    
    return prev

def printList(node):
    while node is not None:
        print(node.data, end="")
        if node.next is not None:
            print(" -> ", end="")
        node = node.next
    print()

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)

    print("Original List:")
    printList(head)

    head = reverseList(head)

    print("Reversed List:")
    printList(head)