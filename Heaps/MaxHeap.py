#Max Heap is a tree where the child is always smaller than the parent

class MaxHeap:
    def __init__(self):
        self.list = [None]
        self.count = 0

    // Use for heapify up, when you insert elements
    def get_parent_idx(self, idx):
        return idx//2

    // Use for heapify down, when u remove element
    def get_left_child_idx(self, idx):
        return idx*2 

    // Use for heapify down, when u remove element
    def get_right_child_idx(self, idx):
        return idx*2 + 1

    // Use for heapify down, when u remove element
    def child_present(self, idx):
       return self.get_left_child_idx(idx) <= self.count

    // Use for heapify down, when u remove element
    def get_larger_child_idx(self, idx):
        left_child_idx = self.get_left_child_idx(idx)
        right_child_idx = self.get_right_child_idx(idx)
        if right_child_idx > self.count:
            return left_child_idx
        else:
            if self.list[left_child_idx] >= self.list[right_child_idx]:
                return left_child_idx

            elif self.list[right_child_idx] > self.list[left_child_idx]:
                return right_child_idx



    #Insert Element
    def push(self,element):
        self.list.append(element)
        self.count += 1
        if len(self.list) > 1:
           self.heapify_up()
    
    // Compare lowest element see if bigger/smaller then top elements
    def heapify_up(self):
        idx = self.count
        while self.get_parent_idx(idx):
            parent_idx = self.get_parent_idx(idx)
            if self.list[idx] > self.list[parent_idx]:
                self.list[idx],self.list[parent_idx] = self.list[parent_idx],self.list[idx]
                idx = parent_idx
                parent_idx = self.get_parent_idx(idx)
            else: 
                break
            

    #Remove Maximum Element
    def retrieve_max(self):
        value_to_retrieve = self.list[1]
        self.list[1] = self.list[-1]
        self.list.pop()
        self.count -= 1
        self.heapify_down()
        return value_to_retrieve
        
        
    
    def heapify_down(self):
        idx = 1
        while self.child_present(idx):
            child_idx = self.get_larger_child_idx(idx)
            if self.list[child_idx] > self.list[idx]:
                self.list[child_idx], self.list[idx] = self.list[idx], self.list[child_idx]
                idx = child_idx
            else: 
                break
            






