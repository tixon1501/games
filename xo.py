from tkinter import Tk, Canvas, Frame, BOTH
from tkinter import Tk, Frame, BOTH


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")  # цвет окна
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Крестики - нолики")  # загаловок
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_line(150, 0, 150, 450)  # линия х, у начала, х,у конца
        canvas.create_line(300, 0, 300, 450)
        canvas.create_line(0, 150, 450, 150)
        canvas.create_line(0, 300, 450, 300)
        canvas.pack(fill=BOTH, expand=1)



def main():
    root = Tk()
    root.geometry("500x500")
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()
