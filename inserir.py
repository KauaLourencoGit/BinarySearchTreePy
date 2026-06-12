from no import No

class Inserir:
    
    def insert(self, value):
        if self.value:
            
            if value < self.value:
                if self.left is None:
                    self.left = No(value)
                else:
                    self.left.insert(value)
           
            elif value > self.value:
                if self.right is None:
                    self.right = No(value)
                else:
                    self.right = No(value)
        
        else:
            self.value = value 