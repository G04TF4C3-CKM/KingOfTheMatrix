#!/bin/python3
#CKM 5.14.2022
import math
import os
import random
import re
import sys
import copy
from collections import deque

def DFS_Recurse(H,h,T,V,Q):
    #print('-----DFS_Recurse------- H= {}, h = {}, T = {}, V = {}'.format(H,h,T,V))
    v = h[0]
    N_v = h[1]
    if N_v == []:
        #print('Leaf Found! leaf v = {}'.format(v))
        #print('Q = {}'.format(Q))
        if Q == deque():
            return(H, T, V, Q)
        else:
            prev = Q.pop()
        H, T, V, Q = DFS_Recurse(H,prev,T,V,Q)
        return(H,T,V,Q)
    else:
        new = N_v.pop(0)
        while new in V:
            if N_v == []:
                H, T, V, Q = DFS_Recurse(H, (v,[]), T, V, Q)
                return(H, T, V, Q)
            else:
                new = N_v.pop(0)
            
        T[v].append(new) 
        T[new] = [v]
        V.add(new)
        Q.append((v,N_v)) #move to first neighbor of v
        for h in H:
            if v in H[h]:
                H[h].remove(v)
        h = (new,H[new])
        H.pop(h[0])
        H, T, V, Q = DFS_Recurse(H,h,T,V,Q)
        return(H, T, V, Q)

def DFS(G,h):
    #print('-------Enter DFS-------')
    #print('G = {}, h = {}'.format(G,h))
    Q = deque()
    H = copy.deepcopy(G)
    v = h[0]
    N_v = h[1]
    if N_v == []:
        #print('Isolate Found!')
        return({v : []},[])
    else:
        T = {}
        new = N_v.pop(0)
        T[v] = [new]
        Q.append((v,N_v)) #start with v and N(v remove w)
        T[new] = [v]
        V = {new}
        for h in H:
            if v in H[h]:
                H[h].remove(v)
        h = (new,H[new]) #this is the key recursion step
        H.pop(h[0])
        H, T, V, Q = DFS_Recurse(H,h,T,V,Q)
        return(T, V)

def LargestCompDFS(n,G):
    H = copy.deepcopy(G)
    #print('-------Enter LargestCompDFS-------')
    #print('G = {}'.format(G))
    Maximus = 0
    count = 1
    
    while count <= n:
        #print('Dynamic graph H = {}'.format(H))
        h = H.popitem()
        count += 1
        T, W = DFS(H,h)
        #print('Pass made T = {}, W = {}'.format(T,W))
        if len(W)+1  > Maximus:
            Maximus = len(W)+1
            #print('We Found A King = {}'.format(Maximus))
        for t in W:
            #print('W = {}, t = {}, H = {}'.format(W,t,H))
            H.pop(t)
            count += 1
            for h in H:
                if t in H[h]:
                    H[h].remove(t)  
    #print('Our King = {}'.format(Maximus))
    return(Maximus)

def GetNeigh(v,G,M):
    #print('Enter GetNeigh(): v = {}, G = {}, M = {}'.format(v,G,M))
    a = v[0]
    b = v[1]
    m = len(M)
    n = len(M[0])
    L = []
    N = []
    
    for i in range(-1,2):
        for j in range(-1,2):
            #print('(i,j) = ({},{})'.format(i,j))
            if a+i == a and b+j == b:
                pass
            elif (a+i < 0) or (b+j < 0) or (a+i >= m) or (b+j >= n):
                pass
            else:
                L.append((a+i,b+j))
    #print('L = {}'.format(L))
    for l in L:
        if M[l[0]][l[1]] == 1:
            N.append( (l[0],l[1]) )
    return(N)

def maxRegion(grid):
    n = 0
    V = {}
    Inv_V = {}
    G = {}
    I = len(grid)
    J = len(grid[0])
    for i in range(I):
        for j in range(J):
            #print('(i,j) = ({},{})'.format(i,j))
            if grid[i][j] == 1:
                n += 1
                V[n] = (i,j)
                Inv_V[(i,j)] = n
                G[n] = []
                            
    #print('n = {},\n G = {},\n V = {}'.format(n,G,V))
    
    for v in G:
        N = GetNeigh(V[v],G,grid)
        Neigh_n = []
        for x in N:
            Neigh_n.append( Inv_V[(x[0],x[1])] )
        G[v] = Neigh_n
        
    #print('G = {}'.format(G))
    #print('grid = {}'.format(grid))
        
    answer = LargestCompDFS(n,G)
    
    return(answer)

# Example:
M = [[0, 1, 0, 0, 0, 0, 1, 1, 0],
[1, 1, 0, 0, 1, 0, 0, 0, 1],
[0, 0, 0, 0, 1, 0, 1, 0, 0],
[0, 1, 1, 1, 0, 1, 0, 1, 1],
[0, 1, 1, 1, 0, 0, 1, 1, 0],
[0, 1, 0, 1, 1, 0, 1, 1, 0],
[0, 1, 0, 0, 1, 1, 0, 1, 1],
[1, 0, 1, 1, 1, 1, 0, 0, 0]]

result = maxRegion(M)
print(result)

