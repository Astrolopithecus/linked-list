# Miles Philips
# 7-20-19
# Prog 260
# Linked List
# Git Commit?

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if (self.head == None):
            return True
        else:
            return False
    def add(self, data):
        ''' Method to add data to the end of the list'''
        node = Node(data) #Create a node to be added from the data argument
        if (self.isEmpty()):
            #List is empty, set the node to be the head
            self.head = node
        else:
            # Add the new node at the head
            # Set new node's next pointer to self.head
            node.next = self.head

            # Now update the head to be the new node
            self.head = node
            
    def __str__(self):
        ''' Function to get a string representation of the list'''
        retVal = "["
        curr = self.head
        while (curr and curr.next):
            retVal += str(curr) + ","
            curr = curr.next
        retVal += str(curr) if curr else ""
        retVal += "]"
        return retVal
    def size(self):
        '''Return the size of the list'''
        if (self.isEmpty()):
            return 0
        else:
            i = 0
            curr = self.head
            while (curr):
                i += 1
                curr = curr.next
            return i
    
    def search(self,data):
        if (self.isEmpty()):
            return False
        else:
            curr = self.head
            while (curr ):
                if (curr.data == data):
                    return True
                curr = curr.next
            return False

    def remove(self, dataInput):
        ''' Method to remove the node in the list with data attribute
        equal to dataInput from the list.'''
        # Follow the links till the end checking the data field at each node.
        # When the node with dataInput is identified, fix links so that the next pointer
        # of the previous node now points to the next pointer of the identified node.
        # This implies, we need to keep track of previous and current nodes, as
        # we follow the links.

        if (self.isEmpty()):
            # If the list is empty, error case. Raise an exception
            raise KeyError("Data not found in list")
        else:
            #At least one node present in the list
            prev = None
            curr = self.head
            found = False
            while (curr and not found ):
                if (curr.data == dataInput):
                    found = True
                else:
                    prev = curr
                    curr = curr.next
            if (not found): 
                # raise an exception
                raise KeyError("Data not found in list")

            if prev == None:
                #The node with dataInput was the head node.There was no previous node
                # Adjust the head pointer
                self.head = curr.next
            else:
                # Point the next pointer of the previous node to the identified node's next pointer
                # effectively removing the current node
                prev.next = curr.next


    def index(self, dataInput): ##TO BE IMPLEMENTED AS HOMEWORK ##
        '''Method returns the index or position in the list of the node with data attribute equal to dataInput.
        The index or position is zero-based. E.g. self.head is at index/position 0 and the last node has position/index
        of self.size() - 1.
        THe function should return -1 if the list is empty or if the node is not found in the list.
        '''
        if (self.isEmpty()):
            return -1
        
        index = 0
        curr = self.head
        found = False
        while (curr and not found ):
            if (curr.data == dataInput):
                    found = True
            else:
                    index += 1
                    curr = curr.next
        if (not found): 
            # raise an exception
            raise KeyError("Data not found in list")
        else:
            return index

    def insert(self, pos, data): ##TO BE IMPLEMENTED AS HOMEWORK ##
        ''' Method to insert a node with dataInput as data attribute
         in the list at position 'pos' (pos is zero-based index of a node. E.g. self.head is at position 0).
         It should raise an IndexError if pos is negative or >= size of the list'''
         # Validate pos first, if not valid raise IndexError
         # Next, create a new node object with dataInput. 
         # Next, follow the links to get to the node at index = pos. You should keep track of 
         #      the previous node while following the links (similar to remove method) so that
         #      you can adjust pointers of the previous node, the current and the new nodes.
         # Make sure your code works
         #    - when the list is empty (raises IndexError)
         #    - when pos = 0
         #    - when pos = self.size()-1 
         #    - and of course in all other valid values of pos
        temp = Node(data)
        current = self.head
        previous = None
        count = 0
        found = False
        if pos > self.size-1:
            raise IndexError ('Index out of range')
        while current is not None and not found:
            if count == index:
                found = True
            else:
                previous = current
                current = current.next()
                count +=1
        if previous is None:
            temp.next = self.head
            self.head = temp
        else:
            temp.next = current
            previous.next = temp

    def pop(self,pos): ##TO BE IMPLEMENTED AS HOMEWORK ##
        ''' Method to remove and return the data at the node at given position 'pos' in the list.(pos is zero-based index of a node.
         E.g. self.head is at position 0). It should raise an IndexError if pos is negative or >= size of the list'''
         # Validate pos first, if not valid raise IndexError
         # Next, follow the links to get to the node at index = pos. You should keep track of 
         #      the previous node while following the links (similar to remove method) so that
         #      you can adjust pointers of the previous node, the current and the new nodes appropriately.
         #      You should return the data from the node at index = pos.
         # Make sure your code works
         #    - when the list is empty (raises IndexError)
         #    - when pos = 0
         #    - when pos = self.size()-1 
         #    - and of course in all other valid values of pos
        if pos > self.size-1 or pos <0:
             raise IndexError('Index out of range')
        current = self.head
        previous = None
        found = False
        if current:
            count = 0
            while current.next is not None and not found:
                if count == index:
                    found == True
                else:
                    previous = current
                    current = current.next
                    count += 1
            if previous is None:
                self.head = current.next
                return current.data
            else:
                previous.next = current.next
                return current.data
