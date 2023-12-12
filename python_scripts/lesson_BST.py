import random


class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left_tree = None
        self.right_tree = None

    def insert(self, data):
        if self.data != data:  # Is root node != data?
            if data < self.data:
                # insert to left_tree
                if self.left_tree:
                    self.left_tree.insert(data)
                else:
                    self.left_tree = BinarySearchTree(data)
            else:
                # insert to right_tree
                if self.right_tree:
                    self.right_tree.insert(data)
                else:
                    self.right_tree = BinarySearchTree(data)

    def delete(self, data):
        if data < self.data:
            if self.left_tree:
                self.left_tree = self.left_tree.delete(data)
            else:  # 沒有這個數字
                print(f"Delete {data} fail: data not found")
            result_tree = self
        elif data > self.data:
            if self.right_tree:
                self.right_tree = self.right_tree.delete(data)
            else:  # 沒有這個數字
                print(f"Delete {data} fail: data not found")
            result_tree = self
        else:
            # data == self.data
            # 找人遞補我當前這個空缺
            if self.left_tree == None and self.right_tree == None:  # 1. 無子樹
                result_tree = None
            elif self.left_tree == None and self.right_tree != None:  # 2 只有右子樹
                result_tree = self.right_tree
            elif self.left_tree != None and self.right_tree == None:  # 2 只有左子樹
                result_tree = self.left_tree
            else:
                # 3. 左右子樹都在, 找右子樹最小值遞補
                substitute = self.right_tree  # 右子樹根節點
                while substitute.left_tree != None:
                    substitute = substitute.left_tree
                self.data = substitute.data  # 更改成遞補值
                self.right_tree = self.right_tree.delete(substitute.data)
                result_tree = self

        return result_tree

    def search(self, data):  # 有無找到: 有的話return True,  沒有的話 return False
        if data < self.data:
            is_find = \
                self.left_tree.search(data) if self.left_tree else False
        elif data > self.data:
            is_find = \
                self.right_tree.search(data) if self.right_tree else False
        else:
            # data == self.data
            is_find = True

        return is_find

    def traverse_preorder(self, root):
        traversal_order = list()
        if root:
            traversal_order.append(root.data)
            traversal_order += self.traverse_preorder(root.left_tree)
            traversal_order += self.traverse_preorder(root.right_tree)

        return traversal_order

    def traverse_inorder(self, root):
        traversal_order = list()
        if root:
            traversal_order += self.traverse_inorder(root.left_tree)
            traversal_order.append(root.data)
            traversal_order += self.traverse_inorder(root.right_tree)

        return traversal_order

    def traverse_postorder(self, root):
        traversal_order = list()
        if root:
            traversal_order += self.traverse_postorder(root.left_tree)
            traversal_order += self.traverse_postorder(root.right_tree)
            traversal_order.append(root.data)

        return traversal_order


if __name__ == '__main__':
    insert_order = random.sample(range(1, 20), 7)
    print("Insert Order:", insert_order)

    bst = BinarySearchTree(insert_order[0])
    for data in insert_order[1:]:
        print("Insert:", data)
        bst.insert(data)

    print("PreOder Traversal: ", bst.traverse_preorder(bst))
    print("InOder Traversal: ", bst.traverse_inorder(bst))
    print("PostOder Traversal: ", bst.traverse_postorder(bst))

    # Test Search
    print("Test Search Start.")
    targets_must_be_found = random.sample(insert_order, 5)
    for target in targets_must_be_found:
        # 方法一
        if bst.search(target) == False:
            print("Something goes wrong.")

        # 方法二
        assert bst.search(target) == True, print(
            "Something goes wrong. by Assert")

    targets_must_not_be_found = [
        -1 * sample for sample in random.sample(insert_order, 5)]

    for fake_target in targets_must_not_be_found:
        assert bst.search(fake_target) == False, print(
            "Something goes wrong. by Assert")

    print("Test Search Done.")
