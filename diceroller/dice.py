from random import randint

class Dice:
    def __init__(self,dice_thrown) -> None:
        self.__type        = 20
        self.__amount      = 1
        self.__op_modifier = '+'
        self.__modifier    = 0
        self.treat_dice(dice_thrown)
        self.__dice        = self._roll()
        self.__total       = 0
    def __str__(self) -> str:
        return f"{self.__amount}d{self.__type}{self.modifier}: {self.__dice}"

    def treat_dice(self, roll:str) -> None:
        dice_split = roll.split('d')
        if '-' in dice_split[1]:
            minus              = dice_split[1].split('-')
            dice_split[1]      = minus[0]
            self.__modifier    = int(minus[1])
            self.__op_modifier = '-'
        elif '+' in dice_split[1]:
            plus            = dice_split[1].split('+')
            dice_split[1]   = plus[0]
            self.__op_modifier = '+'
            self.__modifier = int(plus[1])

        if dice_split[0] != "":
            self.__amount = int(dice_split[0])
            self.__type   = int(dice_split[1])
        else:
            self.__type   = int(dice_split[1])
            self.__amount = 1

    def _roll(self) -> list:
        return [randint(1,self.__type) for i in range(0,self.__amount)]

    def all(self):
        output_string = f"{self.__amount}d{self.__type}{self.modifier}:"
        output_string += '('
        size = len(self.__dice)-1
        for d in range(0,size+1):
            if 1 == self.__dice[d] or self.__dice[d] == self.__type:
                output_string += "***"+str(self.__dice[d])+"***"
            else:
                output_string += str(self.__dice[d])
            if d < size:
                output_string += ", "
        output_string += ')'
        return output_string
    def result(self) -> int:
        if self.__op_modifier == '+':
            return sum(self.__dice)+self.__modifier
        else:
            return sum(self.__dice)-self.__modifier

    @property
    def amount(self) -> int:
        return self.__amount
    @property
    def type(self) -> str:
        return 'd'+str(self.__type)
    @property
    def modifier(self) -> str:
        if self.__modifier == 0:
            return ""
        return self.__op_modifier+str(self.__modifier)

    @property
    def dice(self) -> list:
        return self.__dice
