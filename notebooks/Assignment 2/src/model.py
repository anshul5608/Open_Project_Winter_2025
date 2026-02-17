# src/model.py

import torch
import torch.nn as nn


class DensityMatrixModel(nn.Module):
    """
    Neural network that maps Pauli expectations
    [<X>, <Y>, <Z>] -> parameters of lower-triangular matrix L
    """

    def __init__(self):
        super().__init__()

        self.network = nn.Sequential(
            nn.Linear(3, 64),
            nn.ReLU(),

            nn.Linear(64, 64),
            nn.ReLU(),

            nn.Linear(64, 4)  # outputs: a, b, c, d
        )

    def forward(self, x):
        """
        x: tensor of shape (batch_size, 3)
        returns: tensor of shape (batch_size, 4)
        """
        return self.network(x)
