from tkinter import *


class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Крестики-нолики")
        self.master.resizable(False, False)
        self.width, self.height = self.master.winfo_screenwidth() // 2 - 250, self.master.winfo_screenheight() // 2 - 268
        self.master.geometry('500x500+{}+{}'.format(self.width, self.height))

        self.canvas = Canvas(width=500, height=500, bg="white")
        window_create = Button(width=40, height=1, text="Добавить фигуру",
                               command=lambda: FigureWindow(self, self.get_coords()))
        self.canvas.pack()
        window_create.pack()

    def get_coords(self):
        self.master.update_idletasks()
        coords = self.master.geometry()
        coords = coords.split('+')
        width_window, height_window = int(coords[1]), int(coords[2])
        return [width_window, height_window]


class FigureWindow:
    def __init__(self, main_window, w_h_array):  # Создаём окно
        self.main = main_window
        self.window = Toplevel(main_window.master)
        w, h = w_h_array[0], w_h_array[1]
        self.window.geometry("190x165+{}+{}".format(510 + w, h))  # Формируем окно
        self.window.title("Фигура")
        self.window.resizable(False, False)

        self.typeVar = IntVar()  # Переменная
        self.typeVar.set(0)

        self.colors = ["black", "white", "snow", "linen", "lavender", "misty rose", "gray", "blue", "cyan", "yellow",
                       "gold",
                       "coral", "red", "purple", "khaki", "thistle", "indian red"]
        self.outline_color, self.fill_color = self.colors[0], self.colors[1]  # Цвета

        frames, elements = self.window_content(self.window)  # Контект окна
        self.pack_content(frames, elements)  # Упаковка окна
        self.bind_events(elements)  # Подсоединение событий

    def window_content(self, window):  # Заполняем окно
        frame_global = Frame(window)
        frame_dot_one, frame_dot_two, frame_figure, \
        frame_fill_color, frame_outline_color = (Frame(frame_global) for i in range(5))

        x1, y1 = Label(frame_dot_one, text="x1"), Label(frame_dot_one, text="y1")
        x2, y2 = Label(frame_dot_two, text="x2"), Label(frame_dot_two, text="y2")
        self.x1_entry, self.y1_entry = Entry(frame_dot_one, width=5), Entry(frame_dot_one, width=5)
        self.x2_entry, self.y2_entry = Entry(frame_dot_two, width=5), Entry(frame_dot_two, width=5)

        square = Radiobutton(frame_figure, text="Прямоугольник", variable=self.typeVar, value=0)
        oval = Radiobutton(frame_figure, text="Овал", variable=self.typeVar, value=1)

        fill_label = Label(frame_fill_color, text="Заливка: ")
        outline_label = Label(frame_outline_color, text="Грани:     ")
        self.color_fill = Listbox(frame_fill_color, width=210, height=1)
        self.color_outline = Listbox(frame_outline_color, width=210, height=1)
        for i in self.colors:
            self.color_outline.insert(END, i)
            if i == "white":
                self.color_fill.insert(0, i)
            else:
                self.color_fill.insert(END, i)

        draw_button = Button(frame_global, text="Нарисовать фиругу",
                             command=lambda: self.create_figure(
                                 (self.x1_entry, self.y1_entry, self.x2_entry, self.y2_entry)))

        return ((frame_dot_one, frame_dot_two, frame_figure, frame_fill_color, frame_outline_color, frame_global),
                ((x1, self.x1_entry, y1, self.y1_entry), (x2, self.x2_entry, y2, self.y2_entry),
                 (square, oval), (fill_label, self.color_fill), (outline_label, self.color_outline), draw_button))

    def pack_content(self, frames, elements):  # Упаковываем окно
        for i in frames: i.pack()
        for i in range(len(elements)):
            if isinstance(elements[i], tuple):
                length = len(elements[i])
            else:
                length = 1
            for j in range(length):
                if length == 1:
                    elements[i].pack(anchor=N)
                elif i == 2:
                    elements[i][j].pack(anchor=W)
                else:
                    elements[i][j].pack(side=LEFT)

    def bind_events(self, elements):  # Подсоединяем события
        self.color_fill.bind("<FocusIn>", lambda event: self.list_select(self.color_fill))
        self.color_outline.bind("<FocusIn>", lambda event: self.list_select(self.color_outline))
        self.color_fill.bind("<Return>", lambda event: self.list_change_item(self.color_fill))
        self.color_outline.bind("<Return>", lambda event: self.list_change_item(self.color_outline))
        self.color_fill.bind("<FocusOut>", lambda event: self.list_deselect(listbox=self.color_fill))
        self.color_outline.bind("<FocusOut>", lambda event: self.list_deselect(listbox=self.color_outline))
        for i in range(len(elements)):
            if i == len(elements) - 1:
                elements[i].bind("<FocusOut>", lambda event: self.list_deselect(Listbox()))
            elif i == 3 or i == 4:
                pass
            else:
                for j in range(len(elements[i])):
                    elements[i][j].bind("<Button-1>", lambda event: self.list_deselect(Listbox()))

    def list_select(self, listbox):
        listbox["height"] = len(self.colors)
        self.window.geometry("190x{}".format(165 + len(self.colors) * 15))

    def list_deselect(self, listbox):
        if listbox != self.color_fill and listbox != self.color_outline:
            self.color_fill["height"] = 1
            self.color_outline["height"] = 1
        else:
            listbox["height"] = 1
        self.window.geometry("190x165")

    def list_change_item(self, listbox):
        if listbox == self.color_fill:
            self.fill_color = listbox.get(listbox.curselection())
        elif listbox == self.color_outline:
            self.outline_color = listbox.get(listbox.curselection())
        listbox.insert(0, listbox.get(listbox.curselection()))
        listbox.delete(listbox.curselection())
        self.list_deselect(listbox)

    def create_figure(self, elements):
        x1, y1, x2, y2 = (elements[i].get() for i in range(4))
        if self.typeVar.get():
            self.main.canvas.create_oval((x1, y1), (x2, y2), fill=self.color_fill.get(0),
                                         outline=self.color_outline.get(0))
        else:
            self.main.canvas.create_rectangle((x1, y1), (x2, y2), fill=self.color_fill.get(0),
                                              outline=self.color_outline.get(0))
        self.window.destroy()


def main():
    root = Tk()
    MainWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()