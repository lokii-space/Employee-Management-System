from customtkinter import *
from PIL import Image
from tkinter import ttk
from tkinter import messagebox
import database
# FUNCTIONS
def delete_all():
    result=messagebox.askyesno('confirm','Do you really want to delete the database?')
    if result:
        database.deleteall_records()
def show_all():
    treeview_data()
    searchEntry.delete(0, END)
    searchbox.set('Search By')
def search_employee():
    if searchEntry.get() == "":
        messagebox.showerror("Error", "enter value to search")
    elif searchbox.get() == "Search By":
        messagebox.showerror("Error", "please select an option")
    else:
        searched_data=database.search(searchbox.get(),searchEntry.get())
        tree.delete(*tree.get_children())
        for i in searched_data:
            tree.insert('', END, values=i)
def clear(value=False):
        if value:
            tree.selection_remove(tree.focus())
        idEntry.delete(0, END)
        nameEntry.delete(0, END)
        phoneEntry.delete(0, END)
        rolebox.set('')
        genderbox.set('')
        salaryEntry.delete(0, END)

def update_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showinfo("Error","No selected item")
    else:
        database.update(idEntry.get(), nameEntry.get(), phoneEntry.get(), rolebox.get(), genderbox.get(),
                        salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo("Success","Employee Updated")

def delete_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showinfo("Error","No selected item")
    else:
        database.delete(idEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo("Success","Employee Deleted")

def selection(event):
    selected_item=tree.selection()
    if selected_item:
        row=tree.item(selected_item)['values']
        clear()
        idEntry.insert(0,row[0])
        nameEntry.insert(0,row[1])
        phoneEntry.insert(0,row[2])
        rolebox.set(row[3])
        genderbox.set(row[4])
        salaryEntry.insert(0,row[5])

def treeview_data():
    employees = database.fetch_employees()
    tree.delete(*tree.get_children())
    for i in employees:
        tree.insert('', END, values=i)


def add_employee():
    if idEntry.get() == '' or phoneEntry.get() == '' or nameEntry.get() == '' or salaryEntry.get() == '':
        messagebox.showerror('Error', 'Please fill all fields')
    elif database.id_exists(idEntry.get()):
        messagebox.showerror('Error', 'Employee ID already exists')
    elif not idEntry.get().startswith('EMP'):
        messagebox.showerror('Error', 'Invalid ID Format(e.g:EMPx)')
    else:
        database.insert(idEntry.get(), nameEntry.get(), phoneEntry.get(), rolebox.get(), genderbox.get(),
                        salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success', 'Employee added')

# GUI PART
window = CTk()
window.geometry('850x608+100+100')
window.resizable(0, 0)
window.title('Employee Management System')

logo = CTkImage(Image.open('nearshore-banner (1).jpg'), size=(850, 186))
logoLabel = CTkLabel(window, image=logo, text='')
logoLabel.grid(column=0, row=0, columnspan=2, pady=(0, 10))

leftFrame = CTkFrame(window, fg_color='#232323')
leftFrame.grid(column=0, row=1)

idLabel = CTkLabel(leftFrame, text='Employee ID', font=('Times New Roman', 15, 'bold'))
idLabel.grid(column=0, row=0, padx=12, pady=12, sticky='w')
idEntry = CTkEntry(leftFrame, font=('Times New Roman', 15, 'bold'), width=150)
idEntry.grid(column=1, row=0)

nameLabel = CTkLabel(leftFrame, text='Employee Name', font=('Times New Roman', 15, 'bold'))
nameLabel.grid(column=0, row=1, padx=12, pady=12, sticky='w')
nameEntry = CTkEntry(leftFrame, font=('Times New Roman', 15, 'bold'), width=150)
nameEntry.grid(column=1, row=1)

phoneLabel = CTkLabel(leftFrame, text='Phone Number', font=('Times New Roman', 15, 'bold'))
phoneLabel.grid(column=0, row=2, padx=12, pady=12, sticky='w')
phoneEntry = CTkEntry(leftFrame, font=('Times New Roman', 15, 'bold'), width=150)
phoneEntry.grid(column=1, row=2)

roleLabel = CTkLabel(leftFrame, text='Employee Role', font=('Times New Roman', 15, 'bold'))
roleLabel.grid(column=0, row=3, padx=12, pady=12, sticky='w')
role_options = ['Web Developer', 'Data Analyst', 'Technical Analyst', 'Business Analyst', 'Software Engineer']
rolebox = CTkComboBox(leftFrame, values=role_options, width=150, font=('Times New Roman', 15, 'bold'), state='readonly')
rolebox.grid(column=1, row=3)

genderLabel = CTkLabel(leftFrame, text='Gender', font=('Times New Roman', 15, 'bold'))
genderLabel.grid(column=0, row=4, padx=12, pady=12, sticky='w')
gender_options = ['Male', 'Female', 'Other']
genderbox = CTkComboBox(leftFrame, values=gender_options, width=150, font=('Times New Roman', 15, 'bold'), state='readonly')
genderbox.grid(column=1, row=4)

salaryLabel = CTkLabel(leftFrame, text='Employee Salary', font=('Times New Roman', 15, 'bold'))
salaryLabel.grid(column=0, row=5, padx=12, pady=12, sticky='w')
salaryEntry = CTkEntry(leftFrame, font=('Times New Roman', 15, 'bold'), width=150)
salaryEntry.grid(column=1, row=5)

rightFrame = CTkFrame(window)
rightFrame.grid(column=1, row=1)

search_options = ['id', 'name', 'phone', 'role', 'gender', 'salary']
searchbox = CTkComboBox(rightFrame, values=search_options, width=120, state='readonly')
searchbox.grid(column=0, row=0)
searchbox.set('Search By ')

searchEntry = CTkEntry(rightFrame, width=120)  # Renamed from salaryEntry
searchEntry.grid(column=1, row=0)

searchButton = CTkButton(rightFrame, text='Search', width=100,command=search_employee)
searchButton.grid(column=2, row=0)

showallButton = CTkButton(rightFrame, text='Show All', width=100,command=show_all)
showallButton.grid(column=3, row=0, pady=15)

tree = ttk.Treeview(rightFrame, height=13)
tree.grid(column=0, row=1, columnspan=4)

tree['columns'] = ('Employee ID', 'Employee Name', 'Phone Number', 'Employee Role', 'Gender', 'Employee Salary')
tree.heading('Employee ID', text='ID')
tree.heading('Employee Name', text='Name')
tree.heading('Phone Number', text='Phone Number')
tree.heading('Employee Role', text='Role')
tree.heading('Gender', text='Gender')
tree.heading('Employee Salary', text='Salary')

tree.config(show='headings')
tree.column('Employee ID', width=100)
tree.column('Employee Name', width=150)
tree.column('Phone Number', width=120)
tree.column('Employee Role', width=100)
tree.column('Gender', width=130)
tree.column('Employee Salary', width=130)

style = ttk.Style()
style.configure('Treeview.Heading', font=('Times new roman', 15, 'bold'))
style.configure('Treeview',font=('Times new roman', 15, 'bold'),rowheight=30,background='#1F69A4')

scrollbar = ttk.Scrollbar(rightFrame, orient=VERTICAL,command=tree.yview)
scrollbar.grid(row=1, column=4, sticky='ns')

tree.config(yscrollcommand=scrollbar.set)

buttonFrame = CTkFrame(window)
buttonFrame.grid(column=0, row=2, columnspan=2)

newButton = CTkButton(buttonFrame, text='New Employee', font=('Times New Roman', 15, 'bold'), width=150, corner_radius=15,command=lambda:clear(True))
newButton.grid(column=0, row=0, pady=5)

addButton = CTkButton(buttonFrame, text='Add Employee', font=('Times New Roman', 15, 'bold'), width=150, corner_radius=15, command=add_employee)
addButton.grid(column=1, row=0, pady=5, padx=5)

updateButton = CTkButton(buttonFrame, text='Update Employee', font=('Times New Roman', 15, 'bold'), width=150, corner_radius=15,command=update_employee)
updateButton.grid(column=2, row=0, pady=5, padx=5)

deleteButton = CTkButton(buttonFrame, text='Delete Employee', font=('Times New Roman', 15, 'bold'), width=150, corner_radius=15,command=delete_employee)
deleteButton.grid(column=3, row=0, pady=5, padx=5)

deleteallButton = CTkButton(buttonFrame, text='Delete All Employee', font=('Times New Roman', 15, 'bold'), width=150, corner_radius=15,command=delete_all)
deleteallButton.grid(column=4, row=0, pady=5, padx=5)

window.bind('<ButtonRelease>',selection)
treeview_data()
window.mainloop()
