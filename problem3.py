#Bhavinkumar Patel
#Nimit Doshi


import numpy as np
import math    


def diff_b():
    A = np.matrix([[0.16,0.10],[0.17,0.11],[2.02,1.29]])
    At =np.transpose(A)

    aat= np.dot(At, A)
    
    x = np.zeros(2);

    b = np.matrix([[0.27],[0.25],[3.33]])
    bx = np.dot(At, b)
    
    x = np.dot(np.linalg.inv(aat), bx)
    print "\n"
    print "With different b value:"
    print " Value of X:"
    print x
    print "\n"
    
    cond1 = np.linalg.cond(aat,1)
    cond2 = np.linalg.cond(aat,2)
    condinfi = np.linalg.cond(aat,np.inf)
    print "Condition number of A^TA for Norm 1:", cond1
    print "Condition number of A^TA for Norm 2:", cond2
    print "Condition number of A^TA for Norm infinity:", condinfi
    print "\n"
    cond = np.linalg.cond(A)
    print "K(A)^2:", cond ** 2
    condA = np.linalg.cond(aat)
    print "K(A^TA):", condA
    
def main():
    A = np.matrix([[0.16,0.10],[0.17,0.11],[2.02,1.29]])
    At =np.transpose(A)

    aat= np.dot(At, A)
    x = np.zeros(2);

    b = np.matrix([[0.26],[0.28],[3.31]])
    bx = np.dot(At, b)
    x = np.dot(np.linalg.inv(aat), bx)
    print " Value of X:"
    print x
    
    
if __name__ == "__main__":    
    main()
    diff_b()
