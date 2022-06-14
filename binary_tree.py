from node import node
from student import Student


class binary_tree:

    def __init__(self):
        self.root = None

    def insert(self, student: Student):
        # вставка вузла за рейтингом
        if self.root is None:
            self.root = node(student)
        else:
            current_node = self.root
            while True:
                if student.rating < current_node.student.rating:
                    if current_node.left is None:
                        current_node.left = node(student)
                        current_node.left.parent = current_node
                        break
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = node(student)
                        current_node.right.parent = current_node
                        break
                    else:
                        current_node = current_node.right

    def find_by_rating(self, rating: int):
        if self.root:
            return self.root.find_node_by_rating(rating)
        return None

    def __delete_all_node(self, nodes):
        if nodes:
            self.__delete_all_node(nodes.left)
            self.__delete_all_node(nodes.right)
            del nodes

    def delete_tree(self):
        # знищення дерева.
        if self.root:
            self.__delete_all_node(self.root.left)
            self.__delete_all_node(self.root.right)
            self.root = None

    def print_tree(self):
        # вивід всіх вузлів
        if self.root is None:
            print("Root is not defined")
        else:
            if self.root.right:
                self.root.right.print_nodes()
            if self.root.left:
                self.root.left.print_nodes()
            print(self.root.student)

    def __make_to_list(self, node=None, nlist=None):
        if nlist is None:
            nlist = []
        if node is not None:
            nlist.append(node)
            self.__make_to_list(node.right, nlist)
            self.__make_to_list(node.left, nlist)

    def __to_list(self):
        list_of_nodes = []
        if self.root:
            list_of_nodes.append(self.root)
            self.__make_to_list(self.root.right, list_of_nodes)
            self.__make_to_list(self.root.left, list_of_nodes)
        return list_of_nodes

    def __find_nodes_by_group(self, group):
        list_of_nodes = self.__to_list()
        list_of_nodes_with_group = []
        for nodes in list_of_nodes:
            if nodes.student.group == group:
                list_of_nodes_with_group.append(nodes)
        return list_of_nodes_with_group

    def delete_everyone_with_group(self, group: int):
        list_of_group = self.__find_nodes_by_group(group)
        for nodes in list_of_group:
            if nodes == self.root:
                if self.root.right is not None:
                    self.root = self.root.right
                else:
                    self.root = self.root.left
            nodes.delete_node()

    def print_with_greater_rating(self, rating: int):

        integer = 0
        while True:
            found_student = self.find_by_rating(rating - integer)
            if found_student is None:
                break
            else:
                print(found_student.student)
            integer += 1

    def __in_order(self, nodes):
        if nodes is not None:
            self.__in_order(nodes.left)
            print(nodes.student)
            self.__in_order(nodes.right)

    def inorder(self):
        if self.root is not None:
            self.__in_order(self.root.left)
            print(self.root.student)
            self.__in_order(self.root.right)
