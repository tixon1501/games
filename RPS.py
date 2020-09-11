import random


class gesture:  # Создание класса для жестов

    def __init__(self, name, losers):
        self.name = name
        self.losers = losers

    def victory(self, enemy):  # Нахождение победителя
        if self.name in enemy.losers:
            text = f'Победил противник т.к. показал {enemy.name}'
        elif enemy.name == self.name:
            text = 'Вы показали одинаковый жест'
        else:
            text = f'Вы победили т.к. противник показал {enemy.name}'
        return text


variant = [gesture('paper', {'rock', 'pistol', 'lightning', 'devil', 'dragon', 'water', 'air'}),
           gesture('air', {'fire', 'rock', 'pistol', 'lightning', 'devil', 'dragon', 'water'}),
           gesture('water', {'scissors', 'fire', 'rock', 'pistol', 'lightning', 'devil', 'dragon'}),
           gesture('dragon', {'snake', 'scissors', 'fire', 'rock', 'pistol', 'lightning', 'devil'}),
           gesture('devil', {'person', 'snake', 'scissors', 'fire', 'rock', 'pistol', 'lightning'}),
           gesture('lightning', {'wood', 'person', 'snake', 'scissors', 'fire', 'rock', 'pistol'}),
           gesture('pistol', {'wolf', 'wood', 'person', 'snake', 'scissors', 'fire', 'rock'}),
           gesture('rock', {'sponge', 'wolf', 'wood', 'person', 'snake', 'scissors', 'fire'}),
           gesture('fire', {'paper', 'sponge', 'wolf', 'wood', 'person', 'snake', 'scissors'}),
           gesture('scissors', {'air', 'paper', 'sponge', 'wolf', 'wood', 'person', 'snake'}),
           gesture('snake', {'water', 'air', 'paper', 'sponge', 'wolf', 'wood', 'person'}),
           gesture('person', {'dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'wood'}),
           gesture('wood', {'devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'}),
           gesture('wolf', {'lighting', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'}),
           gesture('sponge', {'pistol', 'lighting', 'devil', 'dragon', 'water', 'air', 'paper'})]

print('Пожалуйста введите название жеста на английском:')
name = input()

for i in variant:
    if name == i.name:
        player = gesture(name, i.losers)

if player is None:
    print('Введённый жест недоступен или не существует')
else:
    computer = random.choice(variant)
    print(player.victory(computer))
