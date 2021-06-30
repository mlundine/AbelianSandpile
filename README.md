# AbelianSandpile

![Moore Sandpile](https://github.com/mlundine/AbelianSandpile/blob/main/moore.png)

[sandpile video](https://drive.google.com/file/d/1bnxOMElHwGi6ramC5k3wvtxc-wGISrZm/view?usp=sharing)

[Nice explanation of sandpiles here](https://www.youtube.com/watch?v=1MtEUErz7Gg)

Two functions to create sandpiles (rule1 and rule2):

# rule1

rule1(low, high, maxHeight, dim)

rule1 runs the model with cells randomly assigned values.

low and high are integers, specifiying the range of values to assign randomly to cells.

maxHeight is the integer maximum height of a cell.

dim is the integer width/height of the grid.


# rule2

rule2(maxHeight, dim, pile, neighbor)

rule2 creates a pile in the center then runs the model.

maxHeight is the integer maximum height of a cell.

dim is the integer width/height of the grid.

pile is the integer height of the pile created at the center of the grid.

neighbor is the type of neighborhood to implement for each cell ('Moore' for eight neighbors, 'Von Neumann' for four neighbors')


# dependencies

Python>=3.7

numpy

matplotlib






