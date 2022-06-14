from binary_tree import binary_tree
from student import Student


def main():
    student1 = Student("Reshetnyk", "Yurii", 11, 2004, 4)
    student2 = Student("Buchko", "Ustum", 14, 2003, 2)
    student3 = Student("Zavadka", "Bogdan", 13, 2002, 3)
    student4 = Student("Rozhankivskyy", "Yurii", 12, 2004, 5)
    student5 = Student("Shiyka", "Ostab", 11, 2005, 1)
    new_binary_tree = binary_tree()
    new_binary_tree.insert(student1)
    new_binary_tree.insert(student2)
    new_binary_tree.insert(student3)
    new_binary_tree.insert(student4)
    new_binary_tree.insert(student5)
    print(new_binary_tree.find_by_rating(5).student)
    print("_____________________________________")
    new_binary_tree.print_tree()
    print("_____________________________________")
    new_binary_tree.print_with_greater_rating(2)
    print("_____________________________________")
    new_binary_tree.inorder()
    print("_____________________________________")
    new_binary_tree.delete_everyone_with_group(12)
    new_binary_tree.print_tree()
    print("_____________________________________")
    new_binary_tree.delete_tree()
    new_binary_tree.print_tree()


if __name__ == '__main__':
    main()
