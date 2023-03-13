"""
Game Lviv.
"""
balance = 0
class Character:
    """
    Create a character.
    """
    def __init__(self, name, description):
        """
        Create attributes of a character.
        >>> gypsy = Enemy("Циган", "Чоловік, який непомітно може вкрасти в тебе всі гроші.")
        >>> gypsy.name
        'Циган'
        >>> gypsy.description
        'Чоловік, який непомітно може вкрасти в тебе всі гроші.'
        """
        self.name = name
        self.description = description
        self.conversation = None
        self.needed_item = None
        self.thanks = None
    def set_conversation(self, conversation):
        """
        Set conversation to a character.
        >>> gypsy = Enemy("Циган", "Чоловік, який непомітно може вкрасти в тебе всі гроші.")
        >>> gypsy.set_conversation("Чи немає у вас 15 гривень на проїзд або хоча б щось поїсти?")
        >>> gypsy.conversation
        'Чи немає у вас 15 гривень на проїзд або хоча б щось поїсти?'
        """
        self.conversation = conversation
    def talk(self):
        """
        Talk to a character.
        >>> gypsy = Enemy("Циган", "Чоловік, який непомітно може вкрасти в тебе всі гроші.")
        >>> gypsy.set_conversation("Чи немає у вас 15 гривень на проїзд або хоча б щось поїсти?")
        >>> gypsy.talk()
        [Циган каже]: Чи немає у вас 15 гривень на проїзд або хоча б щось поїсти?
        """
        print(f'[{self.name} каже]: {self.conversation}')
    def set_needed_item(self, needed_item):
        """
        Set needed item for a character.
        >>> gypsy = Enemy("Циган", "Чоловік, який непомітно може вкрасти в тебе всі гроші.")
        >>> gypsy.set_needed_item("пляцок")
        >>> gypsy.needed_item
        'пляцок'
        """
        self.needed_item = needed_item
    def get_needed_item(self):
        """
        Get needed item of a character.
        """
        return self.needed_item
    def set_thanks(self, thanks):
        """
        Set thanks for a character.
        >>> gypsy = Enemy("Циган", "Чоловік, який непомітно може вкрасти в тебе всі гроші.")
        >>> gypsy.set_thanks("Дякую за пляцок. Це краще, ніж твої гроші.")
        >>> gypsy.thanks
        'Дякую за пляцок. Це краще, ніж твої гроші.'
        """
        self.thanks = thanks
    def get_thanks(self):
        """
        Get thanks of a character.
        >>> gypsy = Enemy("Циган", "Чоловік, який непомітно може вкрасти в тебе всі гроші.")
        >>> gypsy.set_thanks("Дякую за пляцок. Це краще, ніж твої гроші.")
        >>> gypsy.get_thanks()
        [Циган каже]: Дякую за пляцок. Це краще, ніж твої гроші.
        """
        print(f'[{self.name} каже]: {self.thanks}')
    def describe(self):
        """
        Describe a character.
        >>> gypsy = Enemy("Циган", "Чоловік, який непомітно може вкрасти в тебе всі гроші.")
        >>> gypsy.describe()
        Циган тут. Чоловік, який непомітно може вкрасти в тебе всі гроші.
        """
        print(f'{self.name} тут. {self.description}')
    def get_name(self):
        """
        Get name of a character.
        >>> gypsy = Enemy("Циган", "Чоловік, який непомітно може вкрасти в тебе всі гроші.")
        >>> gypsy.get_name()
        'Циган'
        """
        return self.name

class Street:
    """
    Create a street.
    """
    def __init__(self, name):
        """
        Create attributes of a street.
        >>> lychakivska = Street("Личаківська")
        >>> lychakivska.name
        'Личаківська'
        """
        self.name = name
        self.description = None
        self.ways_to_go = []
        self.character = None
        self.item = None
        self.cafe = None
    def set_description(self, description):
        """
        Set description to a street.
        """
        self.description = description
    def get_description(self):
        """
        Get description of a street.
        """
        print(f"Ти знаходишся на вулиці {self.name}")
        print('-----------------------------------------')
        print(self.description)
        print('-----------------------------------------')
        for way in self.ways_to_go:
            print(f"Вулиця {way[0].name} {way[1]}.")
    def set_character(self, character):
        """
        Set a character on a street.
        """
        self.character = character
    def set_item(self, item):
        """
        Set an item on a street.
        """
        self.item = item
    def set_cafe(self, cafe):
        """
        Set a cafe on a street.
        """
        self.cafe = cafe
    def get_cafe(self):
        """
        Get a cafe which is on a street.
        """
        return self.cafe
    def get_character(self):
        """
        Get a character which is on a street.
        """
        return self.character
    def get_item(self):
        """
        Get an item which is on a street.
        """
        return self.item
    def link_street(self, new_street, side: str):
        """
        Link a street to another street.
        """
        self.ways_to_go.append((new_street, side))
        return self.ways_to_go
    def move(self, side):
        """
        Move to another street.
        """
        for way in self.ways_to_go:
            if way[1] == side:
                return way[0]

class Friend(Character):
    """
    Create a friend.
    """
    def __init__(self, name, description):
        """
        Create attributes of a friend.
        >>> friend = Friend("Друг", "Друг-богослов з УКУ")
        >>> friend.name
        'Друг'
        """
        super().__init__(name, description)
        self.bonus = None
    def get_money(self):
        """
        Get money from a friend.
        """
        global balance
        balance += 5
    def set_bonus(self, bonus):
        """
        Set a bonus a friend can give you.
        >>> granny = Friend("Бабуся", "Бабуся, якій потрібно допогти перейти вулицю.")
        >>> granny.set_bonus('пляцок')
        >>> granny.bonus
        'пляцок'
        """
        self.bonus = bonus
    def get_bonus(self):
        """
        Get bonus from a certain friend.
        """
        return self.bonus

class Enemy(Character):
    """
    Create an enemy.
    """
    def __init__(self, name, description):
        """
        Create attributes of an enemy.
        >>> gypsy = Enemy("Циган", "Чоловік, який непомітно може вкрасти в тебе всі гроші.")
        >>> gypsy.name
        'Циган'
        """
        super().__init__(name, description)
        self.bonus = None
    def get_money(self):
        """
        Lose all your money to an enemy.
        """
        global balance
        balance = 0

class Item:
    """
    Create an item.
    """
    def __init__(self, name):
        """
        Create attributes of an item.
        >>> map = Item("карта")
        >>> map.name
        'карта'
        """
        self.name = name
        self.description = None
    def set_description(self, description):
        """
        Set description to an item.
        >>> map = Item("карта")
        >>> map.set_description("Карта Львова, яка допоможе знайти будь-який шлях.")
        >>> map.description
        'Карта Львова, яка допоможе знайти будь-який шлях.'
        """
        self.description = description
    def get_description(self):
        """
        Get description of an item.
        >>> map = Item("карта")
        >>> map.set_description("Карта Львова, яка допоможе знайти будь-який шлях.")
        >>> map.get_description()
        Карта Львова, яка допоможе знайти будь-який шлях. Можеш взяти цей предмет.
        """
        print(f"{self.description} Можеш взяти цей предмет.")
    def get_name(self):
        """
        Get name of an item.
        >>> map = Item("карта")
        >>> map.get_name()
        'карта'
        """
        return self.name
    
class Building(Item):
    """
    Create a building.
    """
    def __init__(self, name):
        """
        Create attributes of a building.
        >>> cafe = Building("'Львівські круасани'")
        >>> cafe.name
        "'Львівські круасани'"
        """
        super().__init__(name)
    def get_description(self):
        """
        Get description of a building.
        >>> cafe = Building("'Львівські круасани'")
        >>> cafe.get_description()
        'Львівські круасани'. Можеш зайти туди.
        """
        print(f"{self.name}. Можеш зайти туди.")

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
