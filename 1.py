from tkinter import *

counter = 0

def add_label(event=None):

    global counter

    user_text = entry.get().strip()
    if len(user_text) <= 2:
        hint.configure(text="enter text more of then 3 symbols", fg='red')
        return

    hint.configure(text='')
    entry.delete(0, END)
    label_new=Label(root, text=user_text, padx="30", pady="20") 
    if counter % 2:
        label_new.configure(fg="#eeeeee", bg="#333333")
        label_new.pack(side=BOTTOM, fill=X)
    else:
        label_new.configure(bg="red", fg="#333333")
        label_new.pack(side=BOTTOM, fill=X)
    
    if counter > 6:
        counter = 0
        children = root.winfo_children()
        for i in children:
            if isinstance(i, Label):
                i.destroy()
    counter += 1


root = Tk()
root.geometry("300x500")
root.resizable(False, False)
root.title("simple tk")

Label(root, text="just a test", padx="30", pady="20").pack(side=BOTTOM)

input_frame = Frame(root)
input_frame.pack()

hint = Label(input_frame, text="", fg='red2', font=('Times New Roman', 6))
hint.pack(side=BOTTOM)

entry = Entry(input_frame, width="15")
entry.pack(side=LEFT)

button = Button(input_frame, text="click me!", command=add_label)
button.pack(side=LEFT)

entry.bind('<Return>', add_label)

root.mainloop()