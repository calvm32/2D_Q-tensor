# Q-tensor 2D

"*Q-tensor 2D*" is an implementation of the Landau-de Gennes Q-tensor model for liquid crystals based on Andrew Hicks' "[*Q-tensor 3D*](https://github.com/andrewlhicks/q-tensor-3d)". Unlike *Q-tensor 3D*, this repository is designed to be run locally. To do so, simply download the repository and begin changing values in the files under the **user_settings** folder.

## Understanding the "**settings**" file

This file allows the user to control various settings relating to the mesh, boundary condition, and solving method.

| Name in settings file | Meaning of setting |
| ---             | --- |
| PDE settings    | --- |
| mesh            | Region on which the PDE is solved |
| bc_vector       | Vector governing boundary condition |
| bc_type         | What type of boundary condition is used |
| Solver settings | --- |
| grad_desc       | If true, will use gradient descent to solve PDE |
| tol_u           | Upper tolerance for dynamic solver |
| tol_l           | Lower tolerance for dynamic solver |
| tol             | Tolerance for finding a solution |
| num             | Number of time steps |
| step            | The step size |

### PDE settings: choosing a mesh

You may use any 2d mesh [built into Firedrake](https://www.firedrakeproject.org/_modules/firedrake/utility_meshes.html).

### Solver settings: gradient descent

This is a time-stepping method for finding a solution at equilibrium, as opposed to the first solution.

## Understanding the "**init_cond**" file

This file allows the user to input custom expressions for the initial condition _q-vector_ (`initcond`), the weak boundary _director_ (`w_bdy_nu`), the strong boundary _q-vector_ (`sbdy`), the manufactured _q-vector_ (`manu_q`), the forcing right hand side _q-vector_ on the bulk (`forcing_f`), and the forcing right hand side _q-vector_ on the boundary (`forcing_g`).

### Creating user expressions using UFL objects

Using UFL objects is now the preferred method to specify user expressions.
The two major classes of UFL objects that the user can specify are _q-vectors_ (using the `!qvector` flag) and _directors_ (using the `!director` flag).
Vector objects (3-dimensional) are only used for the weak boundary director (`w_bdy_nu`), while q-vector objects (5-dimensional) are used for everything else.

Besides the hundreds of already available objects in the standard UFL library, there are several additional functions available to the user, most of which can be nested inside of each other:

#### `as_vector`

Outputs a vector of any dimension; thus can be used to specify a q-vector or a director object.

__Example:__
```
initcond: !qvector as_vector([x0**2, x0+x1, x1+x2, 1, 0])
```
Another example:
```
w_bdy_nu: !director as_vector([0,0,1])
```

#### `from_director`

Outputs a q-vector from a given director.

__Example:__
```
initcond: !qvector from_director([cos(5*x2),sin(5*x2),0])
```

## Understanding the "**constants**" file

This file allows the user to control various constants relating to the PDE, which may be determined by specific lab experiments or chosen by the user.

| Name in constants file | Name in Hicks' dissertation | Meaning of constant |
| --- | --- | --- |
| A   | a2  | In the bulk potential |
| B   | a3  | In the bulk potential |
| C   | a4  | In the bulk potential |
| L1  | l1  | In the elastic energy |
| L2  | l2  | In the elastic energy |
| L3  | l3  | In the elastic energy |
| w0  | w0  | Corresponds to homeotropic anchoring |
| w1  | w1  | Corresponds to planar degenerate anchoring |
| w2  | w2  | Corresponds to planar degenerate anchoring |
| ep  | eta | Scales the bulk potential |
| q0  | tau0 | Twist term in the elastic energy |
