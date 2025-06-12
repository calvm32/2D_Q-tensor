import firedrake
import numpy as np
import math
import constants

# chosen orthonormal basis for S_0
E1 = firedrake.as_matrix([[math.sqrt(2)/2, 0],
               [0, -math.sqrt(2)/2]])
E2 = firedrake.as_matrix([[0, math.sqrt(2)/2],
               [math.sqrt(2)/2, 0]])

# conversion from a tensor 
# to a linear combination of orthonormal bases [q1,q2]
def tensor_to_vector(Q):
    q1 = math.sqrt(2)*Q[0][0]
    q2 = math.sqrt(2)*Q[0][1]
    return [q1, q2]

# conversion from a vector [q1,q2] 
# to its Q-tensor representation
def vector_to_tensor(q):
    q1 = q[0]
    q2 = q[1]
    Q = firedrake.as_matrix(q1*E1 + q2*E2)
    return Q

# conversion from a director on the boundary 
# to a Q-tensor
def bc_to_tensor(n):
    Q = constants.s0*(np.outer(n,n)-0.5*np.identity(2))
    return Q

# conversion from a director on the boundary 
# to the linear combination representation [q1,q2]
def bc_conversion(n):
    return tensor_to_vector(bc_to_tensor(n))