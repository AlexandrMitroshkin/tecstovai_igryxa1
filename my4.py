from time import *

WEAPONS = {
    "sword": {"damage": 35},
    "mace": {"damage": 40},
    "bow": {"damage": 25}, }

ARMOR = {
    'shirt': {'armor_strength': 1},
    'leather_jacket': {'armor_strength': 10},
    'chainmail': {'armor_strength': 20},
    'steel_armor': {'armor_strength': 30}}

LOCATIONS = {'Пригородный рынок': 'Узбек',
             'Логово Огров': 'Ургаш и Варча',
             'Центральный рынок': 'Ахмет'}

Torgahi = [Axmet , Yzbek]


class Human:

    def __init__(self, name, money, hp, weapon_name, armor_name):
        self.name = name
        self._money = money
        self._hp = hp
        self.assortiment = {}

        # Проверить, существует ли оружие в списке доступного оружия

        if weapon_name in WEAPONS:
            self.weapon_name = weapon_name
            self.damage = WEAPONS[weapon_name]["damage"]

        else:
            raise ValueError(f"Unknown weapon: {weapon_name}")

        if armor_name in ARMOR:
            self.armor_name = armor_name
            self.armor_strength = ARMOR[armor_name]['armor_strength']

        else:
            raise ValueError(f"Unknown armor: {armor_name}")

    def sell(self, q, buyer):
        print(f"Если {buyer.name} был в другой локации то герой  быренько к нему прибежал ")
        z = buyer.gettr_money()

        if q in self.assortiment and z >= self.assortiment[q]:
            price = self.assortiment[q]
            self.settr_money(price)
            buyer.settr_money(-price)
            buyer.assortiment[q] = self.assortiment[q]
            del self.assortiment[q]

        else:
            print('Либо предмет который вы хотите продать отсутсвует , либо у покупателя недостаточно денег')

    def buy(self, w, saleman):
        print(f'Если {saleman.name} был в другой локации , то  герой  быренько к нему прибежал  ')
        saleman.sell(w, self)

    def gettr_hp(self):
        return self._hp

    def settr_hp(self, amount1):  # геттры и сеттры атрибутов
        self._hp = amount1

    def gettr_money(self):
        return self._money

    def settr_money(self, amount2):
        self._money += amount2

    def print_info(self):
        print('Герой', self.name)

        print('Деньги', self.gettr_money())

        print('здоровье', self.gettr_hp())

        print('Оружие', self.weapon_name)

        print('Броня', self.armor_name)

        print('Сила оружия', self.damage)

        print('Крепкость брони', self.armor_strength)

    def is_alive(self):
        return self.gettr_hp() > 0

    def fight(self, enemy):
        print('Методика боя заключается в том что атакующий наносит урон зависящий от своего оружия по броне врага\n'
              'если броня прочнее чем оружие то урон не проходит . \n Броня  не портится от ударов она каждый раз сдерживает часть урона .\n'
              'Бой идет пока здоровье не кончится.')
        sleep(5)

        your_hp_with_armor = self.gettr_hp() + self.armor_strength

        enemy_hp_with_armor = enemy.gettr_hp() + enemy.armor_strength

        your_damage = enemy_hp_with_armor - self.damage

        enemy_damage = your_hp_with_armor - enemy.damage

        while self.is_alive() and enemy.is_alive():

            # Атакующий наносит удар защищающемуся

            print(
                f'Удар {self.name} атакует {enemy.name} с силой {self.damage} используя {self.weapon_name}, его защищает {self.armor_name}')

            enemy.settr_hp(your_damage)

            sleep(5)

            your_hp_with_armor = self.gettr_hp() + self.armor_strength
            # Переопределение всех переменных после нанесения урона
            # в этом заключалась ошибка над которой я работал око 7 часов поэтому возможно какие то из переменных
            # переопределены лишний раз но это лучше чем неработающий код
            enemy_hp_with_armor = enemy.gettr_hp() + enemy.armor_strength

            your_damage = enemy_hp_with_armor - self.damage

            enemy_damage = your_hp_with_armor - enemy.damage

            print(f'{enemy.name} покачнулся, а уровень здоровья упал до {enemy.gettr_hp()}')

            # Проверить, жив ли защищающийся

            if not enemy.is_alive():
                print(f'{enemy.name} проиграл в этом нелегком бою но в последний момент успел сбежать')
                break

            # Защищающийся наносит удар атакующему

            print(
                f'Удар {enemy.name} атакует {self.name} с силой {enemy.damage} используя {enemy.weapon_name}, его защищает {enemy.armor_name}')

            self.settr_hp(enemy_damage)

            sleep(5)

            your_hp_with_armor = self.gettr_hp() + self.armor_strength
            # Переопределение всех переменных после нанесения урона
            # в этом заключалась ошибка над которой я работал око 7 часов поэтому возможно
            # какие то из переменных
            # переопределены лишний раз но это лучше чем неработающий код
            enemy_hp_with_armor = enemy.gettr_hp() + enemy.armor_strength

            your_damage = enemy_hp_with_armor - self.damage

            enemy_damage = your_hp_with_armor - enemy.damage

            print(f'{self.name} покачнулся, а уровень здоровья упал до {self.gettr_hp()}')

            # Проверить, жив ли атакующий

            if not self.is_alive():
                print(f'{self.name} проиграл в этом нелегком бою но в последний момент успел сбежать ')
                break

            # Сделать паузу между ударами
            sleep(5)


class Ogr(Human):
    betta = 0

    def __init__(self, name, money, hp, weapon_name, armor_name):  # у этого класса в атрибуте assortiment
        # добавляется больше значений
        super().__init__(name, money, hp, weapon_name, armor_name)

        self.assortiment = {'vodka': 15, 'bread': 3, 'kokain': 150
            , weapon_name: 150, armor_name: 25, 'сигара': 100}

    def begging_for_mercy(self):
        print('Мы проиграли , мы уйдем только пощади , тебе дадут награду , пока он зазевался бежим\n'
              'крч ты лошара , но награду дадут ')

        self.betta += 1


class Player(Human):
    def __init__(self, name, money, hp, weapon_name,
                 armor_name):  # у этого класса в атрибуте assortiment у этого класса в атрибуте assortiment
        # добавляется больше значений
        super().__init__(name, money, hp, weapon_name, armor_name)

        self.assortiment = {'vodka': 15, 'bread': 3, 'sword': 150,
                            'shirt': 25, 'kokain': 100}

    def move_to_new_location(self, location):
        if location in LOCATIONS:
            match location:
                case 'Пригородный рынок':
                    print('Теперь вы в пригородном рынке\n дрогие вещи сдесь стоят дороже , такие как мечи латы  '
                          'крч теперь ты в новой локации.\n Здесь основной торгаш Ахмет')

                case 'Центральный рынок':
                    print(
                        'Теперь ты в центральном рынке сдесь фермерские продукты и недрогие предметы дороже чем в пригородном рынке.\n'
                        'Здесь основной торгаш Ахмет')

                case 'Логово Огров':
                    print('Теперь ты в логове огров, на тебя сейчас нападут')

                    Yrgash = Ogr("Ургаш", 300, 100, 'mace', 'leather_jacket')
                    Varhcha = Ogr("Варча", 300, 100, 'mace', 'chainmail')

                    Yrgash.fight(self)

                    if self.is_alive():
                        print(
                            'Ты выпил изцеляющее зелье и твои hp восстановились , но вдруг на тебя накидывается 2 огр')
                        sleep(3)

                        Varhcha.fight(self)

                        if Varhcha.is_alive:
                            print('Cьебывай с нашей земли!')
                        else:
                            Varhcha.begging_for_mercy()
                            print(
                                'после этого тяжелого боя вы вернулись на локацию Центральный рынок и получили у торгаша награду.')
                            self.settr_money(500)

    def change_weapons(self, replacement_weapon):
        if replacement_weapon in WEAPONS and replacement_weapon in self.assortiment:
            self.weapon_name = replacement_weapon
            self.damage = WEAPONS[replacement_weapon]["damage"]

        else:
            print('Либо такого оружия нет в игре , либо его нет в вашем ассортимнте')

    def change_armor(self, replacement_armor):
        if replacement_armor in ARMOR and replacement_armor in self.assortiment:

            self.armor_name = replacement_armor

            self.armor_strength = ARMOR[replacement_armor]["armor_strength"]

        else:
            print('Либо тако брони нет в игре , либо его нет в вашем ассортимнте')


class Torgash_of_the_center_market(Human):
    def __init__(self, name, money, hp, weapon_name, armor_name, ):
        # у этого класса в атрибуте assortiment у этого класса в атрибуте assortiment
        # добавляется больше значений
        super().__init__(name, money, hp, weapon_name, armor_name)

        self.assortiment = {'vodka': 15, 'meat': 30, 'apple': 1,
                            'fish': 15, 'milk': 10, 'bread': 3,
                            'sword': 150, 'mace': 175, 'bow': 100,
                            'leather_jacket': 60, 'shirt': 25, 'chainmail': 150,
                            'steel_armor': 300, 'kokain': 150}


class Torgash_of_the_suburb_market(Human):
    def __init__(self, name, money, hp, weapon_name, armor_name, ):
        # у этого класса в атрибуте assortiment у этого класса в атрибуте assortiment
        # добавляется больше значений
        super().__init__(name, money, hp, weapon_name, armor_name)

        self.assortiment = {'vodka': 4.5, 'meat': 10, 'apple': 0.5,
                            'fish': 4, 'milk': 3, 'bread': 1,
                            'меч': 200, 'leather_jacket': 100, 'shirt': 25,
                            'chainmail': 250, 'steel_armor': 500, 'kokain': 200}


Alex = Player("Алеша Попович", 300, 100, 'sword', 'steel_armor')

Axmet = Torgash_of_the_center_market('Ахмет', 1000, 100, 'mace', 'leather_jacket')

Yzbek = Torgash_of_the_suburb_market('Шермухамаджумма', 1000, 100, 'bow', 'shirt')

# Torg = [Axmet, Yzbek]


def get_location():
    print('Вот и список локаций и персонажей')
    print(LOCATIONS)


def F_Q():
    print("Введите сменое оружие")
    weapon = input()
    Alex.change_weapons(weapon)


def F_W():
    print("Ведите сменную броню ")
    armor = input()
    Alex.change_armor(armor)


def F_E():
    print("вот ваш инвентарь")
    print(Alex.assortiment)


def F_R():
    print("Укажи ассортимент какого торговца ты хочешь увидеть")
    print(
        'И если тот торшаш чей ассортимент ты хочешь посмотреть находтися в другой локации, то ты к нему быстренько прибежишь')
    torgash = input()

    if torgash == Axmet:
        print('Вот его товары')
        print(Axmet.assortiment)

    elif torgash == Yzbek:
        print('Вот его товары')
        print(Yzbek.assortiment)

    else:
        print('Сорян, но такого торгаша нет')


def F_T(saleman):
    print("Для покупки тебе нужно указать продавца , а затем товар")
    saleman = input()
    tovar = input()

    if saleman == Axmet:
        Alex.buy(tovar, Axmet)

    elif saleman == Yzbek:
        Alex.buy(tovar, Yzbek)

    else:
        print('Сорян, но такого торгаша нет')


def F_Y():
    print("Для продажи вещи из твоего инвентраря для начала тебе нужно будет указать вещь и покупателя ")
    tovar = input()
    buyer = input()

    if buyer == Axmet:
        Alex.sell(tovar, Axmet)

    elif buyer == Yzbek:
        Alex.sell(tovar, Yzbek)

    else:
        print('Сорян, но такого торгаша нет')


def F_U():
    print("Что бы началось сражене введи имя противника , если забыл их имена то вот они :")

    enemy = input()

    if enemy == Axmet:
        Alex.fight(Axmet)

    elif enemy == Yzbek:
        Alex.fight(Yzbek)

    else:
        print('Сорян, но такого врага нет')


def F_I():
    print("Для смены локации тебе нужно указать нужную тебе локацию")
    print('Вот список доступных:Центральный рынок , Пригородный рынок ')
    location = input()
    Alex.move_to_new_location(location)


spisok_funksi = {'Q': F_Q, 'W': F_W, 'E': F_E, 'R': F_R, 'T': F_T, 'Y': F_Y, 'U': F_U, 'I': F_I}

print('Для начала игры нажмите клавишу "A"')

a = input()

if a == 'A':
    print('Здраствуй игрок , сейчас ты играешь в Алеша_Попович_Текстовая_игруха\n'
          'Это типо а ля открытый мир скайрима, нажми клавишу "B" , если хочешь продолжить')
    print('')
    b = input()
    if b == 'B':
        print("Обучение:")
        print('крч Ты Алеша Попович и ты спавнишься на локации Центральный рынкок.  ')
        print('В игре всего 3 локации вот их список и персонажи обитающие там:\n'
              'Axmet(location - Центральный рынок) , Yzbek(location - Пригородный рынок), Alex(location - может менять , это главный герой тоесть вы ),\n'
              ' также есть огры , они обитают в локации "Логово Огров" , их имена вам знать не обязательно')
        print('')
        print(
            'В игре есть много оружия и брони взависмости от которых у тебя будут меняться урон и крепкость брони \n'
            'вот список оружия :sword 35 , mace  40 , bow 20 \n'
            'справа урон, слева название ,также ты можешь менять оружие используя клавишу "Q" после нажатия введите название оружия на которое вы хотите \n'
            'поменять ваше сейчашнее , но учтите оно должно быть в вашем инвентаре .\n'
            'Тоже самое вы можете провернуть с броней нажав клавишу "W" и введя сменную броню, вот её список:\n'
            'sword 35 , mace  40 , bow 20\n')
        print('')
        print('Кстати о инвентаре, нажав клавишу "E" будет выведен ваш инвентарь.\n'
              'Что бы пополнять инвентарь вам необходимо встреться с торговцем на одном из рынков\n'
              '\n ')
        print('')
        print('О торговле и рынках:\n'
              'сдесь есть 2 рынка на котроых разные цены , в пригородном рынке цены на фермерские товары ниже ,но на крутые товары вроде лат и мечей там цены выше\n '
              'чем на центральном.  '
              'что бы посмотреть то что предлагает торговец нажми на клавишу "R", ты увидишь цены на товары и сам ассортимент\n'
              'что бы купить товар нажми на клавишу "T", и введи товар который хочешь купить и он появится у тебя в инвентаре.\n'
              'Также ты можешь продавть торговцам вещи из своего инвентаря , нажав клавишу "Y"')
        print('')
        print('О боях:\n'
              'В игре ты можешь драться используя оружие и броню нажми на клавишу "U" и указав противника,вот их список')
        print('Axmet - он бывалый торгаш , не советую с ним драться , а если уж решил , то  остерегайся его булавы, \n'
              'Yzbek - он тоже серьезный тогаш, также как и с Ахмедом не рекомендую драться с ним .\n'
              'А вот с кем надо драться так это с ограми , переместившись в их логово там все увидишь и поймешь...\n'
              'но что бы с ними драться тебе нужно перейти в их логово , а эта команда только для остальных\n')
        print('')
        print('О сюжете:\n'
              'Ты проходясь по рынку увидел доску обьявлений, на висит листок с миссией высшего ранга \n'
              'она заключается в том что бы зачистить логово огров за её выполнение дают 500 монет')
        print('')
        print('О смене локаций:\n'
              'Что бы сменть локацию нужно нажать клавишу "I", и ввести локацию, список доступных предствален выше.\n'
              'Но учти что если ты выбрал локацию логово огров то там будет жарко.')
        print('')
        print('Ну все начинай , для продолжения нажми клавишу "С"')
        c = input()

        if c == "C":
            print('Ты успешно прошел обучение вводи команду!')
            d = input()

            for i in spisok_funksi:
                if i == d:
                    spisok_funksi[i]()
                    d = input()


                # else:
                #     print('Такой команды нет ')
                #     d = input()

    else:
        print('Ты нажал че то не то , соблюдай правила игры!')
        a = input()



