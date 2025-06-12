import firedrake
import math

# constants to solve with
l1 = firedrake.Constant(1)
l2 = firedrake.Constant(0)
l3 = firedrake.Constant(0)

a0 = firedrake.Constant(1)
a2 = firedrake.Constant(7.502104)
a3 = firedrake.Constant(60.975813)
a4 = firedrake.Constant(66.519069)

eta = firedrake.Constant(1)

s0 = firedrake.Constant((a3 + math.sqrt(a3*a3 + 24*a2*a4))/(4*a4 ))