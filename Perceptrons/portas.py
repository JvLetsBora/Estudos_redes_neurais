from neural_lib import Perceptron

def _nand(value):
    case = Perceptron(threshold=1,x=value, w=[-1,-1])
    return case.operacao()


testes = [[0,0],[1,0],[1,1],[0,1]]

# print("NAND")
# for i in testes:
#     _nand(i)

def _and(value):
    case = Perceptron(threshold=-2,x=value, w=[1,1])
    return case.operacao()


# print("AND")
# for i in testes:
#    _and(i)


def _or(value):
    case = Perceptron(threshold=-1,x=value, w=[1,1])
    return case.operacao()


# print("OR")
# for i in testes:
#    _or(i)


def _nor(value):
    case = Perceptron(threshold=1,x=value, w=[-2,-2])
    return case.operacao()


# print("NOR")
# for i in testes:
#    _nor(i)


def _nor(value):
    case = Perceptron(threshold=1,x=value, w=[-2,-2])
    return case.operacao()


print("NOR")
for i in testes:
   _nor(i)