Quantum State Tomography using Machine Learning
Overview

This project implements a machine learning–based approach for Quantum State Tomography (QST).
The goal is to reconstruct a physically valid single-qubit density matrix from measurement data using a neural network while strictly enforcing quantum mechanical constraints.

This work is completed as part of Assignment 2 for the QCG × PaAC Open Project (Winter 2025–2026).

Objective

Reconstruct a single-qubit density matrix from Pauli measurement expectations

Ensure the reconstructed state is:

Hermitian

Positive Semi-Definite

Unit Trace

Report fidelity, trace distance, and inference latency

Approach

Track Chosen: Track 1 (Classical / Software-based ML)

Input: ⟨X⟩, ⟨Y⟩, ⟨Z⟩ expectation values

Model: Fully connected neural network (MLP)

Physics Enforcement: Cholesky decomposition	​

This guarantees physical validity by construction.

Repository Structure
quantum-tomography-ml/
├── src/            # Core source code
├── outputs/        # Trained models and metrics
├── docs/           # Documentation
├── README.md
├── AI_USAGE.md
├── requirements.txt

How to Run
Train the Model
python -m src.train

Evaluate the Model
python -m src.evaluate

Reported Metrics

Mean Quantum Fidelity

Mean Trace Distance

Average Inference Latency

Results are saved in:

outputs/metrics/results.json

Notes

The project focuses on single-qubit quantum states.

The implementation is modular and easily extendable to higher-dimensional systems.

Author


Rathod Anshul Ram
