import firedrake
import tensor_conversion

# mesh for solving with N divisions in the x and y directions
N = 10 # number of divisions
mesh = firedrake.UnitSquareMesh(N, N)

# BC conditions
bc_vector = firedrake.Constant(tensor_conversion.bc_conversion([0,1]))
bc_type = "Dirichlet"

# Solver settings
grad_desc = True
tol_u = 2.0
tol_l = 0.2
tol =  1.0e-8
num =  20
step = 1

solver.solve(mesh, bc_vector, bc_type, file_name)