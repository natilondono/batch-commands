import numpy as np
import random
import math
import matplotlib.pyplot as plt


def listmaker (nameoffile):
    f = open(nameoffile,"r")

    mylist = []

    final_list = []

    for line in f:
        current_list = []
        for char in line:
            decimal = (random.random()/10)
            if char == '0':
                current_list.append(decimal)
                continue
            if char == '1':
                current_list.append(1 + decimal)
                continue
            if char == '2':
                current_list.append(2 + decimal)
                continue
            if char == '3':
                current_list.append(3 + decimal)
                continue
            if char == '4':
                current_list.append(4 + decimal)
                continue
            if char == '5':
                current_list.append(5 + decimal)
                continue
            if char == '6':
                current_list.append(6 + decimal)
                continue
            if char == '7':
                current_list.append(7 + decimal)
                continue
            if char == '8':
                current_list.append(8 + decimal)
                continue
            if char == '9':
                current_list.append(9 + decimal)
                continue
            if char == 'i':
                current_list.append(math.inf)
                continue
            if char == '*':
                current_list.append(11 + decimal)
                continue
            if (len(current_list) == 2):
                mylist.append(current_list)
                current_list = []
            if char == ')':
                final_list.append(np.asarray(mylist))
                mylist = []
            else:
                continue
        if (len(current_list) != 0):
            mylist.append(current_list)

    return final_list



def dimension_filtration_simple(list_of_tuples):
    
    fig, ax= plt.subplots()
    max_dim = 0
    #find out the maximum dimension
    for tuples in list_of_tuples:
        if(tuples[1] != np.inf and tuples[1] > max_dim):
            max_dim = tuples[1]

    #draw the delimiter lines
    x_labels=np.arange(0,max_dim,1)
    for dimen in x_labels:
        ax.barh(dimen, max_dim, 0.2, 0, color ='pink', linestyle='dotted')

    #draw the barcodes
    for tuples in list_of_tuples:
        if(np.isfinite(tuples).all()):
            ax.barh(tuples[0], int(tuples[1]-tuples[0]), 0.2, tuples[0], color ='black' )
        else:
            ax.barh(tuples[0], int(max_dim-tuples[0]), 0.2, tuples[0], color ='blue' )
    
    #fix the axes
    ax.set_xticks(x_labels)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Life time')
    ax.set_title('Homologies')
    #plt.show()
probando =[[0,1],[0,np.inf],[1,2],[3,np.inf],[3,np.inf]]
