"""from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from IPython.display import display

# Number of input qubits
n = 3
# Constant oracle: f(x) = 0
oracle_constant = QuantumCircuit(n + 1)
qcf = oracle_constant.to_gate()
qcf.name = "QCF"
# Balanced oracle: f(x) = x[0]
oracle_balanced = QuantumCircuit(n + 1)
oracle_balanced.cx(0, n)
qbf = oracle_balanced.to_gate()
qbf.name = "QBF"
backend = AerSimulator()
for func in ["const", "bal"]:
    print("=" * 40)
    if func == "const":
        print("CONSTANT FUNCTION")
    else:
        print("BALANCED FUNCTION")
    # n input qubits and 1 ancilla qubit
    qc = QuantumCircuit(n + 1, n)
    # Prepare ancilla in |1>
    qc.x(n)
    # Apply Hadamard to all qubits
    qc.h(range(n + 1))
    # Apply oracle
    if func == "const":
        qc.append(qcf, range(n + 1))
    else:
        qc.append(qbf, range(n + 1))
    # Final Hadamard on input qubits
    qc.h(range(n))
    # Measure input qubits
    qc.measure(range(n), range(n))

    display(qc.draw("mpl"))

    # Run simulation
    transpiled_qc = transpile(qc, backend)
    result = backend.run(
        transpiled_qc, shots=1024
    ).result()

    counts = result.get_counts(0)
    print("Final measurement:", counts)

    # Classification
    if "000" in counts and counts["000"] == 1024:
        print("Result: CONSTANT")
    elif "000" not in counts:
        print("Result: BALANCED")
    else:
        print("Result: Check measurement distribution")

    print()"""

def show_deutschj():

    import sys
    from .code_viewer import show_code16

    module = sys.modules[__name__]

    show_code16(module)