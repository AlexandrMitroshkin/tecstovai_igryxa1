from time import *


class Human:
    betta = 0

    def __init__(self, name, money, hp, key_bronia, key_damage,):
        self.name = name
        self._money = money
        self._hp = hp

        self.assortiment = {'vodka': 15, 'bread': 3, 'kokain': 100}

        self.dict_of_bronia = {}

        if key_bronia == "shirt":
            self.dict_of_bronia["shirt"] = 5

        elif key_bronia == 'Leather_jacket':
            self.dict_of_bronia["Leather_jacket"] = 20

        elif key_bronia == 'chainmail':
            self.dict_of_bronia["chainmail"] = 35

        elif key_bronia == 'steel_armor':
            self.dict_of_bronia["steel_armor"] = 70

        else:
            print('Такой брони не существует , просим вас не нарушать правила игры')

        self.dict_of_damage = {}

        if key_damage == "mace":
            self.dict_of_damage["mace"] = 100

        elif key_damage == 'fist':
            self.dict_of_damage["fist"] = 20

        elif key_damage == 'sword':
            self.dict_of_damage["sword"] = 105

        elif key_damage == 'bow':
            self.dict_of_damage["bow"] = 90

        else:
            print('Такого оружия не существует , просим вас не нарушать правила игры')

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



    # def strike(self, enemy, key_damage, key_bronia):
    #
    #     a = enemy.gettr_hp()
    #
    #     d = self.dict_of_damage[key_damage]
    #
    #     # if key_damage in self.dict_of_damage and key_bronia in self.dict_of_bronia:
    #
    #     print('Удар' + self.name + ' атакует ' + enemy.name + ' с силой ' + str(
    #         d) + 'используя' + key_damage + '\n')
    #     enemy.dict_of_bronia[key_bronia] -= d
    #     if enemy.dict_of_bronia[key_bronia] < 0:
    #         a += enemy.dict_of_bronia[key_bronia]
    #         enemy.dict_of_bronia[key_bronia] = 0
    #
    #
    #
    #
    # def strike(self, enemy, key_damage, key_bronia):
    #     a = enemy.gettr_hp()
    #     s = self.dict_of_bronia[key_bronia]
    #     if key_damage in self.dict_of_damage and key_bronia in self.dict_of_bronia:
    #         print('Удар' + self.name + ' атакует ' + enemy.name + ' с силой ' + str(
    #             self.dict_of_damage[key_damage]) + 'используя' + key_damage + '\n')
    #         enemy.dict_of_bronia[key_bronia] -= self.dict_of_damage[key_damage]
    #         if enemy.dict_of_bronia[key_bronia] < 0:
    #             a += enemy.dict_of_bronia[key_bronia]
    #             enemy.dict_of_bronia[key_bronia] = 0
    #         print(
    #             enemy.name + ' покакчеулся .\n Класс его броня упал до' + str(
    #                 enemy.dict_of_bronia[key_bronia]) + ' а, уровень здоровья до ' + str(
    #                 enemy.gettr_hp()) + '\n')
    #
    #
    #
    # def fight(self, enemy, key_damage, key_bronia):
    #     while self.gettr_hp() > 0 and enemy.gettr_hp() > 0:
    #         self.strike(enemy, key_damage, key_bronia)
    #         if enemy.gettr_hp() <= 0:
    #             print(enemy.name, 'проиграл в этом нелегком бою , но в последний момент успел сбежать \n')
    #             break
    #         sleep(5)
    #
    #         enemy.strike(self , key_damage, key_bronia)
    #         if self.gettr_hp() <= 0:
    #             print(self.name, 'проиграл в этом нелегком бою , но в последний момент успел сбежать \n')
    #             break
    #         sleep(5)

    def buy(self, w, saleman):
        saleman.sell(w, self)

    def gettr_hp(self):
        return self._hp

    def settr_hp(self, amount1):                                    # геттры и сеттры атрибутов
        self._hp += amount1

    def gettr_money(self):
        return self._money

    def settr_money(self, amount2):
        self._money += amount2


class Player(Human):
    def move_to_new_location(self):                             # потом тут будет функция
        pass


class Torgash(Human):
    def __init__(self, name, money, hp, key_bronia, key_damage):                                                            #  у этого класса в атрибуте assortiment
                                                                                                                                    # добавляется больше значений
        super().__init__(name, money, hp, key_bronia, key_damage)

        self.assortiment = {'vodka': 15, 'meat': 30, 'apple': 1, 'fish': 15, 'milk': 10, 'bread': 3, 'kokain': 100,
                            'sword': 100, 'mace': 90, 'bow': 50, 'shirt': 10, 'Leather_jacket': 50, 'chainmail': 110,
                            'steel_armor': 300}


Alex = Player("Алеша Попович", 400, 300, 'shirt', 'fist')

Lox = Torgash('Ахмет', 10000, 290, 'Leather_jacket', 'sword')  # name, money, hp, bronia , key

Lox.sell('steel_armor', Alex)

print(Alex.assortiment)                               # тестирования

print(Lox.assortiment)

print(Lox.dict_of_bronia)
print(Alex.dict_of_bronia)

Alex.fight(Lox,'mace','shirt')                      # хуйня которая должна была работать
