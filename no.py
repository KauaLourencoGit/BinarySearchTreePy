
class Nó:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        
    # Inserção de um novo nó na árvore
    def insert(self, value):
        if self.value:
            
            if value < self.value:
                if self.left is None:
                    self.left = Nó(value)
                else:
                    self.left.insert(value)
           
            elif value > self.value:
                if self.right is None:
                    self.right = Nó(value)
                else:
                    self.right.insert(value)
        
        else:
            self.value = value
            
    # Percurso em ordem (inorder)
    def inorder_traversal(self, raiz):
        res  = []
        if raiz:
            res = self.inorder_traversal(raiz.left)
            res.append(raiz.value)
            res = res + self.inorder_traversal(raiz.right)
        return res
    
    # Percurso pré-ordem (preorder)
    def preorder_traversal(self, raiz):
        res  = []
        if raiz:
            res.append(raiz.value)
            res = res + self.preorder_traversal(raiz.left)
            res = res + self.preorder_traversal(raiz.right)
        return res
    
    # Percurso pós-ordem (postorder)
    def postorder_traversal(self, raiz):
        res  = []
        if raiz:
            res = self.postorder_traversal(raiz.left)
            res = res + self.postorder_traversal(raiz.right)
            res.append(raiz.value)
        return res