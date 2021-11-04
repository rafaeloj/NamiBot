from random import randint

class Dice:
    def __init__(self,dice_thrown) -> None:
        self.__type        = 20           # Type of dice to roll
        self.__amount      = 1            # Amount of dice of type to roll
        self.__op_modifier = '+'          # Operator to modifier, server to know whether to add or subtract
        self.__modifier    = 0            # Value of modifier to add or subtract
        self.treat_dice(dice_thrown)
        self.__dice        = self._roll() # Get a list of dices
        self.__total       = 0            # Sum of all dices

    def __str__(self) -> str:
        return f"{self.__amount}d{self.__type}{self.modifier}: {self.__dice}"
    #To facilitate access to variables
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

    def treat_dice(self, roll:str) -> None:
        """
            roll: It's a string with pattern XdY+Z, where x is amount of dice, y is dice type and Z is modifier value
            Split the string and puts each slice in your place in the class
        """
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
        """
            Roll self.__amount dices and return a list of them
        """
        return [randint(1,self.__type) for i in range(0,self.__amount)]

    def all(self):
        """
            Used to print on the discord
        """
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
        """
            Return the sum of dices and modifier
        """
        if self.__op_modifier == '+':
            return sum(self.__dice)+self.__modifier
        else:
            return sum(self.__dice)-self.__modifier
