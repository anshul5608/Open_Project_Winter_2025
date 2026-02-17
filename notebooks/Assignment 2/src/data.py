# src/data.py

import numpy as np

# Pauli matrices
PAULI_X = np.array([[0, 1], [1, 0]], dtype=complex)
PAULI_Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
PAULI_Z = np.array([[1, 0], [0, -1]], dtype=complex)


def generate_random_density_matrix():
    """
    Generates a random 2x2 valid density matrix
    """
    A = np.random.randn(2, 2) + 1j * np.random.randn(2, 2)
    rho = A @ A.conj().T
    rho = rho / np.trace(rho)
    return rho


def pauli_expectations(rho):
    """
    Computes <X>, <Y>, <Z> for a given density matrix
    """
    x = np.real(np.trace(rho @ PAULI_X))
    y = np.real(np.trace(rho @ PAULI_Y))
    z = np.real(np.trace(rho @ PAULI_Z))
    return np.array([x, y, z])


def generate_dataset(num_samples=10000):
    """
    Generates dataset:
    inputs  -> [<X>, <Y>, <Z>]
    targets -> density matrix rho
    """
    inputs = []
    targets = []

    for _ in range(num_samples):
        rho = generate_random_density_matrix()
        meas = pauli_expectations(rho)

        inputs.append(meas)
        targets.append(rho)

    return np.array(inputs), np.array(targets)
