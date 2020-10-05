from PIL import Image, ImageTk
from tkinter.ttk import Frame, Label
import sys
from tkinter import Tk, Canvas, Frame, BOTH, NW, Button
# from tkinter import *
from random import randint
import keyboard
import time
from tkinter import messagebox as mb
from tkinter import filedialog as fd


class Sector:
    def __init__(self, destination, photo, exits, subjects, monsters):
        self.destination = destination
        self.photo = photo  # полное название файла
        self.exits = exits  # словарь
        self.subjects = subjects  # класс
        self.monsters = monsters  # класс

    def __str__(self):
        self.res = f"\t Sector('{self.destination}', {self.photo}, {self.exits}, {self.subjects}, {self.monsters}), \n"
        return self.res


class Subject:
    def __init__(self, destination, door, photo):
        self.destination = destination  # str
        self.door = door  # словарь
        self.photo = photo


class Monster:
    def __init__(self, live, destination, subjects, attack, chance, photo):
        self.live = live
        self.destination = destination
        self.subjects = subjects
        self.attack = attack
        self.chance = chance
        self.photo = photo

    def __str__(self):
        self.res = f"Monster ('{self.live}, {self.destination}, {self.subjects}, {self.weapon}"
        return self.res


"""class Weapon:
    def __init__(self, attack, chance, photo, destination):
        self.attack = attack
        self.chance = chance
        self.photo = photo
        self.destination = destination"""


class armor:
    def __init__(self, protection, chance, photo, destination, evasion):
        self.protection = protection
        self.chance = chance
        self.photo = photo
        self.destination = destination
        self.evasion = evasion


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
image_dop = [load_image("beach1.jpg")]

"""weapons = [  # оружие
    Weapon(100, 50, photo=load_image("sword.jpg"), destination="sword"),
    Weapon(80, 80, load_image("arm.jpg"), "arm")
    Weapon(100, 80, load_image("fin.jpg"), "fin")]"""

monsters = [  # монстры
    Monster(500, "dracon", None, 80, 80, load_image("draсon.gif")),
    Monster(700, "shark", None, 100, 80, load_image("shark.gif")),

]

subjects = [
    Subject("shovel", None, load_image("shovel.jpg")),
    Subject("dinamit", {"cave_rock"}, load_image("dinamit.jpg")),
    Subject("key", {"submarine"}, load_image("key.jpg")),
    Subject("net", None, load_image("net.jpg")),
    Subject("cable", {"big_pit"}, load_image("cable.jpg")),
    Subject("boat", {"glade"}, load_image("boat.jpg")),
    Subject("axe", {"forest"}, load_image("axe.jpg")),
    Subject("hammer", {"hollow"}, load_image("hammer.jpg")),
    Subject("key_s", {"riches"}, load_image("key_s.jpg")),
    Subject("1001101001000100", {"cave_control"},
            load_image("1001101001000100.jpg")),
    Subject("0100111000100111", {"lake"}, load_image("0100111000100111.jpg")),
    Subject("1010001110010011", {"underwater_cave"},
            load_image("1010001110010011.jpg")),
    Subject("scrap", {"seaweed", "bunker"}, load_image("scrap.jpg"))
]

maps = [
    Sector("pier", load_image("pier.jpg"), {
           "beach": 1, "water": 1}, None, None),
    Sector("beach", load_image("beach.jpg"), {
           "pier": 1}, {subjects[0], subjects[1], subjects[6], subjects[9]}, None),
    Sector("water", load_image("water.jpg"), {"beach": 1,
                                              "cave": 0, "submarine": 0}, {subjects[2]}, None),
    Sector("cave", load_image("cave.jpg"), {
           "water": 1, "rock_cave": 0}, {"net"}, None),
    Sector("cave_rock", load_image("cave_rock.jpg"), {
           "cave": 0, "underground_lake": 1}, {subjects[7]}, None),
    Sector("underground_lake", load_image("underground_lake.jpg"), {
           "cave_rock": 1, "riches": 1}, None, [monsters[0]]),
    Sector("riches", load_image("riches.jpg"), {
           "underground_lake": 1, "treasure_cave": 1}, {subjects[8]}, None),
    Sector("submarine", load_image("submarine.jpg"),
           {"water": 0, "control": 1}, {subjects[5]}, None),
    Sector("control", load_image("control.jpg"), {
           "submarine": 1, "lake": 0, "uderwater_cave": 0}, None, None),
    Sector("underwater_cave", load_image("underwater_cave.jpg"),
           {"pit": 1, "control": 0}, None, True),
    Sector("pit", load_image("pit.jpg"), {
           "underwater_cave": 1, "big_pit": 0}, None, None),
    Sector("big_pit", load_image("big_pit.jpg"),
           {"pit": 0}, {subjects[12]}, True),
    Sector("lake", load_image("lake.jpg"), {
           "control": 0, "glade": 0}, None, True),
    Sector("glade", load_image("glade.jpg"), {
           "lake": 0, "forest": 0}, {subjects[11]}, True),
    Sector("forest", load_image("forest.jpg"), {
           "glade": 0, "hollow": 1}, None, None),
    Sector("seaweed", load_image("seaweed.jpg"), {
           "submarine": 1, "bunker": 1}, None, True),
    Sector("bunker", load_image("bunker.jpg"), {"seaweed": 1}, True, None),
    Sector("cave_control", load_image("cave_control.jpg"),
           {"control": 0, "riches": 1}, {subjects[10]}, True),
    Sector("hollow", load_image("hollow.jpg"),
           {"forest": 1}, {subjects[4]}, True)
]
sect = Sector("start", load_image("start.jpg"), None, None, None)
set_image(sect.photo)

hero = Monster(
    1000, "hero", {subjects[2]}, 100, 50, load_image("hero.jpg"))
monstr = None


def moving(event):  # перемещение
    print(event.x, event.y)
    global sect, hero, canvas, maps, monstr
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
        elif event.y > 600 and subjects[2] in hero.subjects:
            sect = maps[7]
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
        elif 330 < event.x < 510 and 310 < event.y < 450 and subjects[8] in hero.subjects:
            sect = maps[6]
    elif sect.destination == "submarine":
        if 390 < event.x < 520 and 200 < event.y < 280:
            sect = maps[8]
        elif event.y < 50:
            sect = maps[2]
        elif 820 < event.x < 880 and 340 < event.y < 410 and subjects[12] in hero.subjects:
            sect = maps[15]
    elif sect.destination == "control":
        if event.y > 600:
            sect = maps[7]
        elif 220 < event.x < 330 and 320 < event.y < 430 and subjects[9] in hero.subjects:
            sect = maps[17]
        elif 340 < event.x < 430 and 320 < event.y < 430 and subjects[10] in hero.subjects:
            sect = maps[12]
        elif 400 < event.x < 540 and 320 < event.y < 430 and subjects[11] in hero.subjects:
            sect = maps[9]
    elif sect.destination == "seaweed":
        if event.x < 100:
            sect = maps[7]
        elif event.y > 600 and subjects[12] in hero.subjects:
            sect = maps[16]
    elif sect.destination == "bunker":
        if event.y > 600:
            sect = maps[15]
    elif sect.destination == "lake":
        if event.y > 500:
            sect = maps[8]
        elif event.y < 270 and subjects[5] in hero.subjects:
            sect = maps[13]
    elif sect.destination == "glade":
        if event.y > 600:
            sect = maps[12]
        elif 300 < event.y < 400 and subjects[6] in hero.subjects:
            sect = maps[14]
    elif sect.destination == "forest":
        if event.y > 600:
            sect = maps[13]
        elif event.x > 600 and subjects[7] in hero.subjects:
            sect = maps[18]
    elif sect.destination == "hollow":
        if event.y > 600:
            sect = maps[14]
    elif sect.destination == "underwater_cave":
        if event.y < 200:
            sect = maps[8]
        elif event.y > 600:
            sect = maps[10]
    elif sect.destination == "pit":
        if 180 < event.x < 550 and 220 < event.y < 510 and subjects[4] in hero.subjects:
            sect = maps[11]
        elif event.y > 550:
            sect = maps[9]
    elif sect.destination == "big_pit":
        if event.y < 100:
            sect = maps[10]
    elif sect.destination == "cave_control":
        if 520 < event.x < 620 and 340 < event. y < 410 and subjects[8] in hero.subjects:
            sect = maps[6]
        elif event.y > 550:
            sect = maps[8]
    elif sect.destination == "riches":
        if event.x < 400:
            sect = maps[5]
        if event.x > 700:
            sect = maps[17]
    elif sect.destination == "start":
        decrypt(event)
    set_image(sect.photo)
    x = 0
    for i in hero.subjects:
        canvas.create_image(25 + 50 * x, 675, image=i.photo)
        x += 1
    canvas.create_line(0, 650, 1000, 650, width=5)
    canvas.create_line(0, 700, 1000, 700, width=5)
    for i in range(21):
        canvas.create_line(50 * i, 650, 50 * i, 700, width=5)
    if not (sect.monsters == None or sect.monsters == True):
        monstr = sect.monsters[0]
        battle()


def battle():  # битва
    global sect, hero, canvas, maps, monstr, root
    output = []
    while hero.live > 0 and monstr.live > 0:
        ran = randint(1, 100)
        if ran > (100 - monstr.chance):
            at = monstr.attack
        else:
            at = int(monstr.attack * ran / 100)
        hero.live -= at

        ran = randint(1, 100)
        if ran > (100 - hero.chance):
            at = hero.attack
        else:
            at = int(hero.attack * ran / 100)
        monstr.live -= at
        output.append(f"hero.live: {hero.live}; monstr.live: {monstr.live}\n")
    else:
        string = ""
        for i in output:
            string += i
        if hero.live > 0:
            mb.showinfo(
                "Победа", f"{string}Вы победили монстра {monstr.destination}, у вас осталосm {hero.live} жизней")
            sect.monsters.pop(0)
            if len(sect.monsters) == 0:
                sect.monsters = None
        else:
            mb.showinfo(
                "Проигрыш", f"{string}Вы проиграли монстру {monstr.destination}, игра самостоятельно закроется через 5 секунд")
            time.sleep(5)
            root.destroy()


def saved():  # сохранять: hero, monsters, sect
    answer = mb.askyesno(title="Сохранения", message="Сохранить игру?")
    if answer == True:
        file_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
                                                    ("All files", "*.*")))
        f = open(file_name, 'w')
        f.write("monsters\n")
        for i in monsters:
            s = f"{i.live}\t{i.destination}\n"
            f.write(s)
        s = f"{hero.live}\t{hero.destination}\t{hero.attack}\t{hero.chance}\t"
        f.write(s)
        for i in hero.subjects:
            s = f"{i.destination}\t"
            f.write(s)
        s = f"\nsect={sect.destination}"
        f.write(s)
        f.close()
    # time.sleep(1)
    root.destroy()
# сохранение и рассохранение списка предметов


def decrypt(event):
    # красивый экран выбора "Новоя игра", "Загрузить", "Выход"
    global hero, monsters, sect
    if 390 < event.x < 600 and 160 < event.y < 220:
        pass
        sect = maps[0]
        set_image(sect.photo)
    elif 390 < event.x < 600 and 280 < event.y < 340:
        file_name = fd.askopenfilename()
        f = open(file_name)
        for string in f:
            string = string.replace('\n', '')
            temp = string.split('\t')
            print(temp)
            if string == "monsters":
                pass
            elif "hero" in temp:
                hero.live = int(temp[0])
                # hero.subjects = string[2]
                hero.attack = int(temp[2])
                hero.chance = int(temp[3])
                sub = temp[4:]
                for i in sub:
                    for k in subjects:
                        if i == k.destination:
                            hero.subjects.add(k)
            elif len(temp) == 2:
                for i in monsters:
                    if i.destination == temp[1]:
                        i.live = int(temp[0])
            elif "sect" in string:
                temp = string.split('=')
                for i in maps:
                    if i.destination == temp[1]:
                        sect = i
                        set_image(sect.photo)
        f.close()
    elif 390 < event.x < 600 and 400 < event.y < 460:
        root.destroy()


# decrypt()
canvas.bind('<Button-1>', moving)
keyboard.add_hotkey('Ctrl + 1', lambda: print('Hello'))
root.protocol("WM_DELETE_WINDOW", saved)
root.mainloop()
