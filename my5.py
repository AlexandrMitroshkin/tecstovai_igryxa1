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
        self.assortiment = {'vodka': 15, 'bread': 3, 'kokain': 100}

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

    def settr_hp(self, amount1):                # геттры и сеттры атрибутов
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
        if self.gettr_hp() > 0:
            return True

    def fight(self, enemy):
        your_hp_with_armor = self.gettr_hp() + self.armor_strength

        enemy_hp_with_armor = enemy.gettr_hp() + enemy.armor_strength

        your_damage = enemy_hp_with_armor - self.damage

        enemy_damage = your_hp_with_armor - enemy.damage

        while self.is_alive() and enemy.is_alive():

            # Атакующий наносит удар защищающемуся

            print(
                f'Удар {self.name} атакует {enemy.name} с силой {self.damage} используя {self.weapon_name}, его защищает {self.armor_name}')

            # your_hp_with_armor = self.gettr_hp() + self.armor_strength

            # enemy_damage = your_hp_with_armor - enemy.damage


            your_damage = enemy_hp_with_armor - self.damage

            enemy_hp_with_armor = enemy.gettr_hp() + enemy.armor_strength

            enemy.settr_hp(your_damage)

            enemy_hp_with_armor = enemy.gettr_hp() + enemy.armor_strength

            your_damage = enemy_hp_with_armor - self.damage


            # your_hp_with_armor = self.gettr_hp() + self.armor_strength

            enemy_damage = your_hp_with_armor - enemy.damage

            print(f'{enemy.name} покачнулся, а уровень здоровья упал до {enemy.gettr_hp()}')

            # Проверить, жив ли защищающийся

            if not enemy.is_alive():
                print(f'{enemy.name} проиграл в этом нелегком бою но в последний момент успел сбежать')
                break

            # Защищающийся наносит удар атакующему

            your_hp_with_armor = self.gettr_hp() + self.armor_strength

            enemy_hp_with_armor = enemy.gettr_hp() + enemy.armor_strength

            your_damage = enemy_hp_with_armor - self.damage

            enemy_damage = your_hp_with_armor - enemy.damage

            print(
                f'Удар {self.name} атакует {enemy.name} с силой {self.damage} используя {self.weapon_name}, его защищает {self.armor_name}')

            self.settr_hp(enemy_damage)

            your_hp_with_armor = self.gettr_hp() + self.armor_strength

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
    def berserk(self):
        pass


class Torgash(Human):
    def __init__(self, name, money, hp, weapon_name, damage, armor_name, armor_strength):         #  у этого класса в атрибуте assortiment у этого класса в атрибуте assortiment
                                                                                                                    # добавляется больше значений
        super().__init__(name, money, hp, weapon_name, damage, armor_name, armor_strength)

        self.assortiment = {'vodka': 15, 'meat': 30, 'apple': 1, 'fish': 15, 'milk': 10, 'bread': 3, 'kokain': 100,
                            'меч': 150}


# Alex = Player("Алеша Попович", 300, 100, 'sword', 30, 'shirt', 5)
#
# Lox = Torgash('Ахмет', 1000, 100, 'mace', 35, 'leather_jacket', 20)
#
# Alex.buy('apple', Lox)
#
# print(Alex.assortiment)
#
# print(Lox.assortiment)
#
# Alex.print_info()
#
# Alex.fight(Lox)




