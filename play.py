from PIL import Image, ImageTk
from tkinter import Tk
from tkinter.ttk import Frame, Label
import sys
from tkinter import Tk, Canvas, Frame, BOTH, NW, Button
# from tkinter import *


class sector:
    def __init__(self, destination, photo, exits, subjects, monsters):
        self.destination = destination
        self.photo = photo  # полное название файла
        self.exits = exits  # словарь
        self.subjects = subjects  # класс
        self.monsters = monsters  # класс


class subject:
    def __init__(self, destination, door, photo, effects):
        self.destination = destination  # str
        self.door = door  # словарь
        self.photo = photo
        self.effect = effects  # описание эффекта, строка


class monster:
    def __init__(self, live, destination, best_weapon, attack_power, subjects):
        self.live = live
        self.destination = destination
        self.best_weapon = best_weapon
        self.attack_power = attack_power
        self.subjects = subjects


class weapon:
    def __init__(self, attack, chance, photo, destination):
        self.attack = attack
        self.chance = chance
        self.photo = photo
        self.destination = destination


class armor:
    def __init__(self, protection, chance, photo, destination, evasion):
        self.protection = protection
        self.chance = chance
        self.photo = photo
        self.destination = destination
        self.evasion = evasion


""" Сектора """

maps = [
    sector("pier", "pier.jpg", {"beach": 1, "water": 1}, None, None),
    sector("beach", "beach.jpg", {"pier": 1}, {"dynamite", "shovel"}, None),
    sector("water", "water.jpg", {"beach": 1,
                                  "cave": 0, "submarine": 0}, {"key"}, None),
    sector("cave", "cave.jpg", {"water": 1, "rock_cave": 0}, {"net"}, None),
    sector("cave_rock", "cave_rock.jpg", {
           "cave": 0, "underground_lake": 1}, None, None),
    sector("underground_lake", "underground_lake.jpg", {
           "cave_rock": 1, "riches": 1}, None, {"dragon", "worm"}),
    sector("riches", "riches.jpg", {
           "underground_lake": 1, "treasure_cave": 1}, None, None),
]

monsters = [

]

hero = monster(1000, "hero", None, 100, set())

root = Tk()
root.geometry('1080x720')

canvas = Canvas(root, width=1000, height=700)
canvas.pack()


def load_image(name):
    img = Image.open(name)
    img.thumbnail((1000, 700), Image.ANTIALIAS)
    return ImageTk.PhotoImage(img)


def set_image(image):
    canvas.delete("all")
    canvas.create_image(500, 350, image=image)

image = []
sect = maps[0]

for i in maps:
    image.append(load_image(i.photo))

set_image(image[0])

def moving(event):  # перемещение
    print(event.y)
    global sect, hero, canvas
    if sect.destination == "pier":
        if 500 > event.y > 250:
            sect = maps[2]
            set_image(image[2])
        elif event.y > 500:
            sect = maps[1]
            set_image(image[1])
    elif sect.destination == "beach":
        if event.y < 250:
            sect = maps[0]
            set_image(image[0])
    elif sect.destination == "water":
        if 300 < event.x < 750 and event.y < 100:
            sect = maps[0]
            set_image(image[0])
        elif event.y > 600 and "key" in hero.subjects:
            pass # поподание в подводную лодку
        elif event.x > 750 and 600 > event.y > 400:
            sect = maps[3]
            set_image(image[3])
    elif sect.destination == "cave":
        if event.x < 500 and event.y < 350:
            sect = maps[2]
            set_image(image[2])


"""image2 = load_image("cave.jpg")



def naz():
    t1['text'] = "Город Назрань был основан..."
    set_image(image2)

def mag():
    t1['text'] = "Город Магас был основан..."
    set_image(image)

def kar():
    t1['text'] = "Город Карабулак был основан..."
    set_image(image2)

def mal():
    t1['text'] = "Город Малгобек был основан..."
    set_image(image)

t1 = Label(root)
t1.place(x=200, y=50)

t2 = Label(root, text="Описание 2")
t2.place(x=200, y=100)

t3 = Label(root, text="Описание 3")
t3.place(x=200, y=150)

btn1 = Button(root, text="Назрань", width=25, command=naz)
btn1.place(x=25, y=240)

btn2 = Button(root, text="Магас", width=25, command=mag)
btn2.place(x=240, y=240)

btn3 = Button(root, text="Карабулак", width=25, command=kar)
btn3.place(x=25, y=280)

btn4 = Button(root, text="Малгобек", width=25, command=mal)
btn4.place(x=240, y=280)"""

canvas.bind('<Button-1>', moving)

root.mainloop()
