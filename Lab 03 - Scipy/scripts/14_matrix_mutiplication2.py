
import numpy as np

# Method I
x=np.array([[1,2,3],[4,5,6]],float)      # 2 by 3
y=np.array([[1,2],[3,3],[4,5]],float)    # 3 by 2
xy=np.dot(x,y)                           # 2 by 2
print xy

# Method II
x=np.matrix('1,2,3;4,5,6') 
y=np.matrix('1,2;3,3;4,5') 
print x*y