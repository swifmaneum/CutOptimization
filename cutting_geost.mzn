include "geost.mzn";
include "lex_greatereq.mzn";

int: k = 2;
int: nObjects;
int: nRectangles;
int: nShapes;

int: sheetLength;
int: sheetWidth;

set of int: DIMENSIONS = 1..k;
set of int: OBJECTS    = 1..nObjects;
set of int: RECTANGLES = 1..nRectangles;
set of int: SHAPES     = 1..nShapes;

array[DIMENSIONS] of int:             l  = [0, 0];
array[DIMENSIONS] of var int:         u;
array[RECTANGLES,DIMENSIONS] of int:  rect_size;
array[RECTANGLES,DIMENSIONS] of int:  rect_offset;
array[SHAPES] of set of RECTANGLES:   shape;
array[OBJECTS,DIMENSIONS] of var int: x;
array[OBJECTS] of var SHAPES:         kind;

array[OBJECTS] of set of SHAPES: valid_shapes;

constraint u[1] <= sheetLength;
constraint u[2] <= sheetWidth;

constraint forall (obj in OBJECTS) (
    kind[obj] in valid_shapes[obj]
);

% There has to be an object at (0,0)
%constraint exists (obj in OBJECTS) (
%    x[obj, 1] = 0 /\ x[obj, 2] = 0
%);

% All objects have to be connected or placed at a 0 coordinate
%constraint forall (f in OBJECTS)(exists (g,h in OBJECTS where f != g /\ f != h) (
%    (x[f,1] = 0 \/ x[f, 1]= x[g,1] + rect_size[kind[g], 1] ) /\ (x[f,2] = 0 \/ x[f,2] = x[h,2] + rect_size[kind[h], 2])
%));

%constraint exists (g,h in OBJECTS where g != h) (
%    x[g,1] = x[h,1] + rect_size[kind[g], 1] /\ x[g,2] = x[h,2] + rect_size[kind[g], 2]
%);

constraint
    geost_bb(
        k,              % the number of dimensions
        rect_size,      % the size of each box in k dimensions
        rect_offset,    % the offset of each box from the base position in k dimensions
        shape,          % the set of rectangles defining the i-th shape
        x,              % the base position of each object.
                        % (var) x[i,j] is the position of object i in dimension j
        kind,           % (var) the shape used by each object
        l,              % array of lower bounds
        u               % array of upper bounds
    );

% Symmetry breaking
constraint forall(i, j in OBJECTS where i < j)(
    valid_shapes[i] = valid_shapes[j]
        <-> x[i, 1] + rect_size[kind[i], 1] <= x[j, 1]
        \/ x[i, 2] + rect_size[kind[i], 2] <= x[j, 2]);

constraint lex_greatereq(row(x, 1) , reverse(row(x, 1)));
constraint lex_greatereq(row(x, 2) , reverse(row(x, 2)));

var int: obj = product(u);
solve minimize obj;