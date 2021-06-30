# AbelianSandpile

Two functions to create sandpiles (rule1 and rule2):

rule1(low, high, maxHeight, dim)

rule1 runs the model with cells randomly assigned values.

low and high are integers, specifiying the range of values to assign randomly to cells.

maxHeight is the integer maximum height of a cell.

dim is the integer width/height of the grid.


rule2(maxHeight, dim, pile, neighbor)

rule2 creates a pile in the center then runs the model.

maxHeight is the integer maximum height of a cell.

dim is the integer width/height of the grid.

pile is the integer height of the pile created at the center of the grid.

neighbor is the type of neighborhood to implement for each cell ('Moore' for eight neighbors, 'Von Neumann' for four neighbors')








