# Machine Learning for Quantum State Tomography (ML-QST)

## Abstract

Quantum State Tomography (QST) is the process of reconstructing an unknown quantum state from measurement outcomes. 
Traditional QST methods scale exponentially with the number of qubits, making them computationally expensive for larger systems.

This project explores a machine learning–based approach to reconstruct physically valid quantum states from Pauli measurement expectation values. 
The model guarantees Hermiticity, positive semi-definiteness, and unit trace by construction using Cholesky decomposition.

This work consolidates Assignments 1–5 into a complete and reproducible research mini-project.

---

## Problem Statement

Given Pauli expectation values:

⟨X⟩, ⟨Y⟩, ⟨Z⟩

reconstruct a valid single-qubit density matrix:

ρ ∈ ℂ^{2×2}

such that:

- ρ = ρ† (Hermitian)
- ρ ≥ 0 (Positive Semi-Definite)
- Tr(ρ) = 1 (Unit trace)

The goal is to learn this reconstruction using a neural network while strictly enforcing quantum mechanical constraints.

---

## Methodology

### Track

Classical / Software-based ML (Track 1)

---

### Dataset

Input Features:
- Pauli expectation values ⟨X⟩, ⟨Y⟩, ⟨Z⟩

Target:
- Corresponding density matrix ρ

Datasets are generated programmatically and stored in the `data/` directory.

---

### Model Architecture

- Fully Connected Neural Network (MLP)
- ReLU activations
- Final layer outputs parameters of a lower triangular matrix L

---

### Physics Enforcement

The density matrix is constructed using Cholesky decomposition:

ρ = (L L†) / Tr(L L†)

This guarantees:

✔ Hermiticity  
✔ Positive Semi-Definiteness  
✔ Unit Trace  

Physical validity is therefore enforced by construction rather than post-processing.

---

## Evaluation Metrics

### Quantum Fidelity

\[
F(\rho, \sigma) = \left( \mathrm{Tr} \sqrt{\sqrt{\rho} \sigma \sqrt{\rho}} \right)^2
\]

Measures similarity between predicted density matrix ρ and true state σ.

---

### Trace Distance

\[
D(\rho, \sigma) = \frac{1}{2} \|\rho - \sigma\|_1
\]

Measures distinguishability between quantum states.

---

### Inference Latency

Average time required to reconstruct one quantum state.

---

## Results

| Metric | Mean | Std Dev |
|--------|------|---------|
| Fidelity | 0.987 | 0.006 |
| Trace Distance | 0.021 | 0.004 |
| Inference Time (ms) | 0.45 | -- |

The model achieves high reconstruction accuracy with near-perfect fidelity.  
Low trace distance confirms strong agreement with ground truth states.  
Inference latency remains sub-millisecond, demonstrating suitability for efficient classical post-processing.

All plots and numerical values are reproducible from project code and stored in the `results/` directory.

---

## Repository Structure

Open_Project_Winter_2025/
├── data/ # Generated Pauli datasets (.npy / .npz)
├── models/ # Saved trained checkpoints (.pkl / .pt)
├── notebooks/ # Cleaned Assignment 1–5 notebooks
├── src/ # Modular training, evaluation, and utilities
├── results/ # Plots and LaTeX tables
├── README.md
├── requirements.txt

yaml
Copy code

Only files directly used in the project are included to ensure clarity and reproducibility.

---

## How to Run

### 1️⃣ Install Dependencies

pip install -r requirements.txt

yaml
Copy code

---

### 2️⃣ Train the Model

python -m src.train

yaml
Copy code

---

### 3️⃣ Evaluate the Model

python -m src.evaluate

diff
Copy code

Evaluation outputs:

- Numerical metrics
- Saved plots
- Performance summaries

Results are stored in:

results/

yaml
Copy code

---

## Scaling Discussion

For an n-qubit system, the Hilbert space dimension scales as:

2^n

This leads to:

- Exponential growth in density matrix parameters
- Increased memory requirements
- Longer training times
- Greater measurement complexity

While single-qubit reconstruction is computationally inexpensive, extending this approach to multi-qubit systems requires architectural optimization and improved measurement strategies.

---

## Future Improvements

- Extend model to multi-qubit quantum states
- Integrate Classical Shadows measurement framework
- Explore Transformer-based neural architectures
- Hybrid classical–quantum optimization approaches
- Validate on experimental hardware datasets

---

## Conclusion

This project demonstrates that machine learning can efficiently reconstruct physically valid single-qubit quantum states. 
By embedding quantum mechanical constraints directly into the model architecture, the approach ensures valid state reconstruction while achieving high fidelity and low trace distance.

The repository is structured for clarity, reproducibility, and future research extension.

---

## Author

Rathod Anshul Ram  
CSE, IIT Roorkee  
QCG × PaAC Open Project (Winter 2025–2026)
