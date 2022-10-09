import ches_math as cm;
from gauss import solve;
from substituicao_retroativa import op as sr;
from substituicao_sucessiva import op as ss;
import decomposicao_lu as lu;




m = int(input());
n = int(input());

A = cm.entrada_matriz(m, n);

L, U = lu.solve(A);






cm.printa_matriz(L);
cm.printa_matriz(U);

C = cm.multiplica(L, U);
cm.printa_matriz(C);
        