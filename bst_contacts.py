# bst_contacts.py 

class BSTNode:
    """One node of the Binary Search Tree."""
    def __init__(self, key, value=None):
        self.key = key          # e.g. contact name (string)
        self.value = value      # e.g. phone/email (string)
        self.left = None        # left child
        self.right = None       # right child


class BST:
    """Simple unbalanced Binary Search Tree with case-insensitive comparisons."""
    def __init__(self):
        self.root = None

    # ---------- INSERT ----------

    def insert(self, key, value=None):
        """
        Public insert method.
        Returns True if new insert, False if update.
        """
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
        """Recursive search helper (case-insensitive)."""
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
        """
        Deletes the node with given key (case-insensitive).
        Returns True if deleted, False if not found.
        """
        self.root, deleted = self._delete(self.root, key)
        return deleted

    def _delete(self, node, key):
        """Recursive delete helper (case-insensitive)."""
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

        # ---- node found ----
        # Case 1: no left child
        if node.left is None:
            return node.right, True

        # Case 2: no right child
        if node.right is None:
            return node.left, True

        # Case 3: two children
        # Replace with inorder successor (smallest in right subtree)
        succ = node.right
        while succ.left:
            succ = succ.left

        # copy successor data into this node
        node.key, node.value = succ.key, succ.value

        # delete successor node from right subtree
        node.right, _ = self._delete(node.right, succ.key)

        return node, True

    # ---------- TRAVERSALS ----------

    def inorder(self):
        """Returns list of (key, value) in sorted order by key."""
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, out):
        if not node:
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
        if not node:
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
        if not node:
            return
        self._postorder(node.left, out)
        self._postorder(node.right, out)
        out.append((node.key, node.value))

    # ---------- UTILITY ----------

    def size(self):
        """Returns the number of nodes in the tree."""
        return len(self.inorder())

    def is_empty(self):
        """Returns True if tree is empty."""
        return self.root is None


# =========================
#   CONTACT MANAGER DEMO
# =========================

def print_menu():
    print("\n=== Contact Manager (BST) ===")
    print("1) Add / Update contact")
    print("2) Search contact")
    print("3) Delete contact")
    print("4) List all contacts (alphabetical)")
    print("5) Show preorder traversal")
    print("6) Show postorder traversal")
    print("7) Show tree statistics")
    print("8) Quit")


def main():
    tree = BST()

    print("Welcome to BST Contact Manager!")
    print("This is a Binary Search Tree implementation for learning purposes.")

    while True:
        print_menu()
        choice = input("\nChoose option: ").strip()

        if choice == "1":
            name = input("Name: ").strip()
            if not name:
                print("❌ Name cannot be empty!")
                continue
            
            info = input("Phone/email: ").strip()
            is_new = tree.insert(name, info)
            
            if is_new:
                print(f"✓ Added new contact: {name} -> {info}")
            else:
                print(f"✓ Updated contact: {name} -> {info}")

        elif choice == "2":
            name = input("Name to search: ").strip()
            if not name:
                print("❌ Name cannot be empty!")
                continue
            
            node = tree.search(name)
            if node:
                print(f"✓ Found: {node.key} -> {node.value}")
            else:
                print(f"❌ Contact '{name}' not found.")

        elif choice == "3":
            name = input("Name to delete: ").strip()
            if not name:
                print("❌ Name cannot be empty!")
                continue
            
            if tree.delete(name):
                print(f"✓ Deleted '{name}'")
            else:
                print(f"❌ Contact '{name}' not found, nothing deleted.")

        elif choice == "4":
            contacts = tree.inorder()
            if not contacts:
                print("📭 No contacts yet.")
            else:
                print(f"\n📇 Contacts (alphabetical order) - Total: {len(contacts)}")
                print("-" * 50)
                for name, info in contacts:
                    print(f"  {name:20} -> {info}")

        elif choice == "5":
            contacts = tree.preorder()
            if not contacts:
                print("📭 No contacts yet.")
            else:
                print("\n🔍 Preorder Traversal (Root -> Left -> Right):")
                print(" -> ".join([name for name, _ in contacts]))

        elif choice == "6":
            contacts = tree.postorder()
            if not contacts:
                print("📭 No contacts yet.")
            else:
                print("\n🔍 Postorder Traversal (Left -> Right -> Root):")
                print(" -> ".join([name for name, _ in contacts]))

        elif choice == "7":
            size = tree.size()
            is_empty = tree.is_empty()
            print(f"\n📊 Tree Statistics:")
            print(f"  Total contacts: {size}")
            print(f"  Tree empty: {is_empty}")
            if size > 0:
                contacts = tree.inorder()
                print(f"  First (alphabetically): {contacts[0][0]}")
                print(f"  Last (alphabetically): {contacts[-1][0]}")

        elif choice == "8":
            print("\n👋 Thanks for using BST Contact Manager. Goodbye!")
            break

        else:
            print("❌ Invalid option, please try again.")


if __name__ == "__main__":

    main()

