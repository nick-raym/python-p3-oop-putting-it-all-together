#!/usr/bin/env python3

class Shoe:
    def __init__(self,brand,size,condition="torn"):
        self.brand=brand
        self.size=size
        self.condition=condition
    
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition="New"

    def get_size(self):
        print("Retrieving page Count.")
        return self._size
    
    def set_size(self,size):
        if (type(size)==(int)):
            print(f"Setting size to { size }.")
            self._size = size

        else:
            print("size must be an integer")
    size = property(get_size, set_size)