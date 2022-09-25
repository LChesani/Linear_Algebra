import ches_math as cm;
from gauss import gauss;
from substituicao_retroativa import op as sr;
from substituicao_sucessiva import op as ss;





m = int(input());
n = int(input());

A = cm.entrada_matriz(m, n);

A = gauss(A);

B, b = cm.split_matriz_solucao(A);



x = sr(B, b, m);




cm.printa_matriz(x);


        