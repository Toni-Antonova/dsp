# Matrix Algebra

#downloaded and played around with octave - .octaverc 

#followed these installation instructions: https://adampash.com/how-to-install-octave/

A = [1, 2, 3; 2, 7, 4]
B = [1, -1; 0, 1]
C= [5, -1; 9, 1; 6, 0]
D=[3,-2,-1;1,2,3]
U =[6,2,-3,5]
V =[3,5,-1,4]
W =[1;8;0;5]



size(A)

size(B)

size(C)

size(D)

size(U)

size(V)

size(W)

U+V

U-V

6*V

U*V


A+C

A-C'

C'-3*D

B*A

B*A'
      
      
#I used python for this part because I wasn't sure what to do in octave:
      
print('||u||')
import numpy as np
print(np.linalg.norm(U))
