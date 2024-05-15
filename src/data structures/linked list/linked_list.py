# Node class of a linked list
class Node:
   
    def __init__(self, data):
        self.data = data 
        self.next = None 

class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):

        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return
        
        current_node = self.head

        while current_node.next:
            current_node = current_node.next
 
        current_node.next = new_node
        return
    
    def length(self):
        if self.head == None:
            return 0
        current_node = self.head
        total = 0 
        while current_node:
            total += 1
            current_node = current_node.next
        return total

    def to_list(self):

        node_data = []
        current_node = self.head

        while current_node:
            node_data.append(current_node.data)
            current_node = current_node.next
        return node_data
    def get(self, index):
        if index >= self.length() or index < 0:
            print("ERROR: 'Get' Index out of range!")
            return None
        current_idx  = 0
        current_node = self.head
        while current_node != None:
            if current_idx == index: 
                return current_node.data
            current_node  = current_node.next
            current_idx += 1
    def reverse_linkedlist(self):
        previous_node = None
        current_node = self.head
        while current_node != None:
            next = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next
        self.head = previous_node
    
    def search_item(self, value):
        if self.head == None:
            print("List has no elements")
            return
        current_node = self.head
        while current_node != None:
            if current_node.data == value:
                print("Item found")
                return True
            current_node = current_node.next
        print("Item not found")
        return False

    def display(self): 
        contents = self.head 
        if contents is None:
            print("List has no element")
        while contents: 
            print(contents.data)
            contents = contents.next
        print("----------") 

    def remove_at_start(self):
        if self.head == None:
            print("The list has no element to delete")
            return 
        self.head = self.head.next
    
    def remove_at_end(self):
        if self.head is None:
            print("The list has no element to delete")
            return
        current_node = self.head
        while current_node.next.next != None:
            current_node = current_node.next
        current_node.next = None

    def remove_element_by_value(self, value):
        current_node = self.head  
  
        if current_node != None:  
            if current_node.data == value:  
                self.head = current_node.next
                current_node = None
                return
  
        while current_node != None:  
            if current_node.data == value:  
                break
            prev = current_node  
            current_node = current_node.next
   
        if current_node == None:  
            return
   
        prev.next = current_node.next
        current_node = None
    
    def insert_at_start(self, data):
        new_node        = Node(data)
        new_node.next   = self.head
        self.head = new_node
  
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def insert_at_index (self, index, data):
        if index == 1:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        i = 1
        current_node = self.head
        while i < index-1 and current_node is not None:
            current_node = current_node.next
            i = i + 1
        if current_node is None:
            print("ERROR: Index out of range!")
        else: 
            new_node = Node(data)
            new_node.next = current_node.next 
            current_node.next  = new_node
	
# Test   
my_list = LinkedList()
my_list.display()
my_list.append(3)
my_list.append(2)
my_list.append(7)
my_list.append(1)

my_list.display()

print("The total number of elements are: " + str(my_list.length()))
print(my_list.to_list()) 
print("---------")
my_list.reverse_linkedlist() 
my_list.display()

my_list.search_item(7)
my_list.search_item(77)

my_list.remove_at_start()
my_list.display()

my_list.remove_at_end()
my_list.display()

my_list.insert_at_start(1)
my_list.display()

my_list.insert_at_end(3)
my_list.display()

my_list.remove_element_by_value(3)
my_list.display()

my_list.insert_at_index(2, 88)
my_list.display()
