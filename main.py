import ches_math as cm;
from gauss import solve;
from substituicao_retroativa import op as sr;
from substituicao_sucessiva import op as ss;
import decomposicao_lu as lu;
import cholesky as cl;

A = [
        [8, 28.27, 125.24, 1341],
        [28.27, 125.84, 627.88, 4823.92],
        [125.24, 627.88, 3337.38, 21286.27]
    ];



LL, det, erro = cl.solve(A); #Cholesky

cl.refine(LL); #remove elementos inuteis

#cm.printa_matriz(LL);

cpy = LL.copy(); #copia pra fazer a transposta sem bugar o bagulho




a, b = cm.split_matriz_solucao(LL); #separa o vetor de igualdade

y = ss(a, b, len(a)); #substituicao sucessiva na matriz inferior

LLT = list(map(list, zip(*cpy))); #transposta
LLT.remove(LLT[-1]); #remove a ultima linha

x = sr(LLT, y, len(LLT)); #substituicao sucessiva na transposta

print(x); #vetor resultado