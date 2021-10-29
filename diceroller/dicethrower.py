from diceroller.dice import Dice
#from dice import Dice
import re
#([0-9]*d[0-9]+)([+-][0-9]+){0,1} - Regex para identificar os dados rolados
class DiceThrower:
    def __init__(self):
        pass
    def treat_string(self,string:str):
        dice_pattern = "([0-9]*d[0-9]+)([+-][0-9]+){0,1}([+-])*"
        op_pattern = "[+-]"
        self.__splitted_dices = re.findall(dice_pattern, string.replace(" ",""))
    @property
    def dices(self):
        return [f'{str(d.amount)}{str(d.type)}{d.modifier}' for d in self.__dices]
    def roll(self):
        self.__operators = []
        self.__dices=[]
        for dice, modifier,op in self.__splitted_dices:
            if op != "":
                self.__operators.append(op)
            self.__dices.append(Dice(dice+modifier))
        self.__total = self.__dices[0].result()
        for op in range(0,len(self.__operators)):
            if self.__operators[op] == "+":
                self.__total += self.__dices[op+1].result()
            else:
                self.__total -= self.__dices[op+1].result()
        return self.__total
    def result(self):
        result_string = "***Result:*** "
        size = len(self.__dices)-1
        for i, dice in enumerate(self.__dices):
            result_string += dice.all()
            if i < size:
                result_string+=", "
        result_string += "\n"
        result_string += "***Total:*** "+str(self.__total)
        return result_string

def main():
    thrower = DiceThrower()
    thrower.treat_string("d20+2+1d4")
    thrower.roll()
    thrower.result()

if __name__=="__main__":
    main()
