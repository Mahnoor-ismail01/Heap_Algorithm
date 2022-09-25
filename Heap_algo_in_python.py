import math

#defining a class Max_Heap for the heap data structure

class Max_Heap: 
    def __init__(self, sizelimit):
        # size limit of heap
        self.sizelimit = sizelimit
        # current heap size = 0
        self.heap_size = 0
        # making a list of 0s for heap with given size+1
        self.heap = [0]*(self.sizelimit + 1)
        # inserting first element to a max inf
        self.heap[0] = math.inf
        # first element i.e. root will be of index 1 in list
        self.root = 1
        

    # helper function to swap the two given nodes of the heap
    # this function will be needed for max-heapify and insertion
    # in order to swap nodes which are not in order (not satisfy max-heap property)
    def swap_nodes(self, node1, node2):
        self.heap[node1], self.heap[node2] = self.heap[node2], self.heap[node1]


# (1)
    # THE MAX_HEAPIFY FUNCTION
    def max_heapify(self, i):
        # If the node is a not a leaf node and is lesser than any of its child
        if not (i >= (self.heap_size//2) and i <= self.heap_size):

            # if node is less tha its right child or left child
            if (self.heap[i] < self.heap[2 * i]  or  self.heap[i] < self.heap[(2 * i) + 1]): 
                if self.heap[2 * i] > self.heap[(2 * i) + 1]:
                    # Swap the node with the left child and call the max_heapify function on it
                    self.swap_nodes(i, 2 * i)
                    self.max_heapify(2 * i)
 
                else:
                    # Swap the node with right child and then call the max_heapify function on it
                    self.swap_nodes(i, (2 * i) + 1)
                    self.max_heapify((2 * i) + 1)


# (2)
    # THE INSERT_MAXHEAP FUNCTION TO INSERT A NODE
    def insert_MaxHeap(self, element):

        # check if heap is full then return
        if self.heap_size >= self.sizelimit:
            return

        # increasing heap size
        self.heap_size+= 1
        # adding new element to the last
        self.heap[self.heap_size] = element
        # current var equal to the heap size
        current = self.heap_size
        # while the current value is greater than its previous
        while self.heap[current] > self.heap[current//2]:
            # swapping them
            self.swap_nodes(current, current//2)
            # making current equal to its previous
            current = current//2


# (3)
    # THE BUILD_MAX_HEAP FUNCTION TO REMOVE THE MAX NODE AND HEAPIFY
    def build_max_heap(self):

        # getting the root/max node
        last = self.heap[self.root]
        # replacing it with the last node
        self.heap[self.root] = self.heap[self.heap_size]
        # making last node in heap which is replace above from max node to be equal to 0
        self.heap[self.heap_size] = 0
        # decreasing the heap size as a node is removed
        self.heap_size -= 1
        # performing max_heapify to sort
        self.max_heapify(self.root)


# (4)
    # THE EXTRACT_HEAP_MAX FUNCTION TO REMOVE ANY NODE AND HEAPIFY
    def extract_HeapMax(self,element):

        # getting the index of the node to remove
        dell = self.heap.index(element)
        # replacing it with the last node
        self.heap[dell] = self.heap[self.heap_size]
        # making last node in heap which is replace above from the node to be equal to 0
        self.heap[self.heap_size] = 0
        # applying max_heapify to sort
        self.max_heapify(dell)


# (5)
    # THE HEAP_INCREASE_KEY FUNCTION TO INCREASE THE VALUE OF A GIVEN NODE
    def heap_increase_key(self,element):

        # getting the index of the given node
        ind = self.heap.index(element)
        # increasing its value
        self.heap[ind] += 1
        # applying max_heapify to sort
        self.max_heapify(ind)

            
 
    # THE PRINT_HEAP FUNCTION TO PRINT THE HEAP
    def print_heap(self):
        for i in range(1,(self.heap_size//2)+1):
            if i == 1:
                print('\n\t\t',self.heap[i],'\n\t',self.heap[2*i],'\t\t',self.heap[2*i+1])
            elif i%2 == 0 and i < 3:
                print('\n   ',self.heap[2*i],'\t    ',self.heap[2*i+1])

            elif i%2 == 0 and i > 3:
                print(self.heap[2*i],'\t',self.heap[2*i+1])

            else:
                print('\t\t   ',self.heap[2*i],'\t    ',self.heap[2*i+1])
        print('\n')


# creating object for Max_Heap Class with max length 10 of heap.
maxHeap = Max_Heap(10)
print('\n USING INSERT MAX HEAP TO INSERT VALUES')
# inserting nodes in the heap using insert_MaxHeap Function
maxHeap.insert_MaxHeap(15)
maxHeap.insert_MaxHeap(7)
maxHeap.insert_MaxHeap(9)
maxHeap.insert_MaxHeap(4)
maxHeap.insert_MaxHeap(19)
maxHeap.insert_MaxHeap(2)
maxHeap.insert_MaxHeap(1)
maxHeap.insert_MaxHeap(13)
print('\n PERFORMING MAX HEAPIFY TO SORT')
print('\n PRINTING HEAP')
maxHeap.print_heap()

# using build_max_heap function to remove the max node from the heap and performing max_heapify to sort
maxHeap.build_max_heap()
print('\n AFTER BUILD MAX HEAP (when max node is removed)')
maxHeap.print_heap()

# using extract_HeapMax Function to remove the given node and performing max_heapify
maxHeap.extract_HeapMax(7)
print('\n AFTER EXTRACT HEAP MAX (removing any node - here 7)')
maxHeap.print_heap()

# using heap_increase_key function to increase the value of a node - here increasing 9 and then performing max_hapify
maxHeap.heap_increase_key(9)
print('\n AFTER HEAP INCREASE KEY (increase value at node - here increasing 9)')
maxHeap.print_heap()
