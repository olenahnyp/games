import game

kitchen = game.Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = game.Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")

ballroom = game.Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

dave = game.Enemy("Dave", "A smelly zombie")
dave.set_conversation("What's up, dude! I'm hungry.")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

tabitha = game.Enemy("Tabitha", "An enormous spider with countless eyes and furry legs.")
tabitha.set_conversation("Sssss....I'm so bored...")
tabitha.set_weakness("book")
ballroom.set_character(tabitha)

cheese = game.Item("cheese")
cheese.set_description("A large and smelly block of cheese")
ballroom.set_item(cheese)

book = game.Item("book")
book.set_description("A really good book entitled 'Knitting for dummies'")
dining_hall.set_item(book)

max = game.Friend("Max", "A small rabbit, your best friend")
max.set_conversation("Hi! Nice to meeet you. Don`t forget you can`t fight a monster\n\
with a wrong item.")
kitchen.set_character(max)

current_room = kitchen
backpack = []

dead = False

name_input = input('Enter your name to start the game: ')
print(f'Hello, {name_input}!\nWelcome to the game.')
start = input('Press enter if you`re ready')

if start == '':
    while dead == False:

        print("\n")
        current_room.get_details()

        inhabitant = current_room.get_character()
        if inhabitant is not None:
            inhabitant.describe()

        item = current_room.get_item()
        if item is not None:
            item.describe()

        command = input("> ")

        if command in ["north", "south", "east", "west"]:
            # Move in the given direction
            current_room = current_room.move(command)
        elif command == "talk":
            # Talk to the inhabitant - check whether there is one!
            if inhabitant is not None:
                inhabitant.talk()
        elif command == "fight":
            if inhabitant is not None:
                # Fight with the inhabitant, if there is one
                print("What will you fight with?")
                fight_with = input()

                # Do I have this item?
                if fight_with in backpack:
                    if inhabitant.fight(fight_with) == True:
                        # What happens if you win?
                        print(f'You fend {inhabitant.name} off with the {inhabitant.weakness}')
                        print("Hooray, you won the fight!")
                        current_room.character = None
                        if inhabitant.get_defeated() == 2:
                            print("Congratulations, you have vanquished the enemy horde!")
                            dead = True
                    elif inhabitant.fight(fight_with) == False:
                        # What happens if you lose?
                        print(f'{inhabitant.name} crushes you, puny adventurer!')
                        print("Oh dear, you lost the fight.")
                        print("That's the end of the game")
                        dead = True
                    elif inhabitant.fight(fight_with) == fight_with:
                        # olWhat happens if you try to fight a friend?
                        print(f'You cant`t fight with your friend with a {fight_with}')
                        print("You should find an enemy to fight with")
                else:
                    print("You don't have a " + fight_with)
            else:
                print("There is no one here to fight with")
        elif command == "take":
            if item is not None:
                print("You put the " + item.get_name() + " in your backpack")
                backpack.append(item.get_name())
                current_room.set_item(None)
            else:
                print("There's nothing here to take!")
        else:
            print("I don't know how to " + command)
