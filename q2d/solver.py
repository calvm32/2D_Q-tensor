# imports
from firedrake import *
import weak_forms
import tensor_conversion

def solve(mesh, bc_vector, bc_type) :
    V = VectorFunctionSpace(mesh, "CG", 1, 2)

    # trial and test function setup
    q = Function(V, name="soln")
    p = TestFunction(V)

    Q = tensor_conversion.vector_to_tensor(q)
    P = tensor_conversion.vector_to_tensor(p)

    # calculates the entire weak form governing the energy of the system
    F = (weak_forms.elastic_energy(Q,P)+weak_forms.bulk_energy(Q,P)) * dx

    # calculates the boundary condition
    if bc_type == "Dirichlet":
        bc = firedrake.DirichletBC(V, bc_vector, "on_boundary")
    elif bc_type == "Neumann":
        bc = Constant(0)
    elif bc_type == "Robin":
        bc = Constant(0)

    solve(F == 0, q, bcs = bc)

    # directly write q1,q2 into the file
    q1 = Function(FunctionSpace(mesh, "CG", 1), name="q1")
    q2 = Function(FunctionSpace(mesh, "CG", 1), name="q2")

    q1.interpolate(q[0])
    q2.interpolate(q[1])

    VTKFile("solution_1.pvd").write(q1, q2)

