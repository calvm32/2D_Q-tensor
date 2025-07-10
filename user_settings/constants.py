import firedrake
import math

# bulk potential constants
a2 = firedrake.Constant(7.502104)
a3 = firedrake.Constant(60.975813)
a4 = firedrake.Constant(66.519069)

# elastic energy constants
l1 = firedrake.Constant(1)
l2 = firedrake.Constant(0)
l3 = firedrake.Constant(0)

# anchoring constants
w0 = firedrake.Constant(10.0)
w1 = firedrake.Constant(0)
w2 = firedrake.Constant(0)

# bulk potential scaling factor
ep = firedrake.Constant(1)

# twist term
q0 = 5

# theoretical energy value
# s0 = firedrake.Constant((a3 + math.sqrt(a3*a3 + 24*a2*a4))/(4*a4 ))