"""from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
# Constant-zero oracle: f(x) = 0
oracle_constant_function = QuantumCircuit(2)
qcf = oracle_constant_function.to_gate()
qcf.name = "QCF"

# Balanced oracle: f(x) = x
oracle_balanced_function = QuantumCircuit(2)
oracle_balanced_function.cx(0, 1)
qbf = oracle_balanced_function.to_gate()
qbf.name = "QBF"

backend = AerSimulator()

for func in ["const", "bal"]:
    print("=" * 40)
    print("CONSTANT FUNCTION" if func == "const"
          else "BALANCED FUNCTION")

    qc = QuantumCircuit(2, 1)

    # Prepare |0>|1>
    qc.x(1)

    # Apply Hadamard gates
    qc.h([0, 1])

    # Apply oracle
    if func == "const":
        qc.append(qcf, [0, 1])
    else:
        qc.append(qbf, [0, 1])

    # Final Hadamard and measurement (both cases)
    qc.h(0)
    qc.measure(0, 0)

    display(qc.draw("mpl"))

    # Execute
    transpiled_qc = transpile(qc, backend)
    job = backend.run(transpiled_qc, shots=1024)
    result = job.result()

    # Retrieve counts
    counts = result.get_counts(0)
    print("Final measurement:", counts)
"""

def show_deutsch():

    import sys
    from .code_viewer import show_code15

    module = sys.modules[__name__]

    show_code15(module)