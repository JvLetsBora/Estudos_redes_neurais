# Percptron basico 

class Perceptron():
    def __init__(self, x:list, w:list, threshold) -> None:
        self.x = x
        self.w = w # Sempe w <= x
        self.threshold = threshold

    def operacao(self):
        soma = 0
        for i in range(len(self.x)):
            soma += self.x[i]*self.w[i]
        return 1 if soma + self.threshold >= 0 else 0
        

class Sigmoid_neuron():
    def __init__(self, x:list, w:list, bias) -> None:
        self.x = x
        self.w = w # Sempe w <= x
        self.bias = bias

    def sigma(value,mean): 
        return value/mean

    def sigma_teste(self,z):
        print(f'z: {z}')
        e = 2.71828  # número de Euler
        return 1 / (1 + (e ** (-z)))
    
    def operacao(self):
        soma = 0
        for i in range(len(self.x)):
            soma += self.x[i]*self.w[i]
        return self.sigma_teste(soma+self.bias)
    