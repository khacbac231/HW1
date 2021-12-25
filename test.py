from matplotlib.pyplot import plot
import numpy as np
from test_linreg_univariate import plotData1D
from test_linreg_univariate import plotRegLine1D
from linreg import LinearRegression
filePath = "data/univariateData.dat"
file = open(filePath, 'r')
allData = np.loadtxt(file, delimiter=',')
X = np.matrixlib.matrix(allData[:,:-1])
y = np.matrixlib.matrix((allData[:,-1])).T
from test_linreg_univariate import plotData1D
plotData1D(X,y)
n,d = X.shape
print(n)
print(d)
X = np.c_[np.ones((n,1)), X]
#print(X)
init_theta = np.matrixlib.matrix(np.ones((d+1,1)))*10
print(init_theta)