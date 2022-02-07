from tkinter import *


class MyApp:
    def __init__(self, root):
        root.title("My App")
        root.ge("500x400")
        root.maxsize(1000, 800)


root = Tk()
MyApp(root)
root.mainloop()
