import numpy as np;


def aloca_matriz(m, n):
    A = [[0 for _ in range(0, n)] for _ in range(0, m)];
    return A;

def entrada_matriz(m, n):
    A = [[0 for _ in range(0, n)] for _ in range(0, m)]; #"malloca" tamanho da matriz A
    for i in range(0, m):
        for j in range(0, n):
            A[i][j] = float(input("A" + str(i) + str(j) + ' '));
    return A;

def entrada_solucao(m):
    b = [0 for _ in range(0, m)]; #"malloca" tamanho do vetor solucao
    for bn in range(0, m): #entrada do conjunto solucao
        b[bn] = float(input("b" + str(bn) + ' '));
    return b;

def vetor_resultado(m):
    x = m * [0];
    return x;


def printa_matriz(A):
    print('[', end=' ');
    for i in range(0, len(A)):
        print(A[i], end=' ');
    print(']');