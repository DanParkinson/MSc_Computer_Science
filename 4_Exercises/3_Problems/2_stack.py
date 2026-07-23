
class Stack():
    def __init__(self, size = 1000):
        self._stack = [None] * size
        self._top_index = 0

    def is_empty(self):
        return self._top_index == 0
    
    def pop(self):
        if self.is_empty():
            return None
        
        item = self._stack[self._top_index - 1]
        self._stack[self._top_index - 1] = None
        self._top_index -= 1

        return item 
    
    def push(self, element):
        if self._top_index == len(self._stack):
            self.resize_up()
        self._stack[self._top_index] = element
        self._top_index += 1

    def resize_up(self):
        new_stack = [None] * (2 * len(self._stack))

        for i in range(self._top_index):
            new_stack[i] = self._stack[i]
        self._stack = new_stack

    

