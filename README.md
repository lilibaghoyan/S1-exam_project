# S1-exam_project

**BST Contact Manager (Python)** — Binary Search Tree Implementation

## 📌 Project Description

This project implements a **Binary Search Tree (BST)** in Python and uses it to build a simple **Contact Manager**.  
Each contact’s **name** is stored as a key (case-insensitive), and the **phone/email** is stored as a value.  
The BST allows adding, updating, searching, deleting, and listing contacts in **alphabetical order**.  
There is also a **tree visualizer** that prints the BST structure as ASCII art.

## 🌳 BST Features

* Case-insensitive key comparison
* Insert new contacts or update existing ones
* Search a contact by name
* Delete nodes (supports all 3 delete cases: leaf, one child, two children)
* Traversal methods:

  * **Inorder** — sorted alphabetical list
  * **Preorder** — root → left → right
  * **Postorder** — left → right → root
* Utility functions:

  * `size()` — number of contacts
  * `is_empty()` — checks if the tree is empty
  * `print_tree()` — prints the BST visually
  
## 📇 Contact Manager (CLI)

Interactive menu with the following options:

1. Add / Update contact
2. Search contact
3. Delete contact
4. List all contacts alphabetically
5. Show preorder traversal
6. Show postorder traversal
7. Show tree statistics
8. Quit
9. Show tree visual

The program provides helpful messages for invalid input, missing names, contacts not found, and empty trees.

## 🧠 What You Learn

* How Binary Search Trees work
* Recursion for search, insertion, and deletion
* Inorder traversal for sorted output
* Handling case-insensitivity in data structures
* Designing a simple but functional command-line interface
* Understanding tree-based data organization

## ▶️ Running the Program

Make sure Python is installed, then run:

```bash
python bst_contacts.py
```

## 📂 Files

* `bst_contacts.py` — full implementation (BST + Contact Manager)

## 📊 Example Output

```
=== Contact Manager (BST) ===
1) Add / Update contact
2) Search contact
3) Delete contact
4) List all contacts (alphabetical)
5) Show preorder traversal
6) Show postorder traversal
7) Show tree statistics
8) Quit
9) Show tree visual

Name: Anna
Phone/email: anna@example.com
Added: Anna -> anna@example.com

```

## Example tree visualization:
```

Current Binary Search Tree:
│       ┌── Vera
│   ┌── Lili
└── Anna
     

```
## 👩🏻‍💻 Authors

**Lili Baghoyan** 

**Vera Ghazaryan**

**Ofelya Gizhlaryan**
