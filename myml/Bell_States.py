"""from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
#|00>
qc= QuantumCircuit(2)
qc.h(0)
qc.cx(0,1)
print(qc.draw())
state = Statevector(qc)
display(state.draw('latex'))
display(state.draw('qsphere'))
#|01>
qc= QuantumCircuit(2)
qc.x(1)
qc.h(0)
qc.cx(0,1)
print(qc.draw())
state = Statevector(qc)
display(state.draw('latex'))
display(state.draw('qsphere'))
#|10>
qc= QuantumCircuit(2)
qc.x(0)
qc.h(0)
qc.cx(0,1)
print(qc.draw())
state = Statevector(qc)
display(state.draw('latex'))
display(state.draw('qsphere'))
#|11>
qc= QuantumCircuit(2)
qc.x(0)
qc.x(1)
qc.h(0)
qc.cx(0,1)
print(qc.draw())
state = Statevector(qc)
display(state.draw('latex'))
display(state.draw('qsphere'))"""
def show_bellstate():
    import sys
    from .code_viewer import show_code11
    module = sys.modules[__name__]
    show_code11(module)