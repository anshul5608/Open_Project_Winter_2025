# Findings and Discussion

## Overview
This project explored a scalable surrogate model for quantum state tomography.
The implementation supports an arbitrary number of qubits and was evaluated
through scalability experiments, visualization, and ablation studies.

---

## Scalability Limits
The scalability study shows that while reconstruction fidelity remains relatively
stable as the number of qubits increases, runtime grows steadily. This behavior
is expected due to the exponential growth of the Hilbert space (dimension 2ⁿ).

As a result, the current surrogate approach is practical only for small to
moderate system sizes. Larger systems would require dimensionality reduction
or alternative measurement strategies.

---

## Ablation Study Observations
The ablation study varied the number of model layers while keeping other factors
fixed. Results indicate that increasing depth generally improves average fidelity,
but with diminishing returns beyond a certain number of layers.

This suggests that overly deep architectures may add unnecessary complexity
without proportional performance gains.

---

## Limitations
- The current model is restricted to pure-state representations.
- No physical constraints such as positivity or trace conditions are enforced.
- Scaling is limited by explicit statevector representations.

---

## Future Directions
Several promising extensions are possible:
- **Classical shadows** to reduce measurement and storage complexity
- **Mixed-state tomography** using density matrices
- **Hardware-based experiments** on real quantum devices
- Hybrid classical–quantum pipelines for scalable inference

These directions would allow the approach to move beyond toy-scale simulations
toward realistic quantum systems.
