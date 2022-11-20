# from abc import ABCMeta, abstractmethod
# from random import randint, randrange

# """案例一：奥特曼打小怪兽"""

# class Fighter(object, metaclass=ABCMeta):
#     """战斗者"""

#     # 通过__slots__魔法限定对象可以绑定的成员变量
#     __slots__ = ("_name", "_hp")

#     def __init__(self, name, hp):
#         """初始化方法

#         :param name: 名字
#         :param hp: 生命值

#         """
#         self._name = name
#         self._hp = hp
    
#     @property
#     def name(self):
#         return self._name
    
#     @property
#     def hp(self):
#         return self._hp 

#     @hp.setter
#     def hp(self, hp):
#         self._hp = hp if hp >= 0 else 0

#     @property
#     def alive(self):
#         return self._hp > 0
    
#     @abstractmethod
#     def attack(self, other):
#         """攻击

#         : param other: 被攻击的对象
#         """
#         pass

# class Ultraman(Fighter):
#     """奥特曼"""

#     __slots__ = ("_name", "_hp", "_mp")

#     def __init__(self, name, mp, hp):
#         """初始化方法

#         :param name: 名字
#         :param hp: 生命
#         :param mp: 魔法值
#         """
#         super().__init__(name, hp)
#         self._mp = mp

#     def attack(self, other):
#         other._hp = randint(15,25)

#     def huge_attack(self, other):
#         """究极必杀技(打掉对方至少50点火四分之三的血)

#         :param other: 被攻击的对象

#         :return: 使用成功返回True 否则返回False
#         """
#         if self._mp >= 50:
#             self._mp -= 50
#             injury = other.hp *3 // 4
#             injury = injury if injury >= 50 else 50
#             other.hp -= injury
#             return True
#         else:
#             self.attack(other)
#             return False

#     def magic_attack(self,others):
#         """魔法攻击

#         :param other: 被攻击的群体

#         :return: 使用魔法成功返回True否则返回False
#         """
#         if self._mp >= 20:
#             self._mp -= 20
#             for temp in others:
#                 if temp.alive:
#                     temp.hp -= randint(10,15)
#             return True
#         else:
#             return False
    
#     def resume(self):
#         """恢复能量"""
#         incr_point = randint(1,10)
#         self._mp += incr_point
#         return incr_point

#     def __str__(self):
#         return '~~~%s奥特曼~~~\n' % self._name + \
#             '生命值: %d\n' % self._hp +\
#             '魔法值：%d\n' % self._mp

# class Monster(Fighter):
#     """小怪兽"""

#     __slots__ = ('_name', '_hp')

#     def attack(self, other):
#         other.hp -= randint(10,20)

#     def __str__(self):
#         return '~~~%s小怪兽~~~\n' % self._name + \
#             '生命值: %d\n' % self._hp

# def is_any_live(monsters):
#     """判断有没有小怪兽是活着的"""
#     for monster in monsters:
#         if monster.alive > 0:
#             return True
#     return False

# def select_alive_one(monsters):
#     """选中一个活着的小怪兽"""
#     monster_len = len(monsters)
#     while True:
#         index = randrange(monster_len)
#         monster = monsters[index]
#         if monster.alive > 0:
#             return monster

# def display_info(ultraman, monsters):
#     """显示奥特曼和小怪兽的信息"""
#     print(ultraman)
#     for monster in monsters:
#         print(monster, end = '')

# def main():
#     u = Ultraman('烈豪', 1000,120)
#     m1 = Monster("蚊子", 250)
#     m2 = Monster('电子烟', 500)
#     m3 = Monster('甲子钟', 750)
#     ms = [m1, m2, m3]
#     fight_round = 1
#     while u.alive and is_any_live(ms):
#         print("=========第%02d回合========" % fight_round)
#         m = select_alive_one(ms) #选择一个小怪兽
#         skill = randint(1, 10) #通过随机数选择使用哪种技能
#         if skill <= 6: # 60%的概率使用普通攻击
#             print('%s使用普通攻击打了%s'% (u.name,m.name))
#             u.attack(m)
#             print("%s的魔法值恢复了%d点。" % (u.name, u.resume()))
#         elif skill <= 9: # 30%的概率使用魔法攻击（可能因为魔法值不足而·失败）
#             if u.magic_attack(ms):
#                 print("%s使用了魔法攻击." % u.name)
#             else:
#                 print("%s使用魔法失败." % u.name)
#         else: # 10%的概率使用究极必杀技（如果魔法值不足就使用普通攻击）
#             if u.huge_attack(m):
#                 print("%s使用了究极必杀技虐了%s" % (u.name, m.name))
#             else:    
#                 print("%s使用了普通攻击打了%s" % (u.name, m.name))
#                 print("%s的魔法值恢复了%d点." % (u.name, u.resume()))
#         if m.alive > 0 : # 选中的小怪兽没有死就回击奥特曼
#             print("%s回击了%s." % (m.name, u.name))
#             m.attack(u)
#         display_info(u, ms) # 每个回合结束后显示小怪兽和奥特曼的信息
#         fight_round += 1
#     print("\n=========战斗结束！=========\n")
#     if u.alive > 0:
#         print('%s奥特曼胜利' % u.name)
#     else:
#         print("小怪兽胜利")
    
# if __name__ == "__main__":
#     main()


import random
class Card(object):
    """一张牌"""

    def __init__(self, suite, face):
        self._suite = suite
        self._face = face

    @property
    def face(self):
        return self._face

    @property
    def suite(self):
        return self._suite

    def __str__(self):
        if self._face == 1:
            face_str = 'A'
        elif self._face == 11:
            face_str = 'J'
        elif self._face == 12:
            face_str = 'Q'
        elif self._face == 13:
            face_str = "K"
        else:
            face_str = str(self._face)
        return '%s%s' % (self._suite, face_str)

    def __repr__(self) :
        return self.__str__()

class Poker(object):
    """一副牌"""

    def __init__(self):
        self._cards = [Card(suite, face)
                        for suite in '♠♥♣♦'
                        for face in range(1,14)]
        self._current = 0
    
    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        """洗牌（随即乱序）"""
        self._current = 0
        random.shuffle(self._cards)
    @property
    def next(self):
        """发牌"""
        card = self._cards[self._current]
        self._current += 1
        return card

    @property
    def has_next(self):
        """还有没有牌"""
        return self._current < len(self._cards)
    
class Player(object):
    """玩家"""

    def __init__(self, name):
        self._name = name
        self._cards_on_hand = []

    @property
    def name(self):
        return self._name

    @property
    def cards_on_hand(self):
        return self._cards_on_hand
    
    def get(self, card):
        """摸牌"""
        self._cards_on_hand.append(card)
    
    def arrange(self, card_key):
        """玩家整理手上的牌"""
        self._cards_on_hand.sort(key=card_key)

# 排序规则-先根据花色再根据点数排序
def get_key(card):
    return (card.suite, card.face)

def main():
    p = Poker()
    p.shuffle()
    players = [Player('烈'), Player('廷'), Player('彬'), Player('鑫')]
    for _ in range(13):
        for player in players:
            player.get(p.next)
    for player in players:
        print(player.name + ':', end=' ')
        player.arrange(get_key)
        print(player.cards_on_hand)
    
if __name__ == '__main__':
    main()