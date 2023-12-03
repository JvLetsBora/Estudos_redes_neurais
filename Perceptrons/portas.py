from neural_lib import Perceptron

# Principais portas lógicas

def _nand(value):
    case = Perceptron(threshold=1,x=value, w=[-1,-1])
    return case.operacao()


def _and(value):
    case = Perceptron(threshold=-2,x=value, w=[1,1])
    return case.operacao()


def _or(value):
    case = Perceptron(threshold=-1,x=value, w=[1,1])
    return case.operacao()



def _nor(value):
    case = Perceptron(threshold=1,x=value, w=[-2,-2])
    return case.operacao()


# Casos especias

def _xor(value):
    or_1 = _nand(value)
    or_2 = _or(value)
    print(f"Para os valores {value} o resultado foi {_and([or_1,or_2])}")

def teste(function):
    teste = [[0,0],[1,0],[0,1],[1,1]]
    for i in teste:
       function(i)


teste(_xor)