class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  
  def set_next_node(self, next_node):
    self.next_node = next_node

# LinkedList class
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
# Add insert_beginning and stringify_list methods below:

  def insert_beginning(self, new_values):
    new_node = Node(new_values)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
  def stringify_list(self):
    string_list = ""
    current_node = self.head_node
    while current_node:
      string_list += str(current_node.value) + "\n"
      current_node = current_node.next_node
    return string_list
  

# Test  code by uncommenting the statements below
ll = LinkedList(5)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)
print(ll.stringify_list())