
#bootcamp utils: a collection of statistical functions
#proved useful to 55 students
import numpy as np

def ecdf(data):
    '''
    compute s, y values for an empirical distribution function
    '''
    x = np.sort(data)
    y = np.arange(1, 1+len(x)) / len(x)

    return x, y
