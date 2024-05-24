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
        print("Если buyer был в другой локации то герой  быренько к нему прибежал ")
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
        print('Если saleman был в другой локации , то  герой  быренько к нему прибежал  ')
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
    def __init__(self, name, money, hp, weapon_name, armor_name):  # у этого класса в атрибуте assortiment у этого класса в атрибуте assortiment
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
    def __init__(self, name, money, hp, weapon_name, armor_name,):
                                                                        # у этого класса в атрибуте assortiment у этого класса в атрибуте assortiment
                                                                        # добавляется больше значений
        super().__init__(name, money, hp, weapon_name,armor_name)

        self.assortiment = {'vodka': 15, 'meat': 30, 'apple': 1,
                            'fish': 15, 'milk': 10, 'bread': 3,
                            'sword': 150, 'mace': 175, 'bow': 100,
                            'leather_jacket': 60, 'shirt': 25, 'chainmail': 150,
                            'steel_armor': 300, 'kokain': 150}


class Torgash_of_the_suburb_market(Human):
    def __init__(self, name, money, hp, weapon_name, armor_name,):
                                                                        # у этого класса в атрибуте assortiment у этого класса в атрибуте assortiment
                                                                        # добавляется больше значений
        super().__init__(name, money, hp, weapon_name, armor_name)

        self.assortiment = {'vodka': 4.5, 'meat': 10, 'apple': 0.5,
                            'fish': 4, 'milk': 3, 'bread': 1,
                            'меч': 200, 'leather_jacket': 100, 'shirt': 25,
                            'chainmail': 250, 'steel_armor': 500,'kokain': 200}


Alex = Player("Алеша Попович", 300, 100, 'sword', 'steel_armor')

Axmet = Torgash_of_the_center_market('Ахмет', 1000, 100, 'mace', 'leather_jacket')

Yzbek = Torgash_of_the_suburb_market('Шермухамаджумма', 1000, 100, 'bow', 'shirt')


# Alex.buy('mace', Axmet)
#
# Alex.buy('leather_jacket', Axmet)
#
# print(Alex.assortiment)
#
# Alex.change_weapons('mace')
#
# print(Alex.weapon_name, Alex.damage)
#
# Alex.change_armor('leather_jacket')
#
# print(Alex.armor_name, Alex.armor_strength)
#
# Alex.move_to_new_location('Логово Огров')

print('Здраствуй игрок , сейчас ты играешь в Алеша_Попович_Текстовая_игруха\n'
      'Это типо а ля открытый мир скайрима , сдесь есть 2 рынка и логово Огров . На рынках разные цены (попробуй на этом подзаработать)\n'
      'Ты спавнишься на центральном рынке где ты иожешь покупать оружие и броню у которой урон и прочность больше чем у твоих. \n'
      'На рынке ты видишь доску обьявлений где висит миссия по зачистке логова гоблинов за котрую обещанна награда , 500 монет , это немало\n'
      'ты можешь менять локации и помни что лучше подготовиться к походу в логово Огров(список доступныч методов пока не готов\n)'
      'список доступных тебе методов:\n'
      '1)Alex.move_to_new_location(location) , она перместит тебя в указанную локацию . Вот список доступных локаций \n'
      'LOCATIONS = {Пригородный рынок: Узбек; Логово Огров: Ургаш и Варча ;Центральный рынок: Ахмет}\n'
      '2)Alex.change_weapons(на что сменить) , этот метод меняет твое оружие на указанное . Вот список доступных , спарва у них урон\n'
      'sword 35 , mace  40 , bow 20\n'
      '3)Alex.change_armor(replacement_weapon) тоже самое что и с оружем но это броня , вот список\n'
      'shirt 5 , leather_jacket 10 , chainmail 20 , steel_armor 30\n'
      '4)ты можешь нападать Alex.fight(enemy)\n'
      '5)ты можешь попросить торновца показать ассортимент print(name.assortiment)\n'
      '6)ты мжешь покупать и продавать Alex.sell(что то) и Alex.buy(что то)'
      '7) Список персножей: Axmet(location - Центральный рынок) , Yzbek(location - Пригородный рынок), Alex(главный герой - вы),\n'
      ' также есть огры но их имена вам знать не обязательно  ')


