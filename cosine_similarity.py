from csv import reader
from csv import writer
import math 


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def rows_readFile(file_name):
    '''
        this function will read the file row by row
    '''
    
    csv_arr =[]
    with open(file_name, 'r') as csv_file:
        csv_reader = reader(csv_file)
        for row in csv_reader:
            csv_arr.append(row)
        
    
    return csv_arr
