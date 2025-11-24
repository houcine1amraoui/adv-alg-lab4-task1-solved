from bst import BST
bst = BST()

assert bst.search_iterative(5) == True
assert bst.search_iterative(20) == False
assert bst.search_recursive(8) == True
assert bst.search_recursive(99) == False

assert bst.level_order() == [7, 4, 9, 2, 5, 8, 12, 0, 16]
assert bst.pre_order()   == [7, 4, 2, 0, 5, 9, 8, 12, 16]
assert bst.in_order()    == [0, 2, 4, 5, 7, 8, 9, 12, 16]
assert bst.post_order()  == [0, 2, 5, 4, 8, 16, 12, 9, 7]
