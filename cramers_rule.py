import numpy as np
#cramer's rule for 2x2
def det_2x2(A):
    #split up the 
    a_1 = A[0][0]
    a_2 = A[1][0]
    b_1 = A[0][1]
    b_2 = A[1][1]
    #perform calculation
    detA = ((a_1)*(b_2)-(a_2)*(b_1))
    
    return detA

def det_3x3(B):
    #break up the 3x3 matrix
    B_0 = B[1:3:1, 1:3:1]
    B_1 = B[1:3:1, 0:3:2]
    B_2 = B[1:3:1, 0:2:1]
    #perform calculation
    detB = B[0][0]*det_2x2(B_0) - 
    B[0][1]*det_2x2(B_1) + B[0][2]*det_2x2(B_2)
    
    return detB

def cramer_2x2(A,b):
    #create temp values when replacing b into A
    tempA = A*1
    tempB = A*1
    tempA[0:,0,] = b[:,0]
    tempB[0:,1,] = b[:,0]
    
    #solve using cramer's rule
    x = det_2x2(tempA)/det_2x2(A)
    y = det_2x2(tempB)/det_2x2(A)
    
    return x,y

def cramer_3x3(A3,b3):
    #create temp values when replacing b into A
    tempAx = A3*1
    tempAy = A3*1
    tempAz = A3*1
    
    #replace specific columns with b3
    tempAx[0:,0] = b3[:,0]
    tempAy[0:,1] = b3[:,0]
    tempAz[0:,2] = b3[:,0]
    
    #solve using cramer's rule
    x = det_3x3(tempAx)/det_3x3(A3)
    y = det_3x3(tempAy)/det_3x3(A3)
    z = det_3x3(tempAz)/det_3x3(A3)

    return x,y,z
