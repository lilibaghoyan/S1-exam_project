class BSTNode:
    """Node of the Binary Search Tree."""
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BST:
    """Basic Binary Search Tree (case-insensitive for keys)."""
    def __init__(self):
        self.root = None

    # INSERT

    def insert(self, key, value=None):
        """Inserts a new key or updates an existing one."""
        self.root, is_new = self._insert(self.root, key, value)
        return is_new

    def _insert(self, node, key, value):
        if node is None:
            return BSTNode(key, value), True

        k = key.lower()
        nk = node.key.lower()

        if k < nk:
            node.left, is_new = self._insert(node.left, key, value)
        elif k > nk:
            node.right, is_new = self._insert(node.right, key, value)
        else:
            # update existing value
            node.value = value
            return node, False

        return node, is_new

    # SEARCH

    def search(self, key):
        """Returns the node with the given key or None."""
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return None

        k = key.lower()
        nk = node.key.lower()

        if k == nk:
            return node
        elif k < nk:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    # DELETE

    def delete(self, key):
        """Deletes the node with the given key."""
        self.root, deleted = self._delete(self.root, key)
        return deleted

    def _delete(self, node, key):
        if node is None:
            return node, False

        k = key.lower()
        nk = node.key.lower()

        if k < nk:
            node.left, deleted = self._delete(node.left, key)
            return node, deleted
        elif k > nk:
            node.right, deleted = self._delete(node.right, key)
            return node, deleted

        # Node found
        if node.left is None:
            return node.right, True
        if node.right is None:
            return node.left, True

        # Two children → find inorder successor
        successor = node.right
        while successor.left:
            successor = successor.left

        node.key, node.value = successor.key, successor.value
        node.right, _ = self._delete(node.right, successor.key)

        return node, True

    # TRAVERSALS

    def inorder(self):
        """Returns (key, value) pairs in sorted order."""
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, out):
        if node:
            self._inorder(node.left, out)
            out.append((node.key, node.value))
            self._inorder(node.right, out)

    def preorder(self):
        """Returns (key, value) pairs in preorder."""
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node, out):
        if node:
            out.append((node.key, node.value))
            self._preorder(node.left, out)
            self._preorder(node.right, out)

    def postorder(self):
        """Returns (key, value) pairs in postorder."""
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node, out):
        if node:
            self._postorder(node.left, out)
            self._postorder(node.right, out)
            out.append((node.key, node.value))

    # TREE VISUALIZER

    def print_tree(self):
        """Prints the tree sideways to show structure clearly."""

        def _print(node, prefix="", is_left=True):
            if node is None:
                return
            _print(node.right, prefix + ("│   " if is_left else "    "), False)
            print(prefix + ("└── " if is_left else "┌── ") + node.key)
            _print(node.left, prefix + ("    " if is_left else "│   "), True)

        if self.root is None:
            print("The tree is empty.")
        else:
            print("\nCurrent Binary Search Tree:")
            _print(self.root)

    # UTILITIES

    def size(self):
        return len(self.inorder())

    def is_empty(self):
        return self.root is None


# CONTACT MANAGER

def print_menu():
    print("\n=== Contact Manager (BST) ===")
    print("1) Add or update a contact")
    print("2) Search for a contact")
    print("3) Delete a contact")
    print("4) Show all contacts (alphabetical)")
    print("5) Show preorder traversal")
    print("6) Show postorder traversal")
    print("7) Show tree statistics")
    print("8) Quit")
    print("9) Show tree visual")


def main():
    tree = BST()

    print("BST Contact Manager")
    print("This program uses a Binary Search Tree to store and manage contacts.")

    while True:
        print_menu()
        choice = input("\nChoose an option: ").strip()

        # Add contact
        if choice == "1":
            name = input("Name: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue

            info = input("Phone/email: ").strip()
            is_new = tree.insert(name, info)

            if is_new:
                print(f"Added: {name} -> {info}")
            else:
                print(f"Updated: {name} -> {info}")

        # Search contact
        elif choice == "2":
            name = input("Name to search: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue
            node = tree.search(name)
            if node:
                print(f"Found: {node.key} -> {node.value}")
            else:
                print("Contact not found.")

        # Delete contact
        elif choice == "3":
            name = input("Name to delete: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue

            if tree.delete(name):
                print(f"Deleted: {name}")
            else:
                print("Contact not found.")

        # Show contacts
        elif choice == "4":
            contacts = tree.inorder()
            if not contacts:
                print("No contacts available.")
            else:
                print("\nContacts:")
                for name, info in contacts:
                    print(f"{name:20} -> {info}")

        # Preorder
        elif choice == "5":
            order = tree.preorder()
            if not order:
                print("Tree is empty.")
            else:
                print("Preorder:", " -> ".join([k for k, _ in order]))

        # Postorder
        elif choice == "6":
            order = tree.postorder()
            if not order:
                print("Tree is empty.")
            else:
                print("Postorder:", " -> ".join([k for k, _ in order]))

        # Stats
        elif choice == "7":
            size = tree.size()
            print("\nTree statistics:")
            print("Number of contacts:", size)
            print("Is empty:", tree.is_empty())
            if size > 0:
                contacts = tree.inorder()
                print("First contact:", contacts[0][0])
                print("Last contact:", contacts[-1][0])

        # Quit
        elif choice == "8":
            print("Exiting program.")
            break

        # Visual tree
        elif choice == "9":
            tree.print_tree()

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
