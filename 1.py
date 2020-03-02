from tkinter import *

counter = 0

def add_label(event=NONE):

    global counter

    user_text = entry.get()
    entry.delete(0, END)
    label_new=Label(root, text=user_text, padx="30", pady="20") 
    if counter % 2:
        label_new.configure(fg="#eeeeee", bg="#333333")
        label_new.pack(side=BOTTOM, fill=X)
    else:
        label_new.configure(bg="red", fg="#333333")
        label_new.pack(side=BOTTOM, fill=X)
    counter += 1


root = Tk()
root.geometry("300x500")
root.resizable(False, False)
root.title("simple tk")

Label(root, text="just a test", padx="30", pady="20").pack(side=BOTTOM)
input_frame = Frame(root)
input_frame.pack()

entry = Entry(input_frame, width="15")
entry.pack(side=LEFT)
button = Button(input_frame, text="click me!", command=add_label)
button.pack(side=LEFT)

button.bind('<Return>', add_label)

root.mainloop()