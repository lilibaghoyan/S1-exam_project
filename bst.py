# bst_contacts.py – Enhanced Version with Tree Visualizer (Official Style)

class BSTNode:
    """One node of the Binary Search Tree."""
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BST:
    """Simple unbalanced Binary Search Tree with case-insensitive comparisons."""
    def __init__(self):
        self.root = None

    # ---------- INSERT ----------

    def insert(self, key, value=None):
        """Public insert method. Returns True if new insert, False if update."""
        self.root, is_new = self._insert(self.root, key, value)
        return is_new

    def _insert(self, node, key, value):
        """Recursive insert helper (case-insensitive)."""
        if node is None:
            return BSTNode(key, value), True

        key_lower = key.lower()
        node_key_lower = node.key.lower()

        if key_lower < node_key_lower:
            node.left, is_new = self._insert(node.left, key, value)
        elif key_lower > node_key_lower:
            node.right, is_new = self._insert(node.right, key, value)
        else:
            node.value = value
            return node, False

        return node, is_new

    # ---------- SEARCH ----------

    def search(self, key):
        """Returns the node with given key, or None (case-insensitive)."""
        return self._search(self.root, key)

    def _search(self, node, key):
        """Recursive search helper."""
        if node is None:
            return None

        key_lower = key.lower()
        node_key_lower = node.key.lower()

        if key_lower == node_key_lower:
            return node
        if key_lower < node_key_lower:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    # ---------- DELETE ----------

    def delete(self, key):
        """Deletes node with key. Returns True if deleted, False if not found."""
        self.root, deleted = self._delete(self.root, key)
        return deleted

    def _delete(self, node, key):
        """Recursive delete helper."""
        if node is None:
            return node, False

        key_lower = key.lower()
        node_key_lower = node.key.lower()

        if key_lower < node_key_lower:
            node.left, deleted = self._delete(node.left, key)
            return node, deleted

        if key_lower > node_key_lower:
            node.right, deleted = self._delete(node.right, key)
            return node, deleted

        # Node found
        if node.left is None:
            return node.right, True
        if node.right is None:
            return node.left, True

        # Two children: replace with inorder successor
        successor = node.right
        while successor.left:
            successor = successor.left

        node.key, node.value = successor.key, successor.value
        node.right, _ = self._delete(node.right, successor.key)

        return node, True

    # ---------- TRAVERSALS ----------

    def inorder(self):
        """Returns list of (key, value) in sorted order."""
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, out):
        if node is None:
            return
        self._inorder(node.left, out)
        out.append((node.key, node.value))
        self._inorder(node.right, out)

    def preorder(self):
        """Returns list of (key, value) in preorder."""
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node, out):
        if node is None:
            return
        out.append((node.key, node.value))
        self._preorder(node.left, out)
        self._preorder(node.right, out)

    def postorder(self):
        """Returns list of (key, value) in postorder."""
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node, out):
        if node is None:
            return
        self._postorder(node.left, out)
        self._postorder(node.right, out)
        out.append((node.key, node.value))

    # ---------- TREE VISUALIZATION ----------

    def print_tree(self):
        """Prints the tree structure sideways in a clear textual format."""

        def _print(node, prefix="", is_left=True):
            if node is None:
                return
            _print(node.right, prefix + ("│   " if is_left else "    "), False)
            print(prefix + ("└── " if is_left else "┌── ") + node.key)
            _print(node.left, prefix + ("    " if is_left else "│   "), True)

        if self.root is None:
            print("Tree is empty. No structure to display.")
        else:
            print("\nBinary Search Tree Structure:")
            _print(self.root)

    # ---------- UTILITY ----------

    def size(self):
        return len(self.inorder())

    def is_empty(self):
        return self.root is None


# =========================
#   CONTACT MANAGER
# =========================

def print_menu():
    print("\n=== Contact Manager (BST) ===")
    print("1) Add or update contact")
    print("2) Search contact")
    print("3) Delete contact")
    print("4) List all contacts (alphabetical order)")
    print("5) Show preorder traversal")
    print("6) Show postorder traversal")
    print("7) Show tree statistics")
    print("8) Quit")
    print("9) Show tree visual representation")


def main():
    tree = BST()

    print("Binary Search Tree Contact Manager")
    print("This program demonstrates BST operations for educational purposes.")

    while True:
        print_menu()
        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            name = input("Name: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue

            info = input("Phone or email: ").strip()
            is_new = tree.insert(name, info)

            if is_new:
                print(f"Contact added: {name} -> {info}")
            else:
                print(f"Contact updated: {name} -> {info}")

        elif choice == "2":
            name = input("Name to search: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue

            node = tree.search(name)
            if node:
                print(f"Contact found: {node.key} -> {node.value}")
            else:
                print(f"Contact '{name}' not found.")

        elif choice == "3":
            name = input("Name to delete: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue

            if tree.delete(name):
                print(f"Contact '{name}' deleted.")
            else:
                print(f"Contact '{name}' not found. No deletion performed.")

        elif choice == "4":
            contacts = tree.inorder()
            if not contacts:
                print("No contacts available.")
            else:
                print("\nContacts in alphabetical order:")
                for name, info in contacts:
                    print(f"{name:20} -> {info}")

        elif choice == "5":
            contacts = tree.preorder()
            if not contacts:
                print("Tree is empty.")
            else:
                print("\nPreorder traversal:")
                print(" -> ".join([name for name, _ in contacts]))

        elif choice == "6":
            contacts = tree.postorder()
            if not contacts:
                print("Tree is empty.")
            else:
                print("\nPostorder traversal:")
                print(" -> ".join([name for name, _ in contacts]))

        elif choice == "7":
            size = tree.size()
            print("\nTree Statistics:")
            print(f"Total contacts: {size}")
            print(f"Tree empty: {tree.is_empty()}")
            if size > 0:
                contacts = tree.inorder()
                print(f"First (alphabetically): {contacts[0][0]}")
                print(f"Last (alphabetically): {contacts[-1][0]}")

        elif choice == "8":
            print("Program terminated.")
            break

        elif choice == "9":
            tree.print_tree()

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
