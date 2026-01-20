1. Environment Setup
1.1 Prerequisites

Python ≥ 3.8

pip package manager

1.2 Clone the Repository
git clone <https://github.com/anshul5608/Open_Project_Winter_2025>
cd quantum-tomography-ml

2. Install Dependencies

It is recommended to use a virtual environment.

python -m venv venv


Activate the virtual environment:

Windows

venv\Scripts\activate


Linux / macOS

source venv/bin/activate


Install required packages:

pip install -r requirements.txt

3. Project Structure

The project is organized as follows:

quantum-tomography-ml/
├── src/            # Source code
├── outputs/        # Saved models and metrics
├── docs/           # Documentation

4. Training the Model

To train the neural network and save the model weights, run the following command from the project root directory:

python -m src.train


This will:

Generate training data

Train the neural network

Save the trained model to:

outputs/models/model.pt

5. Evaluating the Model

After training, evaluate the model using:

python -m src.evaluate


This will compute:

Mean quantum fidelity

Mean trace distance

Average inference latency

The evaluation results are saved to:

outputs/metrics/results.json

6. Expected Output

Console output will display the computed metrics. A sample output is:

mean_fidelity: ~0.99
mean_trace_distance: ~0.01
avg_inference_time_sec: < 1 ms


Exact values may vary slightly due to randomness in data generation.

7. Reproducibility Notes

Random quantum states are generated during training and evaluation.

Physical constraints on density matrices are enforced by construction using Cholesky decomposition.

All experiments can be reproduced by following the steps above.