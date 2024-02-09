import matplotlib.pyplot as plt
from io import BytesIO

def createFigure():
    x = [1,2,3,4]
    y = [4,1,3,2]
    plt.scatter(x,y)

    stream = BytesIO()
    plt.savefig(stream, format="png")
    plt.close()

    return stream