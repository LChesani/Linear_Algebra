import ches_math as cm;


def sub_vet(v1, v2):
    x = [0 for _ in range(0, len(v1))]
    for i in range(0, len(v1)):
        x[i] = v2[i] - v1[i];
    return x;

def solve(a, b):
    return b/a;


def linha_multiplica(l, mult):
    for i in range(0, len(l)):
        l[i] = l[i] * mult;
    return l;

def gauss(A):
    pivot = float();
    mult = float();
    for i in range(0, len(A)):
        pivot = A[i][i];
        for j in range(i+1, len(A)):
            mult = solve(A[j][i], A[i][i]);
            A[j] = sub_vet(linha_multiplica(A[i], mult), A[j]);
    return A;
            
