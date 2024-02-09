import matplotlib.pyplot as plt
from matplotlib import use as backendUse
from io import BytesIO
import base64

backendUse("agg")

def createFigure():
    x = [1,2,3,4]
    y = [4,1,3,2]
    plt.scatter(x,y)

    stream = BytesIO()
    plt.savefig(stream, format="png")
    plt.close()                         #Without this we have memory leaks
    figure = base64.b64encode(stream.getbuffer()).decode("ascii")

    return figure