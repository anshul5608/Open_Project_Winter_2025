1. Problem Overview
Quantum State Tomography (QST) aims to reconstruct an unknown quantum state represented by a density matrix ρ using measurement data. For a single qubit, ρ is a 2×2 complex matrix that must satisfy the following physical constraints:

Hermitian: ρ = ρ†

Positive Semi-Definite

Unit Trace: Tr(ρ) = 1

The goal of this project is to use a machine learning model to reconstruct a physically valid density matrix from experimentally accessible measurements.


2. Input Representation
The input to the model consists of expectation values of Pauli operators:

⟨X⟩

⟨Y⟩

⟨Z⟩

These values fully characterize a single-qubit quantum state and are computed as:

⟨P⟩ = Tr(ρP), where P ∈ {X, Y, Z}

Thus, each input sample is a real-valued vector of dimension 3.


3. Model Architecture
A fully connected neural network (Multilayer Perceptron) is used due to the low-dimensional and non-spatial nature of the input.

Architecture:

Input layer: 3 neurons

Two hidden layers with ReLU activation

Output layer: 4 neurons

The model outputs four real values [a, b, c, d], which parameterize a lower-triangular matrix.


4. Enforcing Physical Constraints using Cholesky Decomposition
Directly predicting the density matrix may violate physical constraints. To prevent this, the model predicts a lower-triangular matrix L:

L = [[a, 0],
[b + ic, d]]

The density matrix is reconstructed as:

ρ = (L L†) / Tr(L L†)

This construction guarantees that the resulting density matrix is:

Hermitian

Positive Semi-Definite

Unit Trace

Thus, physical validity is enforced by design rather than post-processing.


5. Training Objective
The model is trained by minimizing the Mean Squared Error (MSE) between the predicted density matrix and the true density matrix:

Loss = ||ρ_pred − ρ_true||²

Complex matrices are handled by converting them into real-valued representations during loss computation.


6. Summary
This approach combines domain knowledge from quantum mechanics with machine learning by embedding physical constraints directly into the model architecture. As a result, the reconstructed quantum states are both accurate and physically meaningful.