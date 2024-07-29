import random
import json
import utils.manage as manage


def rolagem_atributo():
    values = []
    for i in range(3):
        value = random.randint(1, 4)
        values.append(value)
    result = values[0] + values[1] + values[2] * 5
    result = result + 5
    return result



def teste_rolagem():
    result = random.randint(1,100)
    return result


