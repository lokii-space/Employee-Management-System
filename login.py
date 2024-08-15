from customtkinter import *
from PIL import Image
from tkinter import messagebox
def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','Please enter your username and password')
    elif usernameEntry.get()=='lokesh' and passwordEntry.get()=='lokesh@23':
        messagebox.showinfo('Successful','You have successfully logged in')
        root.destroy()
        import ems
    else:
        messagebox.showerror('Error','Wrong username or password')


root=CTk()
root.geometry('850x608')
root.resizable(0,0)
root.title('login page')
image = CTkImage(Image.open('log.jpg'),size=(850,608))
imageLabel = CTkLabel(root, image=image,text='')
headinglabel = CTkLabel(
    root,
    text='Employee Management System',
    fg_color='#7790D3',
    font=('Goudy Old Style', 24, 'bold'),
    text_color='#2C333D'
)
headinglabel.place(x=30,y=200)
usernameEntry=CTkEntry(
    root,
    placeholder_text='Enter your Username',
    fg_color='#DCE7FC',
    width=200,
    text_color='#2C333D'
)
usernameEntry.place(x=70,y=250)
passwordEntry=CTkEntry(
    root,
    placeholder_text='Enter your Password',
    fg_color='#DCE7FC',
    width=200,
    text_color='#2C333D',
    show='*'
)
passwordEntry.place(x=70,y=300)
loginbutton=CTkButton(root,text='Login',cursor='hand2',command=login)
loginbutton.place(x=95,y=350)
imageLabel.place(x=0, y=0)
root.mainloop()
