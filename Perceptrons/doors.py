from neural_lib import Perceptron, Sigmoid_neuron

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
    return _and([or_1,or_2])

# Testador de portas lógicas:

def teste(function):
    teste = [[0,0],[1,0],[0,1],[1,1]]
    for i in teste:
       print(f"{i} -> {function(i)}")


portas ={
    "or":_or,
    "nor":_nor,
    "xor":_xor,
    "and":_and,
    "nand":_nand,
}

def main():
    porta = input("Digite alguma das seguintes portas para testar nor, and, nand, xor, or: ")
    print(porta.upper())
    teste(portas[porta])



if __name__ == "__main__":
    main()