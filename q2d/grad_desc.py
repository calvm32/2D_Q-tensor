from firedrake import *

while True:
    print(f"Running: \delta_t = {del_t:.3e}")
    energy_lst = []

    for step in range(step_count):
      # initialize
      Q = vector_to_tensor(q)
      Q_old = vector_to_tensor(q_old)

      # weak form including all elastic/bulk terms
      F_time = (1/del_t)*inner(Q - Q_old, P)*dx
      F_elastic = (l1*inner(grad(Q), grad(P)) +
                    l2*inner(div(Q), div(P)) +
                    l3*grad(P)[i,j,k]*grad(Q)[i,k,j]) * dx
      F_bulk = (1/eta**2)*derivative(bulk_psi(Q) * dx, q, p) # double-check that this is equal to the gradient matrix
      F_total = F_time + F_elastic + F_bulk

      # Solve
      solve(F_total == 0, q, bcs=bc2)

      # Track energy
      energy = assemble(energy_eq(q))
      energy_lst.append(energy)

      print(f"Step {step:02d} : Energy = {energy:.3e}")

      if step > 0 and energy_lst[-1] - energy_lst[-2] > epsilon:
          print(f"Energy increased: {energy_lst[-1]:.3e} > {energy_lst[-2]:.3e}")
          del_t /= 10
          q.assign(q_old)
          assert del_t >= min_dt, "del_t too small!"
          break  # retry descent

      q_old.assign(q)
      #q1 = Function(FunctionSpace(mesh, "CG", 1), name=f"q1_step_{step}")
      #q2 = Function(FunctionSpace(mesh, "CG", 1), name=f"q2_step_{step}")
      #q1.interpolate(q[0])
      #q2.interpolate(q[1])
      #vtk2.write(q1, q2)

    else:
        # All steps completed without energy increase
        dE = abs(energy_lst[-1] - energy_lst[-2])
        if dE <= tolerance:
            print("Converged")
            break

        if del_t < max_dt / 10:
            del_t *= 10
            print(f"Increasing del_t to {del_t:.1e}")
        else:
            print("Reached upper bound, BOOM.")
            break