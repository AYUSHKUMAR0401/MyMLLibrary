"""from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from IPython.display import display

def runCircuit(n,s,shots=1024):
    ofunc = QuantumCircuit(n+1)
    for i in range(len(s)):
        if s[i] == '1':
            ofunc.cx(i,n)
        ofunc = ofunc.to_gate()
        ofunc.name = "Oracle"
        qc = QuantumCircuit(n+1,n)
        bits = list(range(n+1))
        qc.x(n)
        qc.h(bits)
        qc.append(ofunc, bits)
        qc.h(bits[:-1])
        qc.measure(bits[:-1], bits[:-1])
        print("="*40)
        print("Bernstein Vazirani Circuit:")
        print("="*40)
        display(qc.draw("mpl"))
        backend = AerSimulator()
        transpiled_qc = transpile(qc, backend)
        result = backend.run(transpiled_qc, shots=shots).result()
        counts = result.get_counts()
        print(f"Final measurement after {shots} shots: {counts}\n")
        return counts
n=3
s="101"
result = list(runCircuit(n,s).keys())
print(f"\nThus, secret key S:{result[0]}.")"""
def show_bv():

    import sys
    from .code_viewer import show_code12

    module = sys.modules[__name__]

    show_code12(module)
