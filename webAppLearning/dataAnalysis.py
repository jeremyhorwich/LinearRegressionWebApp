import pandas as pd
import numpy as np

def parseData(buffer): 
    dataset =  pd.read_csv(buffer,usecols=['x','y']).values       #Will have to update if we want to handle different column names
    return(dataset)

def trainModel(data,learningRate,iterations):
    X = data[:,0]
    xPrime = np.vstack((np.ones((X.size, )), X)).T
    Y = data[:,1]
    Y = Y.reshape(Y.size,1)
    m = Y.shape[0]

    theta = np.zeros((2,1))
    yHat = 0
    cost = 0
    dTheta = 0
    for i in range(0,iterations):
        yHat = np.dot(xPrime,theta)
        cost = (1/(2*m))*np.sum(np.square(yHat - Y))

        d_theta = (1/m)*np.dot(xPrime.T, yHat - Y)
        theta = theta - learningRate*d_theta

    return theta