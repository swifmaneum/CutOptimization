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

array[PARTS] of var LEN: dx;
array[PARTS] of var LEN: dy;

array[PARTS] of var LEN: x;
array[PARTS] of var WID: y;

constraint forall(part in PARTS) (dx[part] = length[part] \/ dx[part] = width[part]);
constraint forall(part in PARTS) (dy[part] = length[part] \/ dy[part] = width[part]);
constraint forall(part in PARTS) (dy[part] = length[part] <-> dx[part] = width[part]);
constraint forall(part in PARTS) (dx[part] = length[part] <-> dy[part] = width[part]);

constraint (diffn(x, y, dx, dy)
    /\ forall(part in PARTS) (x[part] + dx[part] <= plateLength)
    /\ forall(part in PARTS) (y[part] + dy[part] <= plateWidth));

% ----------------------------------------
% Symmetry breaking
% ----------------------------------------

%constraint forall(i, j in PARTS where i < j)(
%    (length[i] = length[j] /\ width[i] = width[j] ) \/ (length[i] = width[j] /\ width[i] = length[j])
%    <-> x[i] < x[j] \/ y[i] < y[j]);

constraint x[nParts] = 0;
constraint y[nParts] = 0;
constraint dx[nParts] = 100;
constraint x[nParts -1] = 100;
constraint y[nParts -1] = 0;
constraint dx[nParts -1] = 100;
constraint x[nParts -2] = 200;
constraint y[nParts -2] = 0;
constraint dx[nParts -2] = 100;
constraint x[nParts -3] = 300;
constraint y[nParts -3] = 0;
constraint dx[nParts -3] = 100;

%solve minimize sum(x) + sum(y) div 2;

%solve satisfy;