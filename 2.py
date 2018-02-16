#Bhavinkumar Patel
#Nimit Doshi

import numpy as np
import math
import matplotlib.pyplot as plt

x = np.matrix([[0.0],[1.0],[2.0],[3.0],[4.0],[5.0]])
y = np.matrix([[1.0],[2.7],[5.8],[6.6],[7.5],[9.9]])
    
for i in range(0,6):
    print "Degree:" , i
    A = np.matrix(np.zeros((6,i+1)))
    '''x = np.array([0.0,1.0,2.0,3.0,4.0,5.0])
    y = np.array([1.0,2.7,5.8,6.6,7.5,9.9])

    for i in range(0,6):
        poly = np.polyfit(x,y,i)
        p = np.poly1d(np.polyfit(x,y,i))
        Error = y - p(x)
        SumError = np.sum(Error ** 2)
        print "Degree:" , i
        print poly
        print "Sum Squared error:", SumError
        print "\n"
        plt.plot(x,y,"o",x,p(x))
        plt.title("Degree %d \n Sum Squared Error: %e "%(i,SumError))
        plt.show()
        '''
    for j in range(i+1):
        A[:,j] = np.power(x,j)
    aat = np.transpose(A)
    adotaat = np.dot(aat, A)
    b = np.dot(aat,y)
    inverse = np.linalg.inv(adotaat)
    poly = np.dot(inverse, b)
    matrix= np.transpose(poly)
    array = np.array(matrix)
    print array
    p = A[:,:i+1] * poly
    Error = p - y
    SumError = np.sum(np.power(Error,2))
    print "Sum Squared error:", SumError
    print "\n"
    plt.plot(x,y,"o",x,p)
    plt.title("Degree %d \n Sum Squared Error: %e "%(i,SumError))
    plt.show()

