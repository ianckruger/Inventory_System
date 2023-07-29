# Inventory System via Binary Search Tree.

class TreeNode:
    _quantity = int
    _name = str
    _leftNode = None
    _rightNode = None

    def __init__(self, quantity: int, name: str, left=None, right=None):
        self._quantity = quantity
        self._name = name
        self._leftNode = left
        self._rightNode = right


class InventorySystem:
    root = None

    def __init__(self, root=None):
        self.root = root

    def addNodeA(self, quantity, name):
        if self.root is None:
            self.root = TreeNode(quantity, name)
        else:
            self.addNodeB(self.root, quantity, name)

    def addNodeB(self, current, quantity, name):
        if name == current._name:
            current._quantity += quantity
        elif name < current._name:
            if current._leftNode is None:
                current._leftNode = TreeNode(quantity, name)
            else:
                self.addNodeB(current._leftNode, quantity, name)
        else:
            if current._rightNode is None:
                current._rightNode = TreeNode(quantity, name)
            else:
                self.addNodeB(current._rightNode, quantity, name)

    def removeNode(self, name, quantity):
        current = self.root
        if self.root is None:
            print(f"Item not found. Make sure {name} is the correct item.")
        else:
            self.searchToRemove(current, name, quantity)

    def searchToRemove(self, current, name, quantity):
        if current is None:
            print(f"Item not found. Make sure {name} is the correct item.")

        elif name < current._name:
            self.searchToRemove(current._leftNode, name, quantity)
        elif name > current._name:
            self.searchToRemove(current._rightNode, name, quantity)
        else:
            if current._quantity >= quantity:
                current._quantity -= quantity
                if current._quantity <= 0:
                    self.deleteNode(current)
            elif current._quantity < quantity:
                print(
                    f"Not enough of item {current._name}. There is {current._quantity} of item. Would you like to delete item?")
                answer = input("Y/N: ")
                if answer == "Y":
                    self.deleteNode(current)
                elif answer == "N":
                    print(f"{current._name} will remain at {current._quantity} amount.")

    def deleteNode(self, node):
        if node._leftNode is None and node._rightNode is None:
            node = None
        elif node._leftNode is None:
            node._rightNode = node
        elif node._rightNode is None:
            node._leftNode = node
        else:
            min_item = self.findMin(node._rightNode)
            node._name = min_item.name
            node._quantity = min_item.quantity
            self.deleteNode(min_item)

    def findMin(self, current):
        while current._leftNode is not None:
            current = current._leftNode
        return current
    
    def findMax(self,current):
        while current._rightNode is not None:
            current = current._rightNode
        return current

    def showInventory(self):
        self.searchInventory(self.root)

    def searchInventory(self, current, query, results):
        if current is not None:
            self.searchInventory(current._leftNode, query, results)

            if query.lower() in current._name.lower():
                results.append((current._name, current._quantity))

            self.searchInventory(current._rightNode, query, results)

    def searchByName(self, query):
        results = []
        self.searchInventory(self.root, query, results)
        return results
    
    def addItem(self, name, quantity):
        self.addNodeA(quantity, name)




