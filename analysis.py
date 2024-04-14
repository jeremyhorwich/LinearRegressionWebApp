import pandas as pd
import numpy as np

def parse_data(filepath): 
    dataset =  pd.read_csv(filepath).values
    return(dataset)

def train_model(data,learningRate,iterations):
    X = data[:,0]
    x_prime = np.vstack((np.ones((X.size, )), X)).T
    Y = data[:,1]
    Y = Y.reshape(Y.size,1)
    m = Y.shape[0]
    theta = np.zeros((2,1))
    
    for i in range(0,iterations):
        y_hat = np.dot(x_prime,theta) 

        d_theta = (1/m)*np.dot(x_prime.T, y_hat - Y)
        theta = theta - learningRate*d_theta
        if i == (iterations - 1):
            cost = (1/(2*m))*np.sum(np.square(y_hat - Y))

    return theta, cost