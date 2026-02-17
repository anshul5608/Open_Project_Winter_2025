# src/evaluate.py

import torch
import numpy as np
import time
import json
import os
from scipy.linalg import sqrtm

from src.data import generate_dataset
from src.model import DensityMatrixModel
from src.train import construct_density_matrix


def fidelity(rho, sigma):
    """
    Quantum fidelity between two density matrices
    """
    sqrt_rho = sqrtm(rho)
    product = sqrt_rho @ sigma @ sqrt_rho
    sqrt_product = sqrtm(product)
    return np.real(np.trace(sqrt_product)) ** 2


def trace_distance(rho, sigma):
    """
    Trace distance between two density matrices
    """
    diff = rho - sigma
    eigenvalues = np.linalg.eigvals(diff)
    return 0.5 * np.sum(np.abs(eigenvalues))


def evaluate():
    # Load test data
    X_test, Y_test = generate_dataset(1000)

    X_test = torch.tensor(X_test, dtype=torch.float32)
    

    # Load model
    model = DensityMatrixModel()
    model.load_state_dict(torch.load("outputs/models/model.pt"))
    model.eval()

    fidelities = []
    trace_distances = []
    inference_times = []

    with torch.no_grad():
        for i in range(len(X_test)):
            x = X_test[i].unsqueeze(0)

            start = time.time()
            params = model(x)
            rho_pred = construct_density_matrix(params)
            end = time.time()

            rho_pred = rho_pred.squeeze(0).numpy()

            fid = fidelity(Y_test[i], rho_pred)
            td = trace_distance(Y_test[i], rho_pred)

            fidelities.append(fid)
            trace_distances.append(td)
            inference_times.append(end - start)

    results = {
        "mean_fidelity": float(np.mean(fidelities)),
        "mean_trace_distance": float(np.mean(trace_distances)),
        "avg_inference_time_sec": float(np.mean(inference_times))
    }

    os.makedirs("outputs/metrics", exist_ok=True)
    with open("outputs/metrics/results.json", "w") as f:
        json.dump(results, f, indent=4)

    print("Evaluation Results:")
    for k, v in results.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    evaluate()
