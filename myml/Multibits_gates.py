"""from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from IPython.display import display

#Controlled-NOT (CNOT)
# State |00>
qc1 = QuantumCircuit(2)
qc1.cx(0, 1)
print("State |00> after CNOT")
display(qc1.draw("mpl"))
display(Statevector.from_instruction(qc1).draw("latex"))
# State |01>
qc2 = QuantumCircuit(2)
qc2.x(1)
qc2.cx(0, 1)
print("State |01> after CNOT")
display(qc2.draw("mpl"))
display(Statevector.from_instruction(qc2).draw("latex"))
# State |10>
qc3 = QuantumCircuit(2)
qc3.x(0)
qc3.cx(0, 1)
print("State |10> after CNOT")
display(qc3.draw("mpl"))
display(Statevector.from_instruction(qc3).draw("latex"))
# State |11>
qc4 = QuantumCircuit(2)
qc4.x(0)
qc4.x(1)
qc4.cx(0, 1)
print("State |11> after CNOT")
display(qc4.draw("mpl"))
display(Statevector.from_instruction(qc4).draw("latex"))

#SWAP
# State |00>
qc1 = QuantumCircuit(2)
qc1.swap(0, 1)
print("State |00> after SWAP")
display(qc1.draw("mpl"))
display(Statevector.from_instruction(qc1).draw("latex"))
# State |01>
qc2 = QuantumCircuit(2)
qc2.x(1)
qc2.swap(0, 1)
print("State |01> after SWAP")
display(qc2.draw("mpl"))
display(Statevector.from_instruction(qc2).draw("latex"))
# State |10>
qc3 = QuantumCircuit(2)
qc3.x(0)
qc3.swap(0, 1)
print("State |10> after SWAP")
display(qc3.draw("mpl"))
display(Statevector.from_instruction(qc3).draw("latex"))
# State |11>
qc4 = QuantumCircuit(2)
qc4.x(0)
qc4.x(1)
qc4.swap(0, 1)
print("State |11> after SWAP")
display(qc4.draw("mpl"))
display(Statevector.from_instruction(qc4).draw("latex"))

#Controlled-Z
# State |00>
qc1 = QuantumCircuit(2)
qc1.cz(0, 1)
print("State |00> after CZ")
display(qc1.draw("mpl"))
display(Statevector.from_instruction(qc1).draw("latex"))
# State |01>
qc2 = QuantumCircuit(2)
qc2.x(1)
qc2.cz(0, 1)
print("State |01> after CZ")
display(qc2.draw("mpl"))
display(Statevector.from_instruction(qc2).draw("latex"))
# State |10>
qc3 = QuantumCircuit(2)
qc3.x(0)
qc3.cz(0, 1)
print("State |10> after CZ")
display(qc3.draw("mpl"))
display(Statevector.from_instruction(qc3).draw("latex"))
# State |11>
qc4 = QuantumCircuit(2)
qc4.x(0)
qc4.x(1)
qc4.cz(0, 1)
print("State |11> after CZ")
display(qc4.draw("mpl"))
display(Statevector.from_instruction(qc4).draw("latex"))"""

def show_multigate():

    import sys
    from .code_viewer import show_code13

    module = sys.modules[__name__]

    show_code13(module)