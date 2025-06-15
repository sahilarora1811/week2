class Node:
    """Represents a node in a singly linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Manages a singly linked list."""

    def __init__(self):
        self.head = None

    def add_node(self, data):
        """Adds a node to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            print(f"Added head: {new_node.data}")
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        print(f"Added node: {new_node.data}")

    def print_list(self):
        """Prints the contents of the list."""
        if not self.head:
            print("List is empty.")
            return
        current = self.head
        print("Linked List:", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        """Deletes the nth node (1-based index) from the list."""
        if not self.head:
            raise Exception("Cannot delete from an empty list.")

        if n <= 0:
            raise IndexError("Index should be a positive integer (1-based).")

        if n == 1:
            print(f"Deleting node at position {n} with value {self.head.data}")
            self.head = self.head.next
            return

        current = self.head
        prev = None
        count = 1

        while current and count < n:
            prev = current
            current = current.next
            count += 1

        if not current:
            raise IndexError(f"Index {n} out of range. List has fewer nodes.")

        print(f"Deleting node at position {n} with value {current.data}")
        prev.next = current.next


# Main program: Menu-driven interface
def main():
    ll = LinkedList()

    while True:
        print("\n----- MENU -----")
        print("1. Add node")
        print("2. Print list")
        print("3. Delete nth node")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            try:
                value = int(input("Enter value to add: "))
                ll.add_node(value)
            except ValueError:
                print("Invalid input! Please enter an integer.")

        elif choice == '2':
            ll.print_list()

        elif choice == '3':
            try:
                index = int(input("Enter position (1-based index) to delete: "))
                ll.delete_nth_node(index)
            except ValueError:
                print("Invalid input! Please enter an integer.")
            except Exception as e:
                print("Error:", e)

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice! Please choose between 1 and 4.")


if __name__ == "__main__":
    main()