from no import Nó

raiz = Nó(5)
raiz.insert(10)
raiz.insert(4)
raiz.insert(3)
raiz.insert(6)
raiz.insert(8)
raiz.insert(12)

inorder = raiz.inorder_traversal(raiz)
print(inorder)

preorder = raiz.preorder_traversal(raiz)
print(preorder)

postorder = raiz.postorder_traversal(raiz)
print(postorder)