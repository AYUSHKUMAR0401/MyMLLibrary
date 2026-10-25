"""from qiskit import QuantumCircuit 
from qiskit.quantum_info import Statevector 
from qiskit_aer import AerSimulator

# 1. Initialize a 3-qubit, 3-classical-bit circuit
qc = QuantumCircuit(3, 3)

# Display initial state |000>
state = Statevector(qc)
display(state.draw("latex"))

# 2. Create an entangled Bell pair between qubit 1 and qubit 2
qc.h(1)
qc.cx(1, 2)

# Display state after entanglement
state = Statevector(qc)
display(state.draw("latex"))

# 3. Perform Bell-state measurement operations on qubits 0 and 1
qc.cx(0, 1)
qc.h(0)

# Display state before measurement
state = Statevector(qc)
display(state.draw("latex"))

# 4. Measure qubits 0 and 1 into classical bits 1 and 0 respectively
qc.measure(0, 1)
qc.measure(1, 0)

# 5. Apply conditional feedback corrections to qubit 2 based on classical bits
with qc.if_test((qc.clbits[0], 1)):
    qc.x(2)
with qc.if_test((qc.clbits[1], 1)):
    qc.z(2)

# 6. Measure the final teleported state on qubit 2
qc.measure(2, 2)

# 7. Visualize the completed circuit diagram
display(qc.draw('mpl'))

# 8. Run the simulation and print execution counts
simulator = AerSimulator()
result = simulator.run(qc, shots=1024).result()
counts = result.get_counts()
print(counts)"""

def show_teleport():

    import sys
    from .code_viewer import show_code21

    module = sys.modules[__name__]

    show_code21(module)