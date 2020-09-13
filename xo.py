from tkinter import *
from random import  randint

c = Canvas(width=450, height=500, bg='grey80')
c.create_line(150, 0, 150, 450)  # линия х, у начала, х,у конца
c.create_line(300, 0, 300, 450)
c.create_line(0, 150, 450, 150)
c.create_line(0, 300, 450, 300)
c.pack(fill=BOTH, expand=1)

x = []
o = []
k = set()
def rect_func(event):
    if event.x < 150:
        if event.y < 150:
            c.create_line(0, 0, 150, 150, width=5)
            c.create_line(0, 150, 150, 0, width=5)
            k.add(1)
            x.append(2)
        elif event.y < 300:
            c.create_line(0, 150, 150, 300, width=5)
            c.create_line(150, 150, 0, 300, width=5)
            k.add(2)
            x.append(7)
        else:
            c.create_line(0, 300, 150, 450, width=5)
            c.create_line(150, 300, 0, 450, width=5)
            k.add(3)
            x.append(6)
    elif event.x < 300:
        if event.y < 150:
            c.create_line(150, 0, 300, 150, width=5)
            c.create_line(300, 0, 150, 150, width=5)
            k.add(4)
            x.append(9)
        elif event.y < 300:
            c.create_line(150, 150, 300, 300, width=5)
            c.create_line(300, 150, 150, 300, width=5)
            k.add(5)
            x.append(5)
        else:
            c.create_line(150, 300, 300, 450, width=5)
            c.create_line(300, 300, 150, 450, width=5)
            k.add(6)
            x.append(1)
    else:
        if event.y < 150:
            c.create_line(300, 0, 450, 150, width=5)
            c.create_line(450, 0, 300, 150, width=5)
            k.add(7)
            x.append(4)
        elif event.y < 300:
            c.create_line(300, 150, 450, 300, width=5)
            c.create_line(450, 150, 300, 300, width=5)
            k.add(8)
            x.append(3)
        else:
            c.create_line(300, 300, 450, 450, width=5)
            c.create_line(450, 300, 300, 450, width=5)
            k.add(9)
            x.append(8)

    r = randint(1, 9)
    while r in k:
        r = randint(1, 9)
    if r == 1:
        c.create_oval(0, 0, 150, 150)
        k.add(1)
        o.append(2)
    elif r == 2:
        c.create_oval(0, 150, 150, 300)
        k.add(2)
        o.append(7)
    elif r == 3:
        c.create_oval(0, 300, 150, 450)
        k.add(3)
        o.append(6)
    elif r == 4:
        c.create_oval(150, 0, 300, 150)
        k.add(4)
        o.append(9)
    elif r == 5:
        c.create_oval(150, 150, 300, 300)
        k.add(5)
        o.append(5)
    elif r == 6:
        c.create_oval(150, 300, 300, 450)
        k.add(6)
        o.append(1)
    elif r == 7:
        c.create_oval(300, 0, 450, 150)
        k.add(7)
        o.append(4)
    elif r == 8:
        c.create_oval(300, 150, 450, 300)
        k.add(8)
        o.append(3)
    elif r == 9:
        c.create_oval(300, 300, 450, 450)
        k.add(9)
        o.append(8)

    if sum(x) == 15:
        print("Вы выиграли")
    elif sum(o) == 15:
        print("Вы проиграли")

c.bind('<Button-1>', rect_func)

mainloop()
