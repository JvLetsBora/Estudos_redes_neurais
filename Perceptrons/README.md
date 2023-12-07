# Perceptron

Para rodar o arquivo ponderada6.py basta ter instalado e configurado o python em seu computador.


## Uso

Escolha uma das portas lógicas já configuradas.

1. Matriz de portas lógicas.
    ```python
        doors ={
        "or":[0, 1, 1, 1],
        "nor":[1, 0, 0, 0],
        "xor":[0, 1, 1, 0],
        "and":[0, 0, 0, 1],
        "nand":[1, 1, 1, 0],
    }

Defina a etiqueta para a qual porta você deseja treinar.


2. Label para o treinamento.
    ```python
        labels = np.array(doors["and"])  # <------------ Porta que voce deseja treinar

Crie uma instância do perceptron e inicie o método de treinamento com a label desejada e o número de épocas. ( epochs )

3. Metódo de treinamento.
    ```python

        # Treinamento
        perceptron.train(training_inputs, labels, epochs=100)

Se tudo ocorrer conforme o esperado, o funcionamento deverá ser semelhante a [esse video](https://clipchamp.com/watch/U9H5EXHNqb8)