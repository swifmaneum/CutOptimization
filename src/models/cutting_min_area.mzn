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

array[PARTS] of var LEN: maxx;
array[PARTS] of var LEN: maxy;

constraint forall(part in PARTS) (dx[part] = length[part] \/ dx[part] = width[part]);
constraint forall(part in PARTS) (dy[part] = length[part] \/ dy[part] = width[part]);
constraint forall(part in PARTS) (dy[part] = length[part] <-> dx[part] = width[part]);
constraint forall(part in PARTS) (dx[part] = length[part] <-> dy[part] = width[part]);

constraint (diffn(x, y, dx, dy)
    /\ forall(part in PARTS) (x[part] + dx[part] <= plateLength)
    /\ forall(part in PARTS) (y[part] + dy[part] <= plateWidth));

constraint forall(i in PARTS)(
  dx[i] >= min(length[i], width[i])
  /\ dx[i] <= max(length[i], width[i])
  /\ dy[i] >= min(length[i], width[i])
  /\ dy[i] <= max(length[i], width[i]));

constraint forall(i in PARTS)(maxx[i] = x[i] + dx[i]);
constraint forall(i in PARTS)(maxy[i] = y[i] + dy[i]);

%constraint cumulative(x, dx, dy, plateLength);
%constraint cumulative(y, dy, dx, plateWidth);

% ----------------------------------------
% Symmetry breaking
% ----------------------------------------

constraint forall(i, j in PARTS where i < j)(
    (length[i] = length[j] /\ width[i] = width[j] ) \/ (length[i] = width[j] /\ width[i] = length[j])
    <-> x[i] + dx[i] <= x[j] \/ y[i] + dy[i] <= y[j]);


solve minimize max(maxx) * max(maxy);
