"""from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from IPython.display import display
# State |000>
qc1 = QuantumCircuit(3)
qc1.ccx(0, 1, 2)
print("State |000> after CCNOT")
display(qc1.draw("mpl"))
display(Statevector.from_instruction(qc1).draw("latex"))

# State |001>
qc2 = QuantumCircuit(3)
qc2.x(2)
qc2.ccx(0, 1, 2)
print("State |001> after CCNOT")
display(qc2.draw("mpl"))
display(Statevector.from_instruction(qc2).draw("latex"))

# State |010>
qc3 = QuantumCircuit(3)
qc3.x(1)
qc3.ccx(0, 1, 2)
print("State |010> after CCNOT")
display(qc3.draw("mpl"))
display(Statevector.from_instruction(qc3).draw("latex"))

# State |011>
qc4 = QuantumCircuit(3)
qc4.x(1)
qc4.x(2)
qc4.ccx(0, 1, 2)
print("State |011> after CCNOT")
display(qc4.draw("mpl"))
display(Statevector.from_instruction(qc4).draw("latex"))

# State |100>
qc5 = QuantumCircuit(3)
qc5.x(0)
qc5.ccx(0, 1, 2)
print("State |100> after CCNOT")
display(qc5.draw("mpl"))
display(Statevector.from_instruction(qc5).draw("latex"))

# State |101>
qc6 = QuantumCircuit(3)
qc6.x(0)
qc6.x(2)
qc6.ccx(0, 1, 2)
print("State |101> after CCNOT")
display(qc6.draw("mpl"))
display(Statevector.from_instruction(qc6).draw("latex"))

# State |110>
qc7 = QuantumCircuit(3)
qc7.x(0)
qc7.x(1)
qc7.ccx(0, 1, 2)
print("State |110> after CCNOT")
display(qc7.draw("mpl"))
display(Statevector.from_instruction(qc7).draw("latex"))

# State |111>
qc8 = QuantumCircuit(3)
qc8.x(0)
qc8.x(1)
qc8.x(2)
qc8.ccx(0, 1, 2)
print("State |111> after CCNOT")
display(qc8.draw("mpl"))
display(Statevector.from_instruction(qc8).draw("latex"))"""

def show_ccnot():

    import sys
    from .code_viewer import show_code14

    module = sys.modules[__name__]

    show_code14(module)