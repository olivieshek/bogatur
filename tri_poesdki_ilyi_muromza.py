"""
	TODO:
		доделать пути
		доделать персонажа
        поправить орфографию (род после чисел)
"""
import random
# игра
game = 1
if game != 1:
    sys.exit()
# ...
rand = 0
err = "Что-то не так. Введи снова: "

level = 0 # уровень;

enter = "Нажмите ENTER, чтобы продолжить."
# (персонаж) начало
print("Представьте, что Вы - богатырь. Сложновато, не правда ли?")
print("Я могу Вам помочь. Для начала, напишите Ваше имя.")

# имя
name = input()
print("Привет, %s!" % name)

# игра начало
print("Вы подъезжаете к трем дорожкам, на перекрестке камень лежит, а на том камне написано:")
print('''   «Кто вправо поедет - тому убитым быть, 
    кто влево поедет - тому богатым быть, 
    а кто прямо поедет - тому женатым быть»''')
print("Куда ехать?")
print('''
    1 - тому убитым быть,
    2 - тому богатым быть,
    3 - тому женатым быть.
    ''')
# убитым быть;
level = 1
user_choice = input("Введите число: ")
while user_choice not in ("1", "2", "3"):
    user_choice = 0
    user_choice = input(err)
    user_choice = input("Введите число: ")

if user_choice == "1":
    user_choice == 0
    print("Вы поехали по дороге, где Вы, судя по тому, что было написано на камне, обречены на смерть.")
    input(enter)
    print("Только Вы отъехали три версты, на Вас напали сорок разбойников.")

    print('''Что делать?
        1 - драться,
        2 - бежать,
        3 - попробовать переговорить.''')
    user_choice1 = input("Введи число: ")

    while user_choice1 not in ("1", "2", "3"):
        user_choice1 = 0
        user_choice1 = input(err)

# убит - ответвления;
    if user_choice1 == "1": # драться;
        print('''
- Не перчечьте мне дорогу! Дорогу моим кулакам!''')
        input(enter)
        print("...")
        print("Кровавая бойня, однако, получилась. У Вас слишком тяжелые ранения!")
        game = 0
    elif user_choice1 == "2": # бежать;
        print("Вы молча попятились назад.")
        rand = random.randrange(2)

        if rand == 1: # ОК
            print("Это рассмешило разбойников, они отвлеклись, и Вам удалось сбежать.")
            level = 2

        else: # УМЕР
            print("Разбойники только умехнулись. Но это не лишило их бдительности - Вас поймали и... Ну, Вы сами знаете, что было дальше.")
            game = 0

    else: # переговоры;
        print("- У-уважаемые... Разбойники! Позвольте договориться!")
        print('''
Очень бородатый дядька нахмурился:''')
        print("- Ты предлагаешь сыграть? Играть в кости - мой конек. Ты не сможешь выиграть!")
        print('''
Другой разбойник подошел к Вам ближе, протянул коробку в которой лежали игральные кости:''')
        print('''- Правила просты:
        Наберешь число больше, чем у хана - отпустим;
        Проиграешь - заберем все, что с собой и убьем!''')
        print('''
Страшно, но деваться некуда.''')
        print("- Играем!")

        # Игра в кости
        print(enter)
        print('''       Вы сели за стол и стали по очереди бросать кубики.''')
        # первый кубик
        input("Чтобы бросить первый кубик, нажмите ENTER.")
        dice = random.randrange(6)
        print("Вам выпало %s." % dice)
        print("Бородач кивнул головой, приказав разбойнику посмотреть, что Вам выпало.")
        if dice == 6:
            print("Бородач попытался скрыть удивление: конечно, ведь Вам выпало максимальное число!")
        else:
            print("Бородач посмеялся и тоже кинул кубик.")
        print("- Ну-с, моя очередь!")
        dice_han = random.randrange(6)
        print("Ему выпало %s. Сами думайте, хорошо это, или плохо." % dice_han)
        print("- Твоя очередь. Кидай еще один.")
        # второй кубик
        input("Чтобы бросить второй кубик, нажмите ENTER.")
        dice1 = random.randrange(6)
        dice += dice1
        print("Вам выпало %s. Всего - %s." % (dice1, dice))
        print("Ситуация накаливается.")
        print("Хан привстал, посмотрел на Ваши кости.")
        print('''
Это его будто никак не удивило.''')
        print("- Я кидаю! Несите мой любимый кубик!")
        print("Разбойник принес куб, который от количества золота на нем блистал.")
        print('''Бородач взял кубик, покатал по ладошке и, поцеловав, прошептал: "Не подведи!"''')
        dice_han1 = random.randrange(7)
        if dice_han1 == 7:
            print("Вы пригляделись: ему выпало... 7.")
            print('''
Вы настолько были удивлены, что вырвался крик:''')
            print("- Так нечестно!")
            print("- Все честно. Не надо тут!..")

elif user_choice == "2":
    print("богатым быть")

else:
    print("женатым быть")








