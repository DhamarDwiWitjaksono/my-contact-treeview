import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from contact import Contacts

# list untuk menyimpan objek kontak
contacts_list = []

# fungsi untuk menambahkan kontak
def add_contact():
    if str(var_number.get()).isdigit() and "@gmail.com" in var_email.get():
        person = Contacts(var_name.get(), int(var_number.get()), var_email.get())
        contacts_list.append(person)
        # Menambahkan data ke Treeview
        Contacts_tree.insert("", "end", values=(person.name, person.phone_number, person.email))
        messagebox.showinfo("Berhasil", f"{var_name.get()} berhasil ditambahkan.")
        
    else:
        messagebox.showerror("Gagal", "Mohon masukkan data yang benar!")

# fungsi untuk menghapus kontak
def delete_contact():
    try:
        selected_item = Contacts_tree.selection()[0]  # Mendapatkan item yang dipilih
        selected_contact = contacts_list[Contacts_tree.index(selected_item)]
        del contacts_list[Contacts_tree.index(selected_item)]
        Contacts_tree.delete(selected_item)
        messagebox.showinfo("Berhasil", f"Kontak {selected_contact} berhasil dihapus.")
    except IndexError:
        messagebox.showwarning("Peringatan", "Pilih kontak yang ingin dihapus.")

# fungsi untuk menghapus data di form/entry
def clear_entry():
    var_name.set("")
    var_number.set("")
    var_email.set("")

# fungsi untuk menutup aplikasi
def close_app():
    window.destroy()

# tampilan utama
window = tk.Tk()
window.title("Kontak Saya")

# untuk menambahkan nama kontak
var_name = tk.StringVar()
frame_name = tk.Frame(window)
frame_name.pack()
label_name = tk.Label(frame_name, text="Name")
label_name.pack()
name_entry = tk.Entry(frame_name, textvariable=var_name)
name_entry.pack()

# untuk menambahkan nomor kontak
var_number = tk.StringVar()
frame_number = tk.Frame(window)
frame_number.pack()
label_phone_no = tk.Label(frame_number, text="Phone Number")
label_phone_no.pack()
number_entry = tk.Entry(frame_number, textvariable=var_number)
number_entry.pack()

# untuk menambahkan email kontak
var_email = tk.StringVar()
frame_email = tk.Frame(window)
frame_email.pack()
label_email = tk.Label(frame_email, text="Email")
label_email.pack()
email_entry = tk.Entry(frame_email, textvariable=var_email)
email_entry.pack()

# bingkai untuk 3 tombol
frame_button = tk.Frame(window)
frame_button.pack(pady=20)

# tombol tambah kontak
add_button = tk.Button(frame_button, text="Add", command=add_contact)
add_button.pack(side="left", padx=10)

# tombol hapus kontak
delete_button = tk.Button(frame_button, text="Delete", command=delete_contact)
delete_button.pack(side="left", padx=10)

# tombol hapus form
clear_button = tk.Button(frame_button, text="Clear", command=clear_entry)
clear_button.pack(side="left", padx=10)

# frame untuk kolom daftar kontak
frame_clumb = tk.Frame(window)
frame_clumb.pack(pady=(40, 0))

# kolom nama
name_clumb = tk.Label(frame_clumb, text="Name")
name_clumb.pack(side="left", padx=30)

# kolom nomor hp
number_clumb = tk.Label(frame_clumb, text="Number")
number_clumb.pack(side="left", padx=30)

# kolom email
email_clumb = tk.Label(frame_clumb, text="Email")
email_clumb.pack(side="left", padx=30)

# frame untuk Treeview
frame_tree = tk.Frame(window)
frame_tree.pack(pady=(20, 0))

# Membuat Treeview untuk menampilkan kontak
Contacts_tree = ttk.Treeview(frame_tree, columns=("Name", "Number", "Email"), show="headings", height=10)
Contacts_tree.pack(padx=20, pady=20)

# Menentukan heading/kolom
Contacts_tree.heading("Name", text="Name")
Contacts_tree.heading("Number", text="Number")
Contacts_tree.heading("Email", text="Email")

# tombol keluar aplikasi
quit_button = tk.Button(window, text="Quit", command=close_app)
quit_button.pack(pady=(20, 0))

window.mainloop()