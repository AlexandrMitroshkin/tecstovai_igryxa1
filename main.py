from time import *



# print('Дратути игрок , ты будешь играть за Алешу Поповича , который вчера так набухался что забыл как тут оказался '
#       'и ему очент хочется есть . Ты должен ему помочь и купить у торгашей еды , лучше покупать чем грабить у них есть охрана .'
#       'Ты можешь менять локации и заниматься перекупкой , и разбогатеть на этом   ')

class Human:
    betta = 0

    def __init__(self, name, money, hp, bronia, straight, oryjie):
        self.name = name
        self.money = money
        self.hp = hp
        self.bronia = bronia
        self.straight = straight
        self.oryjie = oryjie
        self.assortiment = {'vodka': 15, 'bread': 3, 'kokain': 100}

    def strike(self, enemy):
        print('Ydar ' + self.name + 'атакует ' + enemy.name + ' с силой ' + str(
            self.straight) + 'используя' + self.oryjie + "\n")
        enemy.bronia -= self.straight
        if enemy.bronia < 0:
            enemy.hp += enemy.bronia
            enemy.bronia = 0
        print(
            enemy.name + ' покачнулся .\n Класс его броня упал до ' + str(enemy.bronia) + ' а, уровень здоровья до ' + str(
                enemy.hp) + '\n')

    def fight(self, enemy):
        while self.hp > 0 and enemy.hp > 0:
            self.strike(enemy)
            if enemy.hp <= 0:
                print(enemy.name, ' пал в этом не легком бою \n')
                break
            sleep(5)

            enemy.strike(self)
            if self.hp <= 0:
                print(self.name, ' пал в этом не легком бою \n')
                break
            sleep(5)

    def print_info(self):
        print('Герой', self.name)
        print('хп', self.hp)
        print('броня', self.bronia)
        print('удар', self.straight)
        print('оружие', self.oryjie)
        print('деньги', self.money)

    def sell(self, q, buyer):
        if q in self.assortiment:
            buyer.assortiment[q] = self.assortiment[q]
            del self.assortiment[q]
        else:
            print('Такого предмета нема ')

    def buy(self, w, saleman):
        if w in saleman.assortiment:
            saleman.sell(w, self)
        else:
            print('Такого предмета нема ')


class Player(Human):
    def berserk(self):
        pass




class Torgash(Human):
    def __init__(self, name, money, hp, bronia, straight, oryjie):
        super().__init__(name, money, hp, bronia, straight, oryjie)
        self.assortiment = {'vodka': 15, 'meat': 30, 'apple': 1, 'fish': 15, 'milk': 10, 'bread': 3, 'kokain': 100,
                            'меч': 150}

    def force_to_buy_watermalon(self):
        pass


Alex = Player("Алеша Попович", 300, 100, 30, 3, 'кулак')

Lox = Torgash('Ахмет', 1000, 100, 10, 25, 'меч')

Alex.buy('apple',Lox)
print(Alex.assortiment)
print(Lox.assortiment)
Alex.fight(Lox)
