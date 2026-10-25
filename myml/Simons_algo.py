"""from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from IPython.display import display

def runcircuit():
    n = 2
    s = "11"
    ofunc = QuantumCircuit(2*n)
    for i in range(n):
        ofunc.cx(i,2*n-1)
    ofunc = ofunc.to_gate()
    ofunc.name = "Oracle"
    qc = QuantumCircuit(2*n,n)
    bits = list(range(2*n))
    qc.h(bits[:])
    qc.append(ofunc, bits)
    qc.measure(bits[:n], bits[:n])
    print("="*40)
    print("Simon's Circuit:")
    print("="*40)
    display(qc.draw("mpl"))
    backend = AerSimulator()
    tqc = transpile(qc, backend)
    result = backend.run(tqc, shots=1024).result()
    counts = result.get_counts()
    mbits = list(counts.keys())
    linear_equations = [bits[::-1] for bit in mbits]
    return linear_equations
def findS(equations):
    solutions = []
    n = len(equations[0])
    for numbers in range(0,2**n):
        s = format(numbers, f'0{n}b')
        valid = True
        for eq in equations:
            dot = 0
            for i in range(n):
                dot ^= int(eq[i]) * int(s[i])
            if dot != 0:
                valid = False
                break
        if valid:
            solutions.append(s)
    return solutions
equations = runcircuit()
sol = findS(equations)
for s in sol:
    if s != '00':
        print(f"Secret Message S after solving {len(equations)} equations: {s}")"""

def show_simon():

    import sys
    from .code_viewer import show_code19

    module = sys.modules[__name__]

    show_code19(module)
