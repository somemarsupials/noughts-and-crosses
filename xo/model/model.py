from __future__ import annotations
from tensorflow import keras, nn

from xo.state import Board


class Model:
    def __init__(self, network):
        self._model = network

    @staticmethod
    def create(layer_size=20, num_layers=2, activation=nn.relu):
        inputs = keras.Input(shape=(Board.SIZE * 2 + 2,), name="board")
        layer = inputs

        for index in range(num_layers):
            layer = keras.layers.Dense(
                layer_size,
                activation=activation,
                name="layer-{}".format(index),
            )(layer)

        outputs = keras.layers.Dense(1, name="score")(layer)
        return Model(keras.Model(inputs=inputs, outputs=outputs))

    def predict(self, input_values):
        return self._model(input_values)

    def train(self, board):
        pass
