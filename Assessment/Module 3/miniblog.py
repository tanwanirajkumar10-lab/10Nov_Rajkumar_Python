import os
import tkinter as tk
from tkinter import messagebox, filedialog

# -----------------------------
# Classes
# -----------------------------
class User:
    def __init__(self, name):
        self.name = name


class Post:
    def __init__(self, user, title, content):
        self.user = user
        self.title = title
        self.content = content

    def filename(self):
        safe_title = self.title.replace(" ", "_")
        safe_user = self.user.name.replace(" ", "_")
        return f"{safe_user}_{safe_title}.txt"

    def save(self):
        try:
            if not os.path.exists("posts"):
                os.makedirs("posts")
            filepath = os.path.join("posts", self.filename())
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"Author: {self.user.name}\n")
                f.write(f"Title: {self.title}\n\n")
                f.write(self.content)
            return filepath
        except Exception as e:
            messagebox.showerror("Error", f"Could not save post: {e}")
            return None


# -----------------------------
# GUI Application
# -----------------------------
class MiniBlogApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MiniBlog")

        # Labels and Inputs
        tk.Label(root, text="Name:").grid(row=0, column=0, sticky="w")
        self.name_entry = tk.Entry(root, width=30)
        self.name_entry.grid(row=0, column=1)

        tk.Label(root, text="Title:").grid(row=1, column=0, sticky="w")
        self.title_entry = tk.Entry(root, width=30)
        self.title_entry.grid(row=1, column=1)

        tk.Label(root, text="Content:").grid(row=2, column=0, sticky="nw")
        self.content_text = tk.Text(root, width=40, height=10)
        self.content_text.grid(row=2, column=1)

        # Buttons
        tk.Button(root, text="Save Post", command=self.save_post).grid(row=3, column=1, sticky="w")
        tk.Button(root, text="Load Posts", command=self.load_posts).grid(row=3, column=1, sticky="e")

        # Listbox for saved posts
        tk.Label(root, text="Saved Posts:").grid(row=4, column=0, sticky="nw")
        self.post_listbox = tk.Listbox(root, width=40, height=10)
        self.post_listbox.grid(row=4, column=1)
        self.post_listbox.bind("<<ListboxSelect>>", self.view_post)

        # Download button
        tk.Button(root, text="Download Post", command=self.download_post).grid(row=5, column=1, sticky="w")

    def save_post(self):
        name = self.name_entry.get().strip()
        title = self.title_entry.get().strip()
        content = self.content_text.get("1.0", tk.END).strip()

        if not name or not title or not content:
            messagebox.showwarning("Warning", "All fields must be filled!")
            return

        user = User(name)
        post = Post(user, title, content)
        filepath = post.save()
        if filepath:
            messagebox.showinfo("Success", f"Post saved as {filepath}")
            self.load_posts()

    def load_posts(self):
        self.post_listbox.delete(0, tk.END)
        if os.path.exists("posts"):
            for filename in os.listdir("posts"):
                self.post_listbox.insert(tk.END, filename)

    def view_post(self, event):
        try:
            selection = self.post_listbox.get(self.post_listbox.curselection())
            filepath = os.path.join("posts", selection)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            messagebox.showinfo("Post Content", content)
        except Exception as e:
            messagebox.showerror("Error", f"Could not load post: {e}")

    def download_post(self):
        try:
            selection = self.post_listbox.get(self.post_listbox.curselection())
            filepath = os.path.join("posts", selection)

            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            # Ask user where to save
            save_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                initialfile=selection,
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
            )

            if save_path:
                with open(save_path, "w", encoding="utf-8") as f:
                    f.write(content)
                messagebox.showinfo("Success", f"Post downloaded to {save_path}")

        except Exception as e:
            messagebox.showerror("Error", f"Could not download post: {e}")


# -----------------------------
# Run Application
# -----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = MiniBlogApp(root)
    root.mainloop()
