# import tkinter as tk

# class App(tk.Frame):
#     def __init__(self, master):
#         tk.Frame.__init__(self, master, height=42, width=42)
#         self.entry = tk.Entry(self)
#         self.entry.focus()
#         self.entry.pack()
#         self.clear_button = tk.Button(self, text="Clear text", command=self.clear_text)
#         self.clear_button.pack()

#     def clear_text(self):
#         self.entry.delete(0, 'end')

# def main():
#     root = tk.Tk()
#     App(root).pack(expand=True, fill='both')
#     root.mainloop()

# if __name__ == "__main__":
#     main()

# from tkinter import *

# #entry widget = textbox that accepts a single line of user input

# def submit():
#     username = entry.get()
#     print("Hello "+username)

# def delete():
#     entry.delete(0,END)

# def backspace():
#     entry.delete(len(entry.get())-1, END)

# window = Tk()

# entry = Entry(window,
#               font=("Arial",50),
#               fg="#00FF00",
#               bg="black")

# #entry.insert(0,'Spongebob')
# #entry.config(show="*")
# #entry.config(state=DISABLED)

# entry.pack(side=LEFT)

# submit_button = Button(window,text="submit",command=submit)
# submit_button.pack(side=RIGHT)

# delete_button = Button(window,text="delete",command=delete)
# delete_button.pack(side=RIGHT)

# backspace_button = Button(window,text="backspace",command=backspace)
# backspace_button.pack(side=RIGHT)

# window.mainloop()

# try:                        # In order to be able to import tkinter for
#     import tkinter as tk    # either in python 2 or in python 3
# except ImportError:
#     import Tkinter as tk


# def clear_widget_text(widget):
#     widget['text'] = ""


# if __name__ == '__main__':
#     root = tk.Tk()
#     label = tk.Label(root, text="This will be cleared.")
#     button = tk.Button(root, text="Clear",command=lambda : clear_widget_text(label))
#     label.pack()
#     button.pack()
#     root.mainloop()


# # Import Module
# from tkinter import *
 
# # Create Object
# root = Tk()
 
# # specify size of window.
# root.geometry("400x500")
 
# # delete content from Text Box
 
 
# def delete_text():
#     T.delete("1.0", "end")
 
 
# # Create text widget
# T = Text(root)
# T.pack()
 
# # Create Delete Button
# Button(root, text="Delete", command=delete_text).pack()
 
# # Execute Tkinter
# root.mainloop()



