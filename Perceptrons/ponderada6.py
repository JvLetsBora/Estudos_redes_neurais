import numpy as np

class Perceptron:
    def __init__(self, num_inputs, learning_rate=0.01):
        self.w = np.random.rand(num_inputs)
        self.bias = np.random.rand()
        self.learning_rate = learning_rate # Ligado a fusão perda

    def activation_function(self, x):
        return 1 if x+self.bias >= 0 else 0

    def predict(self, inputs):
        weighted_sum = np.dot(inputs, self.w) + self.bias
        return self.activation_function(weighted_sum)

    def train(self, training_inputs, labels, epochs):
        for _ in range(epochs):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                error = label - prediction

                # Atualiza os pesos
                self.w += self.learning_rate * error * inputs

                # Atualiza o bias
                self.bias += self.learning_rate * error
                #print((self.bias,self.w))

# Exemplo de uso

doors ={
    "or":[0, 1, 1, 1],
    "nor":[1, 0, 0, 0],
    "xor":[0, 1, 1, 0],
    "and":[0, 0, 0, 1],
    "nand":[1, 1, 1, 0],
}

if __name__ == "__main__":
    # Dados de treinamento (porta lógica AND)
    training_inputs = np.array([
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ])
    
    labels = np.array(doors["and"])  # <------------ Porta que voce deseja treinar

    # Criação do perceptron
    perceptron = Perceptron(num_inputs=2)

    # Treinamento
    perceptron.train(training_inputs, labels, epochs=100)

    print("Predictions:")
    for inputs in training_inputs:
        prediction = perceptron.predict(inputs)
        print(f"{inputs} -> {prediction}")


# 