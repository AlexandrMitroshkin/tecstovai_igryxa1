from time import *
from enum import Enum


class Weapon(Enum):
    FIST = 5
    BOW = 30
    SWORD = 35
    MACE = 40


class Armor(Enum):
    SHIRT = 5
    LEATHER_JACKET = 20
    CHAINMAIL = 30
    STELL_ARMOR = 50


class Human:

    def __init__(self, name, money, hp, weapon, armor):
        self.name = name
        self._money = money
        self._hp = hp
        self.assortiment = {'vodka': 15, 'bread': 3, 'kokain': 100}

        if isinstance(weapon, Weapon):
            self.weapon = weapon
        else:
            print('Такого оружия не существует , просим вас не нарушать правила игры')

        if isinstance(armor, Armor):
            self.armor = armor
        else:
            print('Такой брони не существует , просим вас не нарушать правила игры')

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
        self._hp += amount1

    def gettr_money(self):
        return self._money

    def settr_money(self, amount2):
        self._money += amount2

    def print_info(self):
        print('Герой', self.name)
        print('Деньги', self.gettr_money())
        print('здоровье', self.gettr_hp())
        print('Оружие', self.weapon)
        print('Броня', self.armor)
        print('Сила оружия', self.weapon.value)
        print('Крепкость брони', self.armor.value)

    def strike(self, enemy, weapon_attack, armor_protection):

        damage = self.weapon.value

        enemy_hp_with_armor = enemy.armor.value + enemy.gettr_hp()

        print(
            f'Удар {self.name} атакует {enemy.name} с силой {damage} используя {weapon_attack}, его защищает {armor_protection}')

        enemy_hp_with_armor -= damage

        print(f'{enemy.name} покачнулся, а уровень здоровья до {enemy_hp_with_armor}')

        return enemy_hp_with_armor

    def Fight(self, enemy, weapon_attack, armor_protection):

        your_hp = self.gettr_hp() + self.weapon.value

        enemy_hp_with_armor = enemy.armor.value + enemy.gettr_hp()

        print('СПРАВКА :  Формула боя заключается в том что броня добавляется к hp и бой идет пока hp не кончатся')

        sleep(5)

        while your_hp > 0 and enemy_hp_with_armor > 0:
            self.strike(enemy, weapon_attack, armor_protection)
            if enemy_hp_with_armor <= 0:
                print(f'{enemy.name},  пал в этом не легком бою, но в последний момент успел сбежать')
                break
            sleep(5)

            your_hp = self.gettr_hp() + self.weapon.value

            enemy_hp_with_armor = enemy.armor.value + enemy.gettr_hp()

            enemy.strike(self, weapon_attack, armor_protection)

            if your_hp <= 0:
                print(f'{self.name},  пал в этом не легком бою, но в последний момент успел сбежать')
                break
            sleep(5)


class Player(Human):
    def berserk(self):
        pass


class Torgash(Human):
    def __init__(self, name, money, hp, weapon, armor):
        super().__init__(name, money, hp, weapon, armor)
        self.assortiment = {'vodka': 15, 'meat': 30, 'apple': 1, 'fish': 15, 'milk': 10, 'bread': 3, 'kokain': 100,
                            'меч': 150}


Alex = Player("Алеша Попович", 300, 100, Weapon.FIST, Armor.SHIRT)

Lox = Torgash('Ахмет', 1000, 100, Weapon.SWORD, Armor.LEATHER_JACKET)

Alex.buy('apple', Lox)
print(Alex.assortiment)
print(Lox.assortiment)
# Alex.print_info()
Alex.Fight(Lox, Weapon.FIST, Armor.SHIRT)
