import spyder as ad
import numpy as np
import pandas as pd
D=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(D)
print()
# mat = np.matrix(np.arange(4).reshape(2,2))
# mT=mat.T
# mH=mat.H
# mI=mat.I
# print("mT={}\n mH={}\n mI={}".format(mT,mH,mI))
d=D[D>5]
print(d)