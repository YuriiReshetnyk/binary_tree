
from student import Student


class node:

    def __init__(self, student: Student):
        self.right = None
        self.left = None
        self.parent = None
        self.student = student

    def find_node_by_rating(self, rating: int):
        # пошук вузла по ключу
        if rating < self.student.rating and self.left:
            return self.left.find_node_by_rating(rating)
        if rating > self.student.rating and self.right:
            return self.right.find_node_by_rating(rating)
        if rating == self.student.rating:
            return self
        return None

    def __go_max_left(self, node):
        if node.left is None:
            return node
        self.__go_max_left(node.left)

    def delete_node(self):
        if self.right is None and self.left is None: # without childs
            if self.parent.right is self:
                self.parent.right = None
            if self.parent.left is self:
                self.parent.left = None
        elif self.left is None:
            self.right.parent = self.parent
            if self.parent.right is self:
                self.parent.right = self.right
            if self.parent.left is self:
                self.parent.left = self.right
        elif self.right is None:
            self.left.parent = self.parent
            if self.parent.right is self:
                self.parent.right = self.left
            if self.parent.left is self:
                self.parent.left = self.left
            return self
        else:
            #         5
            #       /   \
            #      1     10
            #     / \   /  \
            #    0   3 9   11
            #       / \
            #      2   4
            max_left_child = self.__go_max_left(self.right)
            max_left_child.left = self.left

            self.right.parent = self.parent
            if self.parent is not None:
                if self.parent.right is self:
                    self.parent.right = self.right
                if self.parent.left is self:
                    self.parent.left = self.right
        del self

    def print_nodes(self):
        if self.right:
            self.right.print_nodes()
        if self.left:
            self.left.print_nodes()
        print(self.student)
