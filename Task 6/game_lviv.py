balance = 0
class Character:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.conversation = None
        self.needed_item = None
        self.thanks = None
    def set_conversation(self, conversation):
        self.conversation = conversation
    def talk(self):
        print(f'[{self.name} каже]: {self.conversation}')
    def set_needed_item(self, needed_item):
        self.needed_item = needed_item
    def get_needed_item(self):
        return self.needed_item
    def set_thanks(self, thanks):
        self.thanks = thanks
    def get_thanks(self):
        print(f'[{self.name} каже]: {self.thanks}')
    def describe(self):
        print(f'{self.name} тут. {self.description}')
    def get_name(self):
        return self.name

class Street:
    def __init__(self, name):
        self.name = name
        self.description = None
        self.ways_to_go = []
        self.character = None
        self.item = None
        self.cafe = None
    def set_description(self, description):
        self.description = description
    def get_description(self):
        print(f"Ти знаходися на вулиці {self.name}")
        print('-----------------------------------------')
        print(self.description)
        print('-----------------------------------------')
        for way in self.ways_to_go:
            print(f"Вулиця {way[0].name} {way[1]}.")
    def set_character(self, character):
        self.character = character
    def set_item(self, item):
        self.item = item
    def set_cafe(self, cafe):
        self.cafe = cafe
    def get_cafe(self):
        return self.cafe
    def get_character(self):
        return self.character
    def get_item(self):
        return self.item
    def link_street(self, new_street, side: str):
        self.ways_to_go.append((new_street, side))
        return self.ways_to_go
    def move(self, side):
        for way in self.ways_to_go:
            if way[1] == side:
                return way[0]

class Friend(Character):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.bonus = None
    def get_money(self):
        global balance
        balance += 5
    def set_bonus(self, bonus):
        self.bonus = bonus
    def get_bonus(self):
        return self.bonus

class Enemy(Character):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.bonus = None
    def get_money(self):
        global balance
        balance = 0

class Item:
    def __init__(self, name):
        self.name = name
        self.description = None
    def set_description(self, description):
        self.description = description
    def get_description(self):
        print(f"{self.description} Можеш взяти цей предмет.")
    def get_name(self):
        return self.name
    
class Building(Item):
    def __init__(self, name):
        super().__init__(name)
    def get_description(self):
        print(f"{self.name}. Можеш зайти туди.")
