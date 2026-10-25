"""from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
bit_list = ["00", "01", "10", "11"]

for bits in bit_list:
    print("=" * 40)
    print("Classical bits:", bits)

    # Step 1: Prepare Bell state |Phi+>
    qc = QuantumCircuit(2)

    qc.h(0)
    qc.cx(0, 1)

    psi1 = Statevector.from_instruction(qc)
    print("Step 1: Bell state")
    display(psi1.draw("latex"))

    # Step 2: Encode classical bits on qubit 0
    if bits == "00":
        pass
    elif bits == "01":
        qc.z(0)
    elif bits == "10":
        qc.x(0)
    elif bits == "11":
        qc.x(0)
        qc.z(0)

    psi2 = Statevector.from_instruction(qc)
    print("Step 2: After encoding")
    display(psi2.draw("latex"))

    # Step 3: Decode
    qc.cx(0, 1)
    qc.h(0)

    psi3 = Statevector.from_instruction(qc)
    print("Step 3: After decoding")
    display(psi3.draw("latex"))

    # Step 4: Measure
    qc.measure_all()
    print("Final circuit:")
    display(qc.draw("mpl"))

    print("Decoded bits:", bits)
    print()"""

from myml.code_viewer import show_code14


def show_superd():

    import sys
    from .code_viewer import show_code20

    module = sys.modules[__name__]

    show_code20(module)