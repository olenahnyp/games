"""
Create a game.
"""

class Character:
    """
    Create a parent class character.
    """
    def __init__(self, name, description):
        """
        Create attributes all characters have.
        >>> dave = Enemy('Dave', 'A smelly zombie')
        >>> dave.name
        'Dave'
        >>> dave.description
        'A smelly zombie'
        """
        self.name = name
        self.description = description
        self.conversation = None

    def set_conversation(self, conversation):
        """
        Set a conversation for a character.
        >>> dave = Enemy('Dave', 'A smelly zombie')
        >>> dave.set_conversation("What's up, dude! I'm hungry.")
        >>> dave.conversation
        "What's up, dude! I'm hungry."
        """
        self.conversation = conversation

    def describe(self):
        """
        Describe a character.
        """
        description = f'{self.name} is here!\n'
        description += self.description
        print(description)

    def talk(self):
        """
        Talk to a character.
        >>> dave = Enemy('Dave', 'A smelly zombie')
        >>> dave.set_conversation("What's up, dude! I'm hungry.")
        >>> dave.talk()
        [Dave says]: What's up, dude! I'm hungry.
        """
        print(f'[{self.name} says]: {self.conversation}')


class Room:
    """
    Create a room.
    """
    def __init__(self, name: str):
        """
        Create attributes of a room.
        >>> kitchen = Room('Kitchen')
        >>> kitchen.name
        'Kitchen'
        """
        self.name = name
        self.description = None
        self.ways_to_go = []
        self.character = None
        self.item = None

    def set_description(self, description: str):
        """
        Set a description of a room.
        >>> kitchen = Room('Kitchen')
        >>> kitchen.set_description('A dank and dirty room buzzing with flies.')
        >>> kitchen.description
        'A dank and dirty room buzzing with flies.'
        """
        self.description = description

    def link_room(self, new_room, world_side: str):
        """
        Link a room to a different room.
        """
        self.ways_to_go.append((new_room, world_side))
        return self.ways_to_go

    def get_details(self):
        """
        Get details about a room.
        """
        details = self.name + '\n' + '--------------------' + '\n' + self.description + '\n'
        for way in self.ways_to_go:
            details += f'The {way[0].name} is {way[1]}\n'
        print(details[:-1])

    def set_character(self, character):
        """
        Set a character which is in a room.
        """
        self.character = character

    def set_item(self, item):
        """
        Set an item which is in a room.
        """
        self.item = item

    def get_character(self):
        """
        Get a character which is in a room.
        """
        return self.character

    def get_item(self):
        """
        Get an item which is in a room.
        """
        return self.item

    def move(self, world_side):
        """
        Move to a different room.
        """
        for way in self.ways_to_go:
            if way[1] == world_side:
                return way[0]


class Friend(Character):
    """
    Create a friend.
    """
    def __init__(self, name, description):
        """
        Create attributes of a friend.
        >>> max = Friend("Max", "A small rabbit, your best friend")
        >>> max.name
        'Max'
        """
        super().__init__(name, description)

    def fight(self, fight_with):
        """
        Fight with a friend (return an item because you can not
        fight with a friend).
        """
        return fight_with


class Enemy(Character):
    """
    Create an enemy.
    """
    defeated = 0
    def __init__(self, name, description):
        """
        Create attributes of an enemy.
        >>> dave = Enemy('Dave', 'A smelly zombie')
        >>> dave.description
        'A smelly zombie'
        """
        super().__init__(name, description)
        self.weakness = None

    def set_weakness(self, weakness):
        """
        Set a weakness for an enemy to kill him.
        >>> dave = Enemy('Dave', 'A smelly zombie')
        >>> dave.set_weakness('cheese')
        >>> dave.weakness
        'cheese'
        """
        self.weakness = weakness

    def fight(self, fight_with):
        """
        Fight with an enemy if you have an object which
        makes his weak.
        """
        if fight_with == self.weakness:
            Enemy.defeated += 1
        return fight_with == self.weakness

    def get_defeated(self):
        """
        Return a number an enemy was defeated.
        """
        return Enemy.defeated


class Item:
    """
    Create an item.
    """
    def __init__(self, name):
        """
        Create attributes of an item.
        >>> cheese = Item('cheese')
        >>> cheese.name
        'cheese'
        """
        self.name = name
        self.description = None

    def set_description(self, description):
        """
        Set a description for an item.
        >>> cheese = Item('cheese')
        >>> cheese.set_description('A large and smelly block of cheese')
        >>> cheese.description
        'A large and smelly block of cheese'
        """
        self.description = description

    def describe(self):
        """
        Describe an item.
        >>> book = Item('book')
        >>> book.set_description("A really good book entitled 'Knitting for dummies'")
        >>> book.describe()
        The [book] is here - A really good book entitled 'Knitting for dummies'
        """
        print(f'The [{self.name}] is here - {self.description}')

    def get_name(self):
        """
        Get name of an item.
        >>> cheese = Item('cheese')
        >>> cheese.get_name()
        'cheese'
        """
        return self.name


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())