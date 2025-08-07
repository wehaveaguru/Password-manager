from tkinter import *

window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(height=200,width=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

label=Label(text="Website:")
email=Label(text="Email/Username:")
password=Label(text="Password:")
label.grid(row=1,column=0)
email.grid(row=2,column=0)
password.grid(row=3,column=0)

website_entry=Entry(width=35)
website_entry.focus()
website_entry.insert(0,"example.com")
email_entry=Entry(width=35)
email_entry.focus()
email_entry.insert(0,"user@example.com")

password_entry=Entry(width=21)
password_entry.focus()

website_entry.grid(row=1,column=1,columnspan=2)
email_entry.grid(row=2,column=1,columnspan=2)   
password_entry.grid(row=3,column=1)

def generate_password():
    import random
    
    


gen_password_button=Button(text="Generate Password",command=generate_password)
gen_password_button.grid(row=3,column=2)
add_button=Button(text="Add",width=36)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()