include "globals.mzn";
% ----------------------------------------
% input data
% ----------------------------------------
int: nParts;
set of int: PARTS = 1..nParts;

set of int: PARTSx = 1..nParts + 2;

int: plateLength;
int: plateWidth;

set of int: LEN = 0..plateLength;
set of int: WID = 0..plateWidth;

array[PARTS] of LEN: length;
array[PARTS] of WID: width;

array[PARTSx] of var LEN: dx;
array[PARTSx] of var LEN: dy;

array[PARTSx] of var LEN: x;
array[PARTSx] of var WID: y;

constraint forall(part in PARTS) (dx[part] = length[part] \/ dx[part] = width[part]);
constraint forall(part in PARTS) (dy[part] = length[part] \/ dy[part] = width[part]);
constraint forall(part in PARTS) (dy[part] = length[part] <-> dx[part] = width[part]);
constraint forall(part in PARTS) (dx[part] = length[part] <-> dy[part] = width[part]);

constraint (diffn(x, y, dx, dy)
    /\ forall(part in PARTSx) (x[part] + dx[part] <= plateLength)
    /\ forall(part in PARTSx) (y[part] + dy[part] <= plateWidth));

constraint forall(i in PARTS)(
  dx[i] >= min(length[i], width[i])
  /\ dx[i] <= max(length[i], width[i])
  /\ dy[i] >= min(length[i], width[i])
  /\ dy[i] <= max(length[i], width[i]));

constraint
    lex_lesseq([x[i] | i in nParts..nParts + 2 ], reverse([x[i] | i in nParts..nParts + 2 ]))
    /\ lex_lesseq([y[i] | i in nParts..nParts + 2 ], reverse([y[i] | i in nParts..nParts + 2 ]))
    /\ lex_lesseq([dx[i] | i in nParts..nParts + 2 ], reverse([dx[i] | i in nParts..nParts + 2 ]))
    /\ lex_lesseq([dy[i] | i in nParts..nParts + 2 ], reverse([dy[i] | i in nParts..nParts + 2 ]));

constraint forall(i, j in PARTS where i < j)(
    (length[i] = length[j] /\ width[i] = width[j] ) \/ (length[i] = width[j] /\ width[i] = length[j])
    <-> x[i] + dx[i] <= x[j] \/ y[i] + dy[i] <= y[j]);

constraint x[nParts + 2] + dx[nParts + 2] = plateWidth;
constraint y[nParts + 1] + dy[nParts + 1] = plateLength;

%constraint x[nParts] = 0;
%constraint y[nParts] = 0;
%constraint dx[nParts] = 100;
%constraint x[nParts -1] = 100;
%constraint y[nParts -1] = 0;
%constraint dx[nParts -1] = 100;
%constraint x[nParts -2] = 200;
%constraint y[nParts -2] = 0;
%constraint dx[nParts -2] = 100;
%constraint x[nParts -3] = 300;
%constraint y[nParts -3] = 0;
%constraint dx[nParts -3] = 100;


solve maximize dx[nParts + 1] * dy[nParts + 1] + dx[nParts + 2] * dy[nParts + 2];