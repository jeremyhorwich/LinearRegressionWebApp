from  matplotlib.figure import Figure
from matplotlib import use as setBackend
from io import BytesIO
import base64

setBackend("agg")

def createFigure():
    x = [1,2,3,4]
    y = [4,1,3,2]
    fig = Figure()                  #Avoiding PyPlot because it's prone to memory leaks
    ax = fig.subplots()
    ax.scatter(x,y)

    stream = BytesIO()
    fig.savefig(stream, format="png")
    figure = base64.b64encode(stream.getbuffer()).decode("ascii")

    return figure