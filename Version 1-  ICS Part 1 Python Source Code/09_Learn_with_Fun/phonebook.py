import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Contact Book")
        self.root.geometry("450x580")
        self.root.resizable(False, False)
        self.root.configure(bg="#1A1A2E")

        self.contacts = {}  # Store contacts as {name: phone}
        self.editing_contact = None  # Track which contact is being edited

        # Title
        title = tk.Label(root, text="Contact Book", font=("Segoe UI", 24, "bold"),
                         fg="#E94560", bg="#1A1A2E")
        title.pack(pady=(20, 10))

        # Frame for inputs
        input_frame = tk.Frame(root, bg="#16213E", bd=0, relief="ridge", padx=20, pady=20)
        input_frame.pack(pady=10, padx=20, fill="x")

        tk.Label(input_frame, text="Name:", font=("Segoe UI", 14), fg="#F0F0F0", bg="#16213E").grid(row=0, column=0, sticky="w", pady=8)
        self.name_entry = tk.Entry(input_frame, font=("Segoe UI", 14), bg="#0F3460", fg="white",
                                   insertbackground="white", relief="flat")
        self.name_entry.grid(row=0, column=1, pady=8, sticky="ew", padx=(10,0))

        tk.Label(input_frame, text="Phone:", font=("Segoe UI", 14), fg="#F0F0F0", bg="#16213E").grid(row=1, column=0, sticky="w", pady=8)
        self.phone_entry = tk.Entry(input_frame, font=("Segoe UI", 14), bg="#0F3460", fg="white",
                                    insertbackground="white", relief="flat")
        self.phone_entry.grid(row=1, column=1, pady=8, sticky="ew", padx=(10,0))

        input_frame.columnconfigure(1, weight=1)

        # Buttons Frame
        btn_frame = tk.Frame(root, bg="#1A1A2E")
        btn_frame.pack(pady=15)

        style = {
            "font": ("Segoe UI", 13, "bold"),
            "width": 14,
            "bd": 0,
            "relief": "ridge",
            "cursor": "hand2",
            "pady": 8,
        }

        self.add_btn = tk.Button(btn_frame, text="Add Contact", bg="#E94560", fg="white", activebackground="#FF2E63", **style,
                                 command=self.add_or_update_contact)
        self.add_btn.grid(row=0, column=0, padx=10)

        self.clear_btn = tk.Button(btn_frame, text="Clear Fields", bg="#0F3460", fg="white", activebackground="#16213E", **style,
                                   command=self.clear_fields)
        self.clear_btn.grid(row=0, column=1, padx=10)

        # Scrollable contacts list area
        self.contacts_frame = tk.Frame(root, bg="#1A1A2E")
        self.contacts_frame.pack(padx=20, pady=10, fill="both", expand=True)

        self.canvas = tk.Canvas(self.contacts_frame, bg="#1A1A2E", highlightthickness=0)
        self.scrollbar = tk.Scrollbar(self.contacts_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#1A1A2E")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

    def add_or_update_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()

        if not name or not phone:
            messagebox.showwarning("Input Error", "Please enter both name and phone number.")
            return

        if self.editing_contact:  # Update existing contact
            if name != self.editing_contact and name in self.contacts:
                messagebox.showwarning("Duplicate Entry", "This contact name already exists.")
                return
            # Remove old entry if name changed
            if name != self.editing_contact:
                del self.contacts[self.editing_contact]

            self.contacts[name] = phone
            self.editing_contact = None
            self.add_btn.config(text="Add Contact")
        else:  # Add new contact
            if name in self.contacts:
                messagebox.showwarning("Duplicate Entry", "This contact already exists.")
                return
            self.contacts[name] = phone

        self.clear_fields()
        self.refresh_contacts()

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.editing_contact = None
        self.add_btn.config(text="Add Contact")

    def delete_contact(self, name):
        confirm = messagebox.askyesno("Confirm Delete", f"Delete contact '{name}'?")
        if confirm:
            del self.contacts[name]
            if self.editing_contact == name:
                self.clear_fields()
            self.refresh_contacts()

    def load_contact_for_edit(self, name):
        self.editing_contact = name
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, name)
        self.phone_entry.delete(0, tk.END)
        self.phone_entry.insert(0, self.contacts[name])
        self.add_btn.config(text="Update Contact")

    def refresh_contacts(self):
        # Clear current widgets in scrollable_frame
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        for idx, (name, phone) in enumerate(sorted(self.contacts.items())):
            contact_frame = tk.Frame(self.scrollable_frame, bg="#0F3460", pady=10, padx=15)
            contact_frame.grid(row=idx, column=0, pady=8, sticky="ew")
            contact_frame.columnconfigure(0, weight=1)

            contact_label = tk.Label(contact_frame, text=f"{name} : {phone}",
                                     font=("Segoe UI", 14, "bold"), fg="#E94560", bg="#0F3460", anchor="w")
            contact_label.grid(row=0, column=0, sticky="w")

            btn_frame = tk.Frame(contact_frame, bg="#0F3460")
            btn_frame.grid(row=0, column=1, padx=10)

            upd_btn = tk.Button(btn_frame, text="Update", bg="#3F72AF", fg="white",
                                font=("Segoe UI", 11, "bold"), bd=0, padx=12, pady=4,
                                activebackground="#28527A",
                                command=lambda n=name: self.load_contact_for_edit(n))
            upd_btn.pack(side="left", padx=(0,8))

            del_btn = tk.Button(btn_frame, text="Delete", bg="#FF2E63", fg="white",
                                font=("Segoe UI", 11, "bold"), bd=0, padx=12, pady=4,
                                activebackground="#E94560",
                                command=lambda n=name: self.delete_contact(n))
            del_btn.pack(side="left")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
