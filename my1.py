class Human:
    betta = 0

    def __init__(self, name, money, hp, bronia, straight, oryjie):
        self.name = name
        self._money = money
        self._hp = hp
        self._bronia = bronia
        self._straight = straight
        self._oryjie = oryjie
        self.assortiment = {'vodka': 15, 'bread': 3, 'kokain': 100}

    def sell(self, q, buyer):
        if q in self.assortiment:
            price = self.assortiment[q]
            self.settr_money(price)
            buyer.settr_money(-price)
            buyer.assortiment[q] = self.assortiment[q]
            del self.assortiment[q]
        else:
            print('Такого предмета нет ')

    # def strike(self, enemy):
    #     print('Ydar ' + self.name + 'атакует ' + enemy.name + ' с силой ' + str(
    #         self._straight) + 'используя' + self._oryjie + "\n")
    #     enemy._bronia -= self._straight
    #     if enemy._bronia < 0:
    #         enemy._hp += enemy._bronia
    #         enemy._bronia = 0
    #     print(
    #         enemy.name + ' покачнулся .\n Класс его броня упал до ' + str(
    #             enemy._bronia) + ' а, уровень здоровья до ' + str(
    #             enemy._hp) + '\n')
    #
    # def fight(self, enemy):
    #     while self._hp > 0 and enemy._hp > 0:
    #         self.strike(enemy)
    #         if enemy._hp <= 0:
    #             print(enemy.name, ' пал в этом не легком бою \n')
    #             break
    #         sleep(5)
    #
    #         enemy.strike(self)
    #         if self._hp <= 0:
    #             print(self.name, ' пал в этом не легком бою \n')
    #             break
    #         sleep(5)

    def buy(self, w, saleman):
        saleman.sell(w, self)

        # name, money, hp, bronia, straight, oryjie   сеттры и геттры

    def gettr_hp(self):
        return self._hp

    def settr_hp(self, amount1):
        self._hp += amount1

    def gettr_money(self):
        return self._money

    def settr_money(self, amount2):
        self._money += amount2

    def gettr_bronia(self, ):
        return self._bronia

    def settr_bronia(self, amount3):
        self._bronia += amount3

    def gettr_straight(self):
        return self._straight

    def settr_straight(self, amount4):
        self._straight += amount4

    def gettr_oryjie(self):
        return self._oryjie

    def settr_oryjie(self, amount5):
        self._oryjie = amount5


class Player(Human):
    def move_to_new_location(self):
        pass


class Torgash(Human):
    def __init__(self, name, money, hp, bronia, straight, oryjie):
        super().__init__(name, money, hp, bronia, straight, oryjie)
        self.assortiment = {'vodka': 15, 'meat': 30, 'apple': 1, 'fish': 15, 'milk': 10, 'bread': 3, 'kokain': 100,}



# class Torgash_oryjiem(Human):
#     def __init__(self, name, money, hp, bronia, straight, oryjie):
#         super().__init__(name, money, hp, bronia, straight, oryjie)
#         self.assortiment = {'sword':100, 'mace':90,'bow':50}


Alex = Player("Алеша Попович", 300, 100, 30, 3, 'кулак')

Lox = Torgash('Ахмет', 1000, 100, 10, 25, 'меч')

Lox.sell('meat', Alex)

print(Alex.assortiment)

print(Lox.assortiment)

print(Alex.gettr_money())

print(Lox.gettr_money())
print(Lox.gettr_hp())
print(Lox.gettr_bronia())
print(Lox.gettr_straight())
print(Lox.gettr_oryjie())

