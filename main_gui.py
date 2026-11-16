import tkinter as tk
from tkinter import ttk

from graphs.graph import Graph
from hash_tables.hash_table import HashTable
from trees.binary_tree import BinaryTree, layout


class DataStructuresDemo:
    def __init__(self, master):
        self.master = master
        master.title("Data Structures Demo by Paul Martin McNeill")

        # Add a header with your name
        header_frame = ttk.Frame(master, padding="10 10 10 10")
        header_frame.pack(fill="x")
        ttk.Label(
            header_frame, text="Data Structures and Algorithms GUI", font=("Arial", 18, "bold")
        ).pack(side="left", padx=10)
        ttk.Label(header_frame, text="by Paul Martin McNeill", font=("Arial", 14, "italic")).pack(
            side="right", padx=10
        )

        # Create a notebook to switch between different data structures
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(expand=1, fill="both")

        # Initialize frames for each data structure
        self.binary_tree_frame = ttk.Frame(self.notebook, padding="10 10 10 10")
        self.hash_table_frame = ttk.Frame(self.notebook, padding="10 10 10 10")
        self.graph_frame = ttk.Frame(self.notebook, padding="10 10 10 10")

        self.notebook.add(self.binary_tree_frame, text="Binary Tree")
        self.notebook.add(self.hash_table_frame, text="Hash Table")
        self.notebook.add(self.graph_frame, text="Graph")

        # Initialize the data structures
        self.binary_tree = BinaryTree()
        self.hash_table = HashTable()
        self.graph = Graph()

        # Build the interfaces
        self.build_binary_tree_interface()
        self.build_hash_table_interface()
        self.build_graph_interface()

    def build_binary_tree_interface(self):
        ttk.Label(
            self.binary_tree_frame, text="Binary Tree Operations", font=("Arial", 16, "bold")
        ).pack(pady=10)

        self.bt_info_display = tk.Text(
            self.binary_tree_frame,
            height=5,
            wrap=tk.WORD,
            font=("Arial", 10),
            background="#f0f0f0",
            relief="flat",
            borderwidth=0,
        )
        self.bt_info_display.pack(fill="x", padx=5, pady=5)
        self.bt_info_display.insert(
            tk.END,
            "A Binary Tree is a hierarchical structure where each node has at most two children. "
            "You can insert values into the tree, and the system will maintain a sorted structure. "
            "Smaller values go to the left, larger to the right. The drawing shows the tree's shape; "
            "the in-order traversal underneath visits it in ascending order.\n"
            "\nInstructions:\n1. Enter a whole number.\n2. Click 'Insert'.\n3. Watch where it lands in the tree.",
        )

        input_frame = ttk.Frame(self.binary_tree_frame)
        input_frame.pack(fill="x", pady=10)

        ttk.Label(input_frame, text="Enter a number:", font=("Arial", 12)).pack(side="left", padx=5)
        self.bt_insert_entry = ttk.Entry(input_frame, width=10, font=("Arial", 12))
        self.bt_insert_entry.pack(side="left", padx=5)
        ttk.Button(input_frame, text="Insert", command=self.insert_binary_tree).pack(
            side="left", padx=5
        )
        ttk.Button(input_frame, text="Clear", command=self.clear_binary_tree).pack(
            side="left", padx=5
        )

        self.bt_canvas = tk.Canvas(
            self.binary_tree_frame,
            height=240,
            background="#ffffff",
            highlightthickness=1,
            highlightbackground="#bbbbbb",
        )
        self.bt_canvas.pack(fill="both", expand=True, padx=5, pady=5)
        self.bt_canvas.bind("<Configure>", lambda e: self.draw_tree())

        self.bt_inorder_var = tk.StringVar(value="In-order traversal: (empty)")
        ttk.Label(
            self.binary_tree_frame, textvariable=self.bt_inorder_var, font=("Arial", 12)
        ).pack(anchor="w", padx=5, pady=5)

    def insert_binary_tree(self):
        value = self.bt_insert_entry.get()
        if value.isdigit():
            value = int(value)
            self.binary_tree.insert(value)
            self.display_binary_tree()

            explanation = (
                f"Inserted {value} into the Binary Tree.\n"
                "It was compared with each node from the root down, going left when smaller "
                "and right when larger, until it found an empty place."
            )
            self.bt_info_display.delete(1.0, tk.END)
            self.bt_info_display.insert(tk.END, explanation)
        else:
            self.bt_info_display.delete(1.0, tk.END)
            self.bt_info_display.insert(tk.END, "Error: Please enter a valid integer.")

    def display_binary_tree(self):
        result = self.binary_tree.inorder_traversal()
        self.bt_inorder_var.set("In-order traversal: " + (" ".join(map(str, result)) or "(empty)"))
        self.draw_tree()

    def draw_tree(self):
        """Draw each node at (in-order position, depth), with lines to its children."""
        c = self.bt_canvas
        c.delete("all")
        nodes, edges = layout(self.binary_tree)
        if not nodes:
            return
        w, h = max(c.winfo_width(), 200), max(c.winfo_height(), 120)
        depth = max(d for _, _, d in nodes) + 1
        dx, dy = w / (len(nodes) + 1), (h - 40) / max(depth - 1, 1) if depth > 1 else 0
        xy = [((col + 1) * dx, 20 + d * dy) for _, col, d in nodes]
        for a, b in edges:
            c.create_line(*xy[a], *xy[b], fill="#888888", width=2)
        r = 16
        for (value, _, _), (x, y) in zip(nodes, xy, strict=True):
            c.create_oval(x - r, y - r, x + r, y + r, fill="#dbeafe", outline="#1d4ed8", width=2)
            c.create_text(x, y, text=str(value), font=("Arial", 10, "bold"))

    def clear_binary_tree(self):
        self.binary_tree = BinaryTree()  # Reset the binary tree
        self.bt_insert_entry.delete(0, tk.END)
        self.display_binary_tree()
        self.bt_info_display.delete(1.0, tk.END)
        self.bt_info_display.insert(
            tk.END, "Cleared the binary tree. You can start inserting values again."
        )

    def build_hash_table_interface(self):
        ttk.Label(
            self.hash_table_frame, text="Hash Table Operations", font=("Arial", 16, "bold")
        ).pack(pady=10)

        self.ht_info_display = tk.Text(
            self.hash_table_frame,
            height=5,
            wrap=tk.WORD,
            font=("Arial", 10),
            background="#f0f0f0",
            relief="flat",
            borderwidth=0,
        )
        self.ht_info_display.pack(fill="x", padx=5, pady=5)
        self.ht_info_display.insert(
            tk.END,
            "A Hash Table is a data structure that uses a hash function to map keys to indices in an array. "
            "Each key-value pair is stored at an index determined by the hash function. This allows for fast lookups, "
            "insertion, and deletion.\n\nInstructions:\n1. Enter a key-value pair.\n2. Click 'Insert'.\n3. View the current state of the hash table.",
        )

        input_frame = ttk.Frame(self.hash_table_frame)
        input_frame.pack(fill="x", pady=10)

        ttk.Label(input_frame, text="Enter Key:", font=("Arial", 12)).pack(side="left", padx=5)
        self.ht_insert_key_entry = ttk.Entry(input_frame, width=15, font=("Arial", 12))
        self.ht_insert_key_entry.pack(side="left", padx=5)

        ttk.Label(input_frame, text="Enter Value:", font=("Arial", 12)).pack(side="left", padx=5)
        self.ht_insert_value_entry = ttk.Entry(input_frame, width=15, font=("Arial", 12))
        self.ht_insert_value_entry.pack(side="left", padx=5)

        ttk.Button(input_frame, text="Insert", command=self.insert_hash_table).pack(
            side="left", padx=5
        )
        ttk.Button(input_frame, text="Clear", command=self.clear_hash_table).pack(
            side="left", padx=5
        )

        ttk.Label(self.hash_table_frame, text="Hash Table Contents:", font=("Arial", 12)).pack(
            anchor="w", padx=5, pady=5
        )
        self.ht_display = tk.Text(
            self.hash_table_frame,
            height=10,
            wrap=tk.WORD,
            font=("Arial", 10),
            background="#ffffff",
            relief="sunken",
            borderwidth=1,
        )
        self.ht_display.pack(fill="x", padx=5, pady=5)

    def insert_hash_table(self):
        key = self.ht_insert_key_entry.get()
        value = self.ht_insert_value_entry.get()
        if key and value:
            self.hash_table[key] = value
            self.display_hash_table()

            explanation = (
                f"Inserted key '{key}' with value '{value}' into the Hash Table.\n"
                "The key is hashed to determine its position in the table, where the value is stored."
            )
            self.ht_info_display.delete(1.0, tk.END)
            self.ht_info_display.insert(tk.END, explanation)
        else:
            self.ht_info_display.delete(1.0, tk.END)
            self.ht_info_display.insert(tk.END, "Error: Please enter both a key and a value.")

    def display_hash_table(self):
        """One line per occupied slot; keys whose hashes collide share a slot."""
        self.ht_display.delete(1.0, tk.END)
        slots = {}
        for index, k, v in self.hash_table.items():
            slots.setdefault(index, []).append(f"{k} -> {v}")
        for index, pairs in slots.items():
            note = f"   ({len(pairs)} keys share this slot)" if len(pairs) > 1 else ""
            self.ht_display.insert(tk.END, f"Slot {index}: " + " | ".join(pairs) + note + "\n")

    def clear_hash_table(self):
        self.hash_table = HashTable()  # Reset the hash table
        self.ht_insert_key_entry.delete(0, tk.END)
        self.ht_insert_value_entry.delete(0, tk.END)
        self.ht_display.delete(1.0, tk.END)
        self.ht_info_display.delete(1.0, tk.END)
        self.ht_info_display.insert(
            tk.END, "Cleared the hash table. You can start inserting key-value pairs again."
        )

    def build_graph_interface(self):
        ttk.Label(self.graph_frame, text="Graph Operations", font=("Arial", 16, "bold")).pack(
            pady=10
        )

        self.graph_info_display = tk.Text(
            self.graph_frame,
            height=5,
            wrap=tk.WORD,
            font=("Arial", 10),
            background="#f0f0f0",
            relief="flat",
            borderwidth=0,
        )
        self.graph_info_display.pack(fill="x", padx=5, pady=5)
        self.graph_info_display.insert(
            tk.END,
            "A Graph is a set of nodes connected by edges. Each edge connects two nodes, and can be directed or undirected. "
            "This tool allows you to build a graph by adding edges between nodes and performing a breadth-first search (BFS) to explore the graph.\n\n"
            "Instructions:\n1. Enter a start and end node to create an edge.\n2. Click 'Add Edge'.\n3. View the adjacency list.\n4. Enter a node and click 'Perform BFS' to explore the graph.\n"
            "Examples:\n- Add Edge: Start Node = 0, End Node = 1\n- Add Edge: Start Node = 1, End Node = 2\n- Perform BFS from Start Node = 0",
        )

        input_frame = ttk.Frame(self.graph_frame)
        input_frame.pack(fill="x", pady=10)

        ttk.Label(input_frame, text="Start Node:", font=("Arial", 12)).pack(side="left", padx=5)
        self.graph_add_start_entry = ttk.Entry(input_frame, width=10, font=("Arial", 12))
        self.graph_add_start_entry.pack(side="left", padx=5)

        ttk.Label(input_frame, text="End Node:", font=("Arial", 12)).pack(side="left", padx=5)
        self.graph_add_end_entry = ttk.Entry(input_frame, width=10, font=("Arial", 12))
        self.graph_add_end_entry.pack(side="left", padx=5)

        ttk.Button(input_frame, text="Add Edge", command=self.add_graph_edge).pack(
            side="left", padx=5
        )
        ttk.Button(input_frame, text="Clear", command=self.clear_graph).pack(side="left", padx=5)

        bfs_frame = ttk.Frame(self.graph_frame)
        bfs_frame.pack(fill="x", pady=(0, 10))
        ttk.Label(bfs_frame, text="BFS Start Node:", font=("Arial", 12)).pack(side="left", padx=5)
        self.bfs_start_entry = ttk.Entry(bfs_frame, width=10, font=("Arial", 12))
        self.bfs_start_entry.pack(side="left", padx=5)
        ttk.Button(bfs_frame, text="Perform BFS", command=self.perform_bfs).pack(
            side="left", padx=5
        )

        self.bfs_result_var = tk.StringVar(value="BFS order: (not run yet)")
        ttk.Label(
            self.graph_frame, textvariable=self.bfs_result_var, font=("Arial", 12, "bold")
        ).pack(anchor="w", padx=5, pady=5)

        ttk.Label(self.graph_frame, text="Graph Adjacency List:", font=("Arial", 12)).pack(
            anchor="w", padx=5, pady=5
        )
        self.graph_display = tk.Text(
            self.graph_frame,
            height=10,
            wrap=tk.WORD,
            font=("Arial", 10),
            background="#ffffff",
            relief="sunken",
            borderwidth=1,
        )
        self.graph_display.pack(fill="x", padx=5, pady=5)

    def add_graph_edge(self):
        start = self.graph_add_start_entry.get()
        end = self.graph_add_end_entry.get()

        # Error handling for invalid inputs
        if not start.isdigit() or not end.isdigit():
            self.graph_info_display.delete(1.0, tk.END)
            self.graph_info_display.insert(
                tk.END, "Error: Please enter valid integers for both start and end nodes."
            )
            return

        start, end = int(start), int(end)
        self.graph.add_edge(start, end)
        self.display_graph()

        explanation = (
            f"Added an edge from node {start} to node {end} in the Graph.\n"
            "The edge has been added to the adjacency list, displayed below."
        )
        self.graph_info_display.delete(1.0, tk.END)
        self.graph_info_display.insert(tk.END, explanation)

    def perform_bfs(self):
        start = self.bfs_start_entry.get()

        # Error handling for invalid BFS start node
        if not start.isdigit():
            self.graph_info_display.delete(1.0, tk.END)
            self.graph_info_display.insert(
                tk.END, "Error: Please enter a valid integer for the BFS start node."
            )
            return

        start = int(start)
        if start not in self.graph.nodes():
            self.graph_info_display.delete(1.0, tk.END)
            self.graph_info_display.insert(
                tk.END,
                f"Error: Node {start} does not exist in the graph. Please enter a valid start node.",
            )
            return

        bfs_result = self.graph.bfs(start)
        # Show the visit order on its own line; the adjacency list stays visible.
        self.bfs_result_var.set(f"BFS order from {start}: " + " \u2192 ".join(map(str, bfs_result)))

        explanation = (
            f"Performed BFS starting from node {start}.\n"
            "BFS explores the graph level by level, starting from the given node. "
            "The order of node visits is shown above the adjacency list."
        )
        self.graph_info_display.delete(1.0, tk.END)
        self.graph_info_display.insert(tk.END, explanation)

    def display_graph(self):
        self.graph_display.delete(1.0, tk.END)
        for node in self.graph.nodes():
            targets = self.graph.graph.get(node, [])
            self.graph_display.insert(
                tk.END, f"{node} \u2192 {', '.join(map(str, targets)) or '(no outgoing edges)'}\n"
            )

    def clear_graph(self):
        self.graph = Graph()  # Reset the graph
        self.graph_add_start_entry.delete(0, tk.END)
        self.graph_add_end_entry.delete(0, tk.END)
        self.bfs_start_entry.delete(0, tk.END)
        self.graph_display.delete(1.0, tk.END)
        self.bfs_result_var.set("BFS order: (not run yet)")
        self.graph_info_display.delete(1.0, tk.END)
        self.graph_info_display.insert(
            tk.END, "Cleared the graph. You can start adding edges and performing BFS again."
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = DataStructuresDemo(root)
    root.mainloop()
