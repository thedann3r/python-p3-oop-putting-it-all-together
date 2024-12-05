#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    def get_size(self):
        return self._size
    
    def set_size(self,size):
        if(isinstance(size,(int,float)) and size > 0):
            self._size = size
        else:
            print("size must be an integer")   

    size = property(get_size,set_size)  

    def cobble(self):
        print("Your shoe is as good as new!") 

    def cobble_makes_new(self,condition):
        self.condition = condition 

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")     
    
stan_smith = Shoe("Adidas",9)
