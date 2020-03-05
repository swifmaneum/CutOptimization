include "globals.mzn";
% ----------------------------------------
% input data 
% ----------------------------------------
int: nParts;
set of int: PARTS = 1..nParts; 

int: plateLength;
int: plateWidth;

set of int: LEN = 0..plateLength;
set of int: WID = 0..plateWidth;


array[PARTS] of LEN: length;
array[PARTS] of WID: width;

array[PARTS] of var int: dx;
array[PARTS] of var int: dy;

array[PARTS] of var LEN: x;
array[PARTS] of var WID: y;

constraint forall(part in PARTS) (dx[part] = length[part] \/ dx[part] = width[part]);
constraint forall(part in PARTS) (dy[part] = length[part] \/ dy[part] = width[part]);
constraint forall(part in PARTS) (dy[part] = length[part] <-> dx[part] = width[part]);
constraint forall(part in PARTS) (dx[part] = length[part] <-> dy[part] = width[part]);

constraint (diffn(x, y, dx, dy) /\ forall(part in PARTS) (x[part] + dx[part] <= plateLength) /\ forall(part in PARTS) (y[part] + dy[part] <= plateWidth));

%constraint (diffn(x, y, length, width) /\ forall(part in PARTS) (x[part] + length[part] <= plateLength) /\ forall(part in PARTS) (y[part] + width[part] <= plateWidth))
%\/ (diffn(x, y, width, length) /\ forall(part in PARTS) (x[part] + length[part] <= plateLength) /\ forall(part in PARTS) (y[part] + width[part] <= plateWidth));

%constraint forall(part in PARTS) (x[part] + length[part] <= plateLength);
%constraint forall(part in PARTS) (y[part] + width[part] <= plateWidth);

%solve minimize sum(x);
solve satisfy;