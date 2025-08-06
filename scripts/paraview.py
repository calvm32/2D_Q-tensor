import numpy as np
import vtk

input = inputs[0]

N = input.PointData['q1'].shape[0]
Q_tensor = np.zeros((N, 2, 2))

# reconstruct Q-tensor
Q_tensor[:, 0, 0] = input.PointData['q1']/sqrt(2)
Q_tensor[:, 0, 1] = input.PointData['q2']/sqrt(2)
Q_tensor[:, 1, 0] = Q_tensor[:, 0, 1]
Q_tensor[:, 1, 1] = -Q_tensor[:, 0, 0]

# obtain eigenvalues, eigenvectors
evals, evecs = np.linalg.eigh(Q_tensor[:,:,:])

# pad the 2D vector (x, y) with a 0 z-component to make it 3D
n_vectors = np.hstack((evecs[:, 1, :], np.zeros((N, 1))))

# add the vector n and scalar s to the output
output.PointData.append(n_vectors, 'n')
output.PointData.append(evals[:, 1], 's')