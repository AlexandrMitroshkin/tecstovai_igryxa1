from time import *

WEAPONS = {
    "sword": {"damage": 35},
    "mace": {"damage": 40},
    "bow": {"damage": 25}, }

ARMOR = {
    'shirt': {'armor_strength': 5},
    'leather_jacket': {'armor_strength': 20},
    'chainmail': {'armor_strength': 35},
    'steel_armor': {'armor_strength': 50}}


class Human:

    def __init__(self, name, money, hp, weapon_name, damage, armor_name, armor_strength):
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

        your_hp_with_armor = self.gettr_hp() + self.armor_strength

        enemy_hp_with_armor = enemy.gettr_hp() + enemy.armor_strength

        your_damage = enemy_hp_with_armor - self.damage

        enemy_damage = your_hp_with_armor - enemy.damage

        while self.is_alive() and enemy.is_alive():

            # Атакующий наносит удар защищающемуся

            print(
                f'Удар {self.name} атакует {enemy.name} с силой {self.damage} используя {self.weapon_name}, его защищает {self.armor_name}')

            enemy.settr_hp(your_damage)

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
                f'Удар {self.name} атакует {enemy.name} с силой {self.damage} используя {self.weapon_name}, его защищает {self.armor_name}')

            self.settr_hp(enemy_damage)

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
            sleep(2)


class Player(Human):
    def __init__(self, name, money, hp, weapon_name, damage, armor_name,
                 armor_strength):  # у этого класса в атрибуте assortiment у этого класса в атрибуте assortiment
        # добавляется больше значений
        super().__init__(name, money, hp, weapon_name, damage, armor_name, armor_strength)

        self.assortiment = {'vodka': 15, 'bread': 3, 'меч': 150, 'shirt': 25}

    def move_to_new_location(self, location):
        match location:
            case 'Пригородный рынок':
                print('Теперь вы в пригородном рынке\n '
                      'дрогие вещи сдесь стоят дороже , такие как мечи латы  '
                      'крч теперь ты в новой локации')




class Ogr(Human):
    def __init__(self, name, money, hp, weapon_name, damage, armor_name,
                     armor_strength):                                                           # у этого класса в атрибуте assortiment
                                                                                                # добавляется больше значений
        super().__init__(name, money, hp, weapon_name, damage, armor_name, armor_strength)

        self.assortiment = {'vodka': 15, 'bread': 3, 'kokain': 100, 'mace': 150, 'shirt': 25, }




class Torgash(Human):
    def __init__(self, name, money, hp, weapon_name, damage, armor_name,
                 armor_strength):                                               # у этого класса в атрибуте assortiment у этого класса в атрибуте assortiment
                                                                                    # добавляется больше значений
        super().__init__(name, money, hp, weapon_name, damage, armor_name, armor_strength)

        self.assortiment = {'vodka': 15, 'meat': 30, 'apple': 1, 'fish': 15, 'milk': 10, 'bread': 3,
                            'меч': 150, 'leather_jacket': 60, 'shirt': 25, 'chainmail': 150, 'steel_armor': 300}


Alex = Player("Алеша Попович", 300, 100, 'sword', 30, 'shirt', 5)

Axmet = Torgash('Ахмет', 1000, 100, 'mace', 35, 'leather_jacket', 20)

Yzbek = Torgash('Шермухамаджумма', 1000, 100, 'bow', 35, 'shirt', 20)

Yrgash = Ogr("Робин", 300, 100, 'mace', 30, 'shirt', 5)

Varhcha = Ogr("Виктор", 300, 100, 'mace', 30, 'shirt', 5)

print(Alex.assortiment)

print(Yrgash.assortiment)

# Alex.buy('kokain', Yrgash)
#
# print(Alex.assortiment)
#
# print(Yrgash.assortiment)
