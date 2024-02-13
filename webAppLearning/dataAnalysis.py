import pandas as pd
import numpy as np

def parseData(filepath): 
    dataset =  pd.read_csv(filepath,usecols=['x','y']).values       #TODO: Handle different column names
    return(dataset)

def trainModel(data,learningRate,iterations):
    X = data[:,0]
    xPrime = np.vstack((np.ones((X.size, )), X)).T
    Y = data[:,1]
    Y = Y.reshape(Y.size,1)
    m = Y.shape[0]
    theta = np.zeros((2,1))
    
    for i in range(0,iterations):
        yHat = np.dot(xPrime,theta) 

        dTheta = (1/m)*np.dot(xPrime.T, yHat - Y)
        theta = theta - learningRate*dTheta
        if i == iterations:
            cost = (1/(2*m))*np.sum(np.square(yHat - Y))

    return theta, cost