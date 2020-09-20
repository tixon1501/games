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
    def __init__(self, destination, door, photo):
        self.destination = destination  # str
        self.door = door  # словарь
        self.photo = photo


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
    canvas.create_line(0, 650, 1000, 650, width=5)
    canvas.create_line(0, 700, 1000, 700, width=5)
    for i in range(21):
        canvas.create_line(50 * i, 650, 50 * i, 700, width=5)


image = []
image_dop = [load_image("beach1.jpg")]

maps = [
    sector("pier", load_image("pier.jpg"), {
           "beach": 1, "water": 1}, None, None),
    sector("beach", load_image("beach.jpg"), {
           "pier": 1}, {"dynamit", "shovel"}, None),
    sector("water", load_image("water.jpg"), {"beach": 1,
                                              "cave": 0, "submarine": 0}, {"key"}, None),
    sector("cave", load_image("cave.jpg"), {
           "water": 1, "rock_cave": 0}, {"net"}, None),
    sector("cave_rock", load_image("cave_rock.jpg"), {
           "cave": 0, "underground_lake": 1}, None, None),
    sector("underground_lake", load_image("underground_lake.jpg"), {
           "cave_rock": 1, "riches": 1}, None, {"dragon", "worm"}),
    sector("riches", load_image("riches.jpg"), {
           "underground_lake": 1, "treasure_cave": 1}, None, None),
    sector("submarine", load_image("submarine.jpg"), {"water": 0, "control": 1}, None, None),
    sector("control", load_image("control.jpg"), {"submarine": 1, "lake": 0, "uderwater_cave": 0}, None, None),
    sector("underwater_cave", load_image("underwater_cave.jpg"), {"pit": 1, "control": 0}, None, True),
    sector("pit", load_image("pit.jpg"), {"underwater_cave": 1, "big_pit": 0}, None, None),
    sector("big_pit", load_image("big_pit.jpg"), {"pit": 0}, None, True),
    sector("lake", load_image("lake.jpg"), {"control": 0, "glade": 0}, None, True),
    sector("glade", load_image("glade.jpg"), {"lake": 0, "forest": 0}, None, True),
    sector("forest", load_image("forest.jpg"), {"glade": 0, "hollow": 1}, None, None)
]
sect = maps[0]
set_image(sect.photo)
subjects = [
    subject("shovel", None, load_image("shovel.jpg")),
    subject("dinamit", {"cave_rock"}, load_image("dinamit.jpg")),
    subject("key", {"submarine"}, load_image("key.jpg")),
    subject("net", None, load_image("net.jpg"))
]


def moving(event):  # перемещение
    print(event.x, event.y)
    global sect, hero, canvas, maps
    if sect.destination == "pier":
        if 500 > event.y > 250:
            sect = maps[2]
        elif event.y > 500:
            sect = maps[1]
    elif sect.destination == "beach":
        if event.y < 400:
            sect = maps[0]
        elif 520 < event.y < 620 and 600 < event.x < 800 and subjects[0] in hero.subjects:
            set_image(image_dop[0])
            hero.subjects.add(subjects[1])
            maps[1].photo = image_dop[0]
        elif event.x < 200 and event.y > 450:
            hero.subjects.add(subjects[0])
    elif sect.destination == "water":
        if 300 < event.x < 750 and event.y < 100:
            sect = maps[0]
        elif event.y > 600 and "key" in hero.subjects:
            pass  # поподание в подводную лодку
        elif event.x > 750 and 600 > event.y > 400:
            sect = maps[3]
    elif sect.destination == "cave":
        if event.x < 500 and event.y < 350:
            sect = maps[2]
        elif event.y > 450 and event.x > 500 and subjects[1] in hero.subjects:
            sect = maps[4]
    elif sect.destination == "cave_rock":
        if 280 < event.y < 420 and 300 < event.x < 800:
            sect = maps[5]
        elif event.y > 500:
            sect = maps[3]
    elif sect.destination == "underground_lake":
        if event.y > 600:
            sect = maps[4]

    set_image(sect.photo)
    x = 0
    for i in hero.subjects:
        canvas.create_image(25 + 50 * x, 675, image=i.photo)
        x += 1


canvas.bind('<Button-1>', moving)

root.mainloop()