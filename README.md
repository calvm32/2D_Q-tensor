# Q-tensor 2D

"*Q-tensor 2D*" is an implementation of the Landau-de Gennes Q-tensor model for liquid crystals based on Andrew Hicks' "[*Q-tensor 3D*](https://github.com/andrewlhicks/q-tensor-3d)". Unlike *Q-tensor 3D*, this repository is designed to be run locally. To do so, simply download the repository and begin changing values in the files under the **user_settings** folder.

When your solution is written to a .pvd file, open it in your software (we use Paraview), and 
1. select the input as **q1**
2. navigate to filters > programmable > programmable filter
3. run the script from the "**paraview**" file in the "**scripts**" folder
4. navigate to filters > common > glyph
5. change the input array to **n** and optionally adjust other features

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
