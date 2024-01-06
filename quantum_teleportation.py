import pennylane as qml
import numpy as np

def entangle_qubits():
    # ENTANGLE THE SECOND QUBIT (WIRES=1) AND THE THIRD QUBIT
    qml.Hadamard(1)
    qml.CNOT([1,2])

def rotate_and_controls():
    # PERFORM THE BASIS ROTATION
    qml.CNOT([0,1])
    qml.Hadamard(0)
    # PERFORM THE CONTROLLED OPERATIONS
    qml.CNOT([1,2])
    qml.CZ([0,2])

dev = qml.device("default.qubit", wires=3)

# OPTIONALLY UPDATE THIS STATE PREPARATION ROUTINE
def state_preparation():
    qml.Hadamard(wires=0)
    qml.Rot(0.1, 0.2, 0.3, wires=0)

@qml.qnode(dev)
def teleportation():
    # USE YOUR QUANTUM FUNCTIONS TO IMPLEMENT QUANTUM TELEPORTATION
    state_preparation()
    entangle_qubits()
    rotate_and_controls()
    
    #print(qml.measure(0))
    #print(qml.measure(1))
    # RETURN THE STATE
    return qml.state()

def extract_qubit_state(input_state):
    """Extract the state of the third qubit from the combined state after teleportation.
    
    Args:
        input_state (array[complex]): A 3-qubit state of the form 
            (1/2)(|00> + |01> + |10> + |11>) (a|0> + b|1>)
            obtained from the teleportation protocol.
            
    Returns:
        array[complex]: The state vector np.array([a, b]) of the third qubit.
    """
    # DETERMINE THE STATE OF THE THIRD QUBIT
    #print(input_state)
    return np.array([2*input_state[0],2*input_state[1]])

full_state = teleportation()
print(full_state)
print(extract_qubit_state(full_state))


