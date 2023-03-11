import game_lviv

print("О, ні! Лекція з основ програмування починається через 30 хвилин, а ти досі не в УКУ.\n\
Ти зараз на проспекті Свободи, але тобі потрібно доїхати на Козельницьку. Якщо підеш пішки, \n\
то запізнишся, тому потрібно знайти 15 гривень на маршрутку. Ти поспішав, тому забув взяти \n\
гаманець, тому поквапся і знайти людей, які зможуть дати тобі гроші. Можеш перевірити свій \n\
баланс, написавши команду 'баланс', або перевірити, що знаходиться у твоєму рюкзаку,\n\
написавши команду 'рюкзак'.")

start = input("Напиши 'старт', щоб почати гру.\n> ")

prospect_svobody = game_lviv.Street("Проспект Свободи")
prospect_svobody.set_description("Проспект Свободи є однією з найбільш відомих та центральних вулиць у Львові.\n\
Тут знаходяться також кілька пам'ятників архітектури, серед яких варто виділити величезний Палац 'Україна',\n\
Оперний театр, пам'ятник Тарасу Шевченку та інші визначні споруди.")

gorodotska = game_lviv.Street("Городоцька")
gorodotska.set_description("Вулиця Городоцька має багату історію та багато пам'яток архітектури, таких як\n\
Галицький районний будинок, Храм святого Юра, Палац Потоцьких та інші.")

teatralna = game_lviv.Street("Театральна")
teatralna.set_description("Вулиця Театральна у Львові знаходиться в самому серці історичної частини міста і\n\
відома своїм театром та кінотеатром, які знаходяться вздовж вулиці. Тут знаходяться також кілька пам'ятників\n\
архітектури, серед яких варто виділити театр імені Марії Заньковецької, кінотеатр 'Довженко', палац Левандівських\n\
та інші визначні будівлі.")

kopernyka = game_lviv.Street("Коперника")
kopernyka.set_description("Вулиця отримала свою назву на честь відомого польського астронома Ніколая Коперника.\n\
Вона відома своїми пам'ятками архітектури, зокрема це будинок Коперника, колишній готель 'Дністер' та інші.")

lychakivska = game_lviv.Street("Личаківська")
lychakivska.set_description("Вулиця отримала свою назву на честь міста Личаків, яке розташовувалось на заході від Львова.\n\
Тут знаходяться такі визначні пам'ятки архітектури, як костел святого Юра, палац Сапєгів, будинки національної науки та інші.")

prospect_svobody.link_street(kopernyka, "наліво")
kopernyka.link_street(gorodotska, "направо")
teatralna.link_street(lychakivska, "направо")
teatralna.link_street(prospect_svobody, "наліво")
lychakivska.link_street(teatralna, "наліво")
lychakivska.link_street(kopernyka, "направо")
gorodotska.link_street(teatralna, "направо")

tourist = game_lviv.Friend("Турист", "Хлопець з Англії, який загубився на вулиці Театральна.\n\
Йому потрібно пройти до проспекти Свободи. Підкажи йому, щоб отримати нагороду.")
tourist.set_conversation("Hello! Can you help me please? I want to get to Prospect Svobody.\n\
Where should I go?")
tourist.set_needed_item("карта")
tourist.set_thanks("Thank you so much!")
teatralna.set_character(tourist)

blogger = game_lviv.Friend("Блогер", "Дівчинка, яка знімає відео в Tik-Tok. Потрібно відповісти\n\
на 3 запитання, які стосуються історії Львова, щоб отримати нагороду.")
blogger.set_conversation("Привіт, не хочеш взяти участь у моєму відео?")
blogger.set_needed_item("книжка")
blogger.set_thanks("Дякую за участь. Відео вийшло дуже крутим!")
prospect_svobody.set_character(blogger)

granny = game_lviv.Friend("Бабуся", "Бабуся, якій потрібно допогти перейти вулицю. Допоможи, щоб\n\
отримати нагороду.")
granny.set_conversation("Вітаю! Чи не могли б ви допомогти мені?")
granny.set_needed_item("руки")
granny.set_thanks("Дякую за допомогу. Тримай пляцок, який я спекла.")
granny.set_bonus('пляцок')
gorodotska.set_character(granny)

friend = game_lviv.Friend("Друг", "Друг-богослов з УКУ, який допоможе тобі в будь-яку хвилину.\n\
Однак, ти не можеш просто так взяти гроші. Пригости його кавою, щоб отримати нагороду.")
friend.set_conversation("Привіт, у тебе хіба немає сьогодні першої пари?")
friend.set_needed_item("кава")
friend.set_thanks("Дякую за каву. Тримай гроші на дорогу.")
kopernyka.set_character(friend)

gypsy = game_lviv.Enemy("Циган", "Чоловік, який непомітно може вкрасти в тебе всі гроші.")
gypsy.set_conversation("Чи немає у вас 15 гривень на проїзд?")
gypsy.set_needed_item("пляцок")
gypsy.set_thanks("Дякую за пляцок. Це краще, ніж твої гроші.")
lychakivska.set_character(gypsy)

cafe = game_lviv.Building("'Львівські круасани'")
cafe.set_description("Сьогодні тут відбувається щось цікаве. Можливо, зайдеш і подивишся?")
lychakivska.set_cafe(cafe)

book = game_lviv.Item("книжка")
book.set_description("Книжка історії Львова.")
gorodotska.set_item(book)

map = game_lviv.Item("карта")
map.set_description("Карта Львова, яка допоможе знайти будь-який шлях.")
kopernyka.set_item(map)

current_street = prospect_svobody
backpack = ['руки']
playing = True

playing = True
while playing:
    print("\n")
    current_street.get_description()
 
    character = current_street.get_character()
    if character is not None:
        print('-----------------------------------------')
        character.describe()
 
    item = current_street.get_item()
    if item is not None:
        print('-----------------------------------------')
        item.get_description()

    cafe = current_street.get_cafe()
    if cafe is not None:
        print('-----------------------------------------')
        cafe.get_description()

    command = input("> ")

    if command == "наліво" or command == "направо":
        current_street = current_street.move(command)
    elif command == "говорити":
        character.talk()
    elif command == "допомогти":
        if character is not None:
            print("Чим ти можеш допомогти?")
            help_item = input("> ")
            if help_item in backpack:
                if character.get_name() == 'Циган':
                    if help_item == character.get_needed_item():
                        character.get_thanks()
                    else:
                        character.get_money()
                        print("На жаль, у тебе вкрали всі гроші.")
                        playing = False
                    current_street.character = None
                elif help_item == character.get_needed_item():
                    character.get_thanks()
                    if character.bonus != None:
                        print(f"Ти отримав бонус - {character.get_bonus()}.")
                        backpack.append(character.get_bonus())
                    else:
                        print("Молодець! Ти допоміг і отримав 5 гривень.")
                        character.get_money()
                    current_street.character = None
                    current_street.item = None
                    backpack.remove(help_item)
                    if game_lviv.balance == 15:
                        print("Ти переміг! Тепер спокійно можеш сідати в 53 маршрутку і їхати в УКУ.")
                        playing = False
                else:
                    print("На жаль, ти програв і не встиг доїхати на першу пару :(")
                    playing = False
            else:
                print(f"На жаль, у тебе немає {help_item}.")
        else:
            print("Тут немає кому допомагати...")
    elif command == "взяти":
        if item != None:
            item_name = item.get_name()
            print(f"Ти взяв {item_name}.")
            backpack.append(item_name)
            current_street.set_item(None)
        else:
            print("На цій вулиці нічого немає.")
    elif command == "баланс":
        print(f"У тебе зараз {game_lviv.balance} гривень.")
    elif command == "зайти":
        print("Ви стали нашим 10000-м клієнтом. У подарунок отримуєте каву.")
        backpack.append("кава")
        current_street.cafe = None
    elif command == "рюкзак":
        print(backpack)
    else:
        print("Такої команди немає.")
