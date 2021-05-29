import matplotlib.pyplot as plt
import numpy as np


def createGrid():
    numRows = int(input("Enter the number of rows! "))
    numColumns = int(input("Enter the number of columns! "))
    plt.xticks(np.arange(numColumns+1))
    plt.yticks(np.arange(numRows+1))

    ax = plt.gca()
    list = ["Q", "V", "P", " "]
    ax.axes.xaxis.set_ticklabels([])
    ax.axes.yaxis.set_ticklabels([])
    for y in range(numRows, -1, -1):
        for x in range(numColumns+1):
            plt.text(x,y, f"({x},{y})")
            if x != 0 and y != 0:
                random = np.random.randint(0,len(list))
                plt.text(x-0.5, y-0.5, list[random])
    plt.grid()


createGrid()
plt.show()