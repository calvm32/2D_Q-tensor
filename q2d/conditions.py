import firedrake
import tensor_conversion
import solver

# how many divisions the mesh is made of
N = 10

# mesh for solving with N divisions in the x and y directions
mesh = firedrake.UnitSquareMesh(N, N)

# vector governing boundary condition
bc_vector = firedrake.Constant(tensor_conversion.bc_conversion([0,1]))

# decides what type of boundary condition is used, default to Dirichlet
bc_type = "Dirichlet"
#bc_type = "Neumann"
#bc_type = "Robin"

# writes the solution to a file with given name (MUST BE .pvd)
file_name = "Solution_1.pvd"

solver.solve(mesh, bc_vector, bc_type, file_name)