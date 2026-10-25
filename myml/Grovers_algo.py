"""from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import math
from IPython.display import display
# Oracle
def oracle(qc):
    qc.cz(0, 2)


# Diffusion operator
def diffusion(qc):
    qc.h([0, 1, 2])
    qc.x([0, 1, 2])

    qc.h(2)
    qc.ccx(0, 1, 2)
    qc.h(2)

    qc.x([0, 1, 2])
    qc.h([0, 1, 2])


# Grover's Algorithm
n = 3
target = "101"

# Create circuit
qc = QuantumCircuit(n, n)

# Step 1: Create superposition
qc.h([0, 1, 2])

# Number of Grover iterations
N = 2 ** n
iterations = round(math.pi / 4 * math.sqrt(N))

print("Number of iterations:", iterations)

# Step 2: Grover iterations
for i in range(iterations):
    oracle(qc)
    diffusion(qc)

# Step 3: Measure
qc.measure([0, 1, 2], [0, 1, 2])

# Display circuit
print("\nGrover Circuit:")
display(qc.draw("mpl"))

# Run circuit
backend = AerSimulator()
result = backend.run(qc, shots=1024).result()

counts = result.get_counts()

print("\nMeasurement Results:")
print(counts)"""


def show_grover():

    import sys
    from .code_viewer import show_code17

    module = sys.modules[__name__]

    show_code17(module)
