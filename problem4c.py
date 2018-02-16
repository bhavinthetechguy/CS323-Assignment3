#Bhavinkumar Patel
#Nimit Doshi

import numpy as np
import math

L = np.zeros([3,3])
U = np.zeros([3,3])

def Gaussian_Elimination(A):
    m=A.shape[0]
    n=A.shape[1]
    if(m!=n):
        print 'Matrix is not square!'
        return
    for k in range(0,n-1):
        if A[k,k] == 0:
            return
        for i in range(k+1,n):
            A[i,k]=np.float32(A[i,k]/A[k,k])
        for j in range(k+1,n):
            for i in range(k+1,n):
                A[i,j]-=np.float32(A[i,k]*A[k,j])
                A[i,j] = np.float32(A[i,j])
                
def Elimination_Matrix(A): 
    np.fill_diagonal(L,1) 
    x = A.shape[0]
    for q in range(0,x):
        for w in range(0,q):
            L[q,w] = A[q,w]
    c = 0
    x=A.shape[0]
    for r in range(0,x):      
        for t in range(c,x):
            U[r,t] = A[r,t]
        c = c+1

def Forward_Substitution(L,b,x):
    m=L.shape[0]
    n=L.shape[1]
    if(m!=n):
        print 'Matrix is not square!'
        return
    for j in range(0,n):
        if L[j,j] == 0:
            print 'Matrix is singular!'
            return          # matrix is singular
        x[j] = b[j]/L[j,j]
        for i in range(j+1,n):
            b[i] = b[i] - L[i,j]*x[j]

def Back_Substitution(U,b,x):
    m=U.shape[0]
    n=U.shape[1]
    if(m!=n):
        print 'Matrix is not square!'
        return
    for j in range(n-1,-1,-1):
        if U[j,j] == 0:
            print 'Matrix is singular!'
            return          # matrix is singular
        x[j] = b[j]/U[j,j]
        for i in range(0,j):
            b[i] = b[i] - U[i,j]*x[j]

def main():
    A=np.matrix([[0.1,0.2,0.3],[0.4,0.5,0.6],[0.7,0.8,0.9]])
    Gaussian_Elimination(A)
    b = np.matrix([[0.1],[0.3],[0.5]])
    x = np.dot(np.linalg.inv(A),b)
    
    b1 = np.matrix([[0.1],[0.3],[0.5]])
    A1=np.matrix([[0.1,0.2,0.3],[0.4,0.5,0.6],[0.7,0.8,0.9]])
   
    print ' '
    print "Values of X Using Guassian Elimination:"
    print x
    print "\n"

    ax= np.dot(A1,x)
     
    condA = np.linalg.cond(A1)
    print "Condition Number of A:" , condA
    print "\n"

if __name__ == "__main__":
    main()
    







