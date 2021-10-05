# Linked List Implementation
#7 --> 8  --> 9



# Linked List contains a NodeObject 

class Linked_List:
    def __init__(self):
        self.head = None


class Node:
    # Function to initialise Node Object 
    def __init__(self,value):
        self.value = value
        self.next = None



# Driver Function

if __name__ == '__main__':
    linkedlist = Linked_List()   # Object Creation 
    

    
    linkedlist.head = Node('Sudharsan')
    second          = Node('Karthick')
    third           = Node('Gautham')

    node = linkedlist.head
    #Reference between the nodes 
    linkedlist.head.next = second 

    linkedlist.head.next.next = third 
    
    while node:
        print(node.value)
        node = node.next


    


    print(f"Linked List elements are : { linkedlist.head.value} --> {linkedlist.head.next.value} --> {linkedlist.head.next.next.value}")

