import numpy as np
from scipy import stats
import re

def main():
    print("Stat analysis here")
    print("Default layout is: \n Samples, Stdev, Mean, Max, Min, Median, Mode")
    
    datafile = open("out.txt","r") #out.txt contains a single input from the user per line
    grid=datafile.read()
    datafile.close()
    grid = grid.split("\n") #grid is an array of lines
    print("Word length analysis")
    print(quickstat(analyseWordLength(grid)))

def quickstat(data):
    arrOut = []
    arrOut.append(len(data))
    arrOut.append(np.std(data))
    arrOut.append(np.mean(data))
    arrOut.append(np.amax(data))
    arrOut.append(np.amin(data))
    arrOut.append(np.median(data))

    return arrOut

def analyseWordLength(raw):
    arrOut = []
    for k in raw:
        work = re.split("; |, |\\ |- |~",k)
        for l in work:
            arrOut.append(len(l))

    return arrOut

if __name__ == "__main__":
    main()

