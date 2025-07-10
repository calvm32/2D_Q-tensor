import firedrake
import user_settings.constants as constants
from ufl import indices

# returns the weak form of the elastic energy equation before integration
def elastic_energy(Q,P):
    i, j, k = indices(3)
    l1_term = constants.l1*firedrake.inner(firedrake.grad(Q), firedrake.grad(P))
    l2_term = constants.l2*firedrake.inner(firedrake.div(Q), firedrake.div(P))
    l3_term = constants.l3*firedrake.grad(P)[i,j,k] * firedrake.grad(Q)[i,k,j]
    return (l1_term + l2_term + l3_term)

# returns the weak form of the bulk energy equation before integration
def bulk_energy(Q,P):
    a2_term = (-1)*constants.a2*firedrake.tr(Q*P)
    a3_term = (-1)*constants.a3*firedrake.tr((Q*Q)*P) # note that this 3d term computes to 0, so it is not necessary to consider
    a4_term = constants.a4*firedrake.tr(Q*Q)*firedrake.tr(Q*P)
    return (1/(constants.eta**2))*(a2_term+a3_term+a4_term)