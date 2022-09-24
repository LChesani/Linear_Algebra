import ches_math as cm;
from gauss import gauss;
from substituicao_retroativa import op as sr;
from substituicao_sucessiva import op as ss;





m = int(input());
n = int(input());

A = cm.entrada_matriz(m, n);

#b = cm.entrada_solucao(m);

#x = sr(A, b, m);

B = gauss(A);

cm.printa_matriz(B);
#B = gauss.gauss(A);


        