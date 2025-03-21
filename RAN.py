import random
import tkinter as tk

names = ["Adri", "Ági", "Csilla", "Dia", "Evi",  "Feri", "Kata", "Kriszta", "Lilla", "Meli", "Tündi"]

root = tk.Tk()
root.title("RAN")

name_list = tk.Listbox(root, selectmode='multiple', height=12, width=25)
for name in names:
    name_list.insert(tk.END, name)
name_list.pack()

remove_button = tk.Button(root, text="Kiválaszt", command=lambda: remove_names())
remove_button.pack()
exit_button = tk.Button(root, text="Kilépés", command=lambda: exit_program())
exit_button.pack()
random_button = tk.Button(root, text="Random", command=lambda: select_random())
random_button.pack()
#accept_deny_button = tk.Checkbutton(root, text="Elfogadta", command=lambda: acceptlist())
#accept_deny_button.pack()

output_area = tk.Text(root, height=5, width=20)
output_area.pack()

def remove_names():
    selected_indices = name_list.curselection()
    if selected_indices:
        removed_names = [name_list.get(i) for i in selected_indices]
        print("selected_indices: {}".format(selected_indices))
        for r in removed_names:
            names.remove(r)
            output_area.configure(state='normal')
            output_area.delete(1.0, tk.END)
            output_area.insert(tk.END, f'Kiválasztott nevek: {removed_names}')
            output_area.configure(state='disabled')
            name_list.delete(0,tk.END)
        for n in names:
            name_list.insert(tk.END,n)
    else:
        output_area.configure(state='normal')
        output_area.delete(1.0, tk.END)
        output_area.insert(tk.END, 'Kérlek válassz nevet')
        output_area.configure(state='disabled')
    print("removed_names: {}".format(removed_names))
    print("names: {}".format(names))

def exit_program():
    root.destroy()

def select_random():
    if name_list.size() > 0:
        random_name = random.choice(names)
        for i in range(name_list.size()):
            if name_list.get(i) == random_name:
                name_list.delete(i)
                break
        names.remove(random_name)
        output_area.configure(state='normal')
        output_area.delete(1.0, tk.END)
        output_area.insert(tk.END, f'Az áldozat: {random_name}')
        output_area.configure(state='disabled')
    else:
        output_area.configure(state='normal')
        output_area.delete(1.0, tk.END)
        output_area.insert(tk.END, 'Elfogytak a \nlehetőségek')
        output_area.configure(state='disabled')

root.mainloop()
