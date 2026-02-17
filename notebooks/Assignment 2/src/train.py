# src/train.py

import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import os

from src.data import generate_dataset
from src.model import DensityMatrixModel


def construct_density_matrix(params):
    """
    params: tensor of shape (batch_size, 4)
    returns: density matrix rho of shape (batch_size, 2, 2)
    """
    a, b, c, d = params[:, 0], params[:, 1], params[:, 2], params[:, 3]

    L = torch.zeros((params.shape[0], 2, 2), dtype=torch.complex64)
    L[:, 0, 0] = a
    L[:, 1, 0] = b + 1j * c
    L[:, 1, 1] = d

    rho = L @ torch.conj(L.transpose(1, 2))
    trace = torch.real(torch.diagonal(rho, dim1=1, dim2=2).sum(dim=1))
    rho = rho / trace.view(-1, 1, 1)

    return rho


def train():
    # Hyperparameters
    num_samples = 10000
    batch_size = 128
    epochs = 30
    lr = 1e-3

    # Data
    X, Y = generate_dataset(num_samples)
    X = torch.tensor(X, dtype=torch.float32)
    Y = torch.tensor(Y, dtype=torch.complex64)

    # Model
    model = DensityMatrixModel()
    optimizer = optim.Adam(model.parameters(), lr=lr)
    criterion = nn.MSELoss()

    # Training loop
    for epoch in range(epochs):
        perm = torch.randperm(num_samples)
        epoch_loss = 0.0

        for i in range(0, num_samples, batch_size):
            idx = perm[i:i + batch_size]

            x_batch = X[idx]
            y_true = Y[idx]

            optimizer.zero_grad()

            params = model(x_batch)
            rho_pred = construct_density_matrix(params)

            loss = criterion(
                torch.view_as_real(rho_pred),
                torch.view_as_real(y_true)
            )

            loss.backward()
            optimizer.step()

            epoch_loss += loss.item()

        print(f"Epoch {epoch + 1}/{epochs} | Loss: {epoch_loss:.6f}")

    # Save model
    os.makedirs("outputs/models", exist_ok=True)
    torch.save(model.state_dict(), "outputs/models/model.pt")
    print("Model saved to outputs/models/model.pt")


if __name__ == "__main__":
    train()
