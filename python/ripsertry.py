from pylab import *
from ripser import ripser
from persim import plot_diagrams
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
import stableRANK as sr
import listmaker as lm

def barcode(thedata):
        dgms= thedata
        i=0
        dic={}
        while i<len(thedata):
            dic["H"+str(i)]=dgms[i]
            i=i+1
        return sr.bc(dic)

################################################

data_try = list([np.array([[0.06126404652860065, 20],
[0.0637818082556853, inf]]),np.array([[0.07377368243910108, 0.00000001]]), np.array([
[0.01125152421057371, 20],
[0.04432581875866819, inf],
[0.031626459502142734, inf],
[0.08152887908155626, inf],
[0.09730552531141861, inf],
[0.08708784657145582, inf],
[0.09800609255340356, inf],
[0.03623152116739087, inf]]),np.array([[0.016173805713055378, inf],
[0.08884911332084169, 20]])])

all = False

#turn the data into a list
data_2 = lm.listmaker('../../dimension_alpha')

#build the bc instance
final_output = barcode(data_2)

#this we always want
mpl.style.use('seaborn')

if(all):
    

    #plot the birth-death diagram
    plot_diagrams(data_2, show= True)

    #plot the life time diagram
    plot_diagrams(data_2, lifetime=True, show=False)

    # plot the barcodes 
    the_barcod_fig = plt.figure(figsize=(20, 20))
    final_output.plot("bar")
    the_barcod_fig.savefig('barcodetry1')

#signatures
#all together
all_at_once = True

if all_at_once:
    figsizea = (30,30)
else:
    figsizea = (4,4)


#build up for signatures
signature = final_output.stable_rank_max()
border=1
linewidth=1.0
signature_fig = plt.figure(figsize=figsizea)

if all_at_once:
    i=1
    
    color=["red","orange","blue","black","green","pink","mediumorchid","grey","crimson","grey"]
    for k in signature.keys():
        if i < 10:
            a = plt.subplot(3,3,i)
            signature[k].plot(border, color[i-1],linewidth)
            i=i+1
            a.set_title(k)
    signature_fig.savefig('signaturetry')

    #part 2
    figsizea2 = (4,4)
    signature_fig2 = plt.figure(figsize=figsizea2)
    signature["H9"].plot(border, "crimson",linewidth)
    plt.title("H9 signature")
    plt.show
    signature_fig2.savefig('signature_H9')

else:
    # just one signature
    signature["H0"].plot(border, "crimson",linewidth)
    plt.title("H0 signature")
    plt.show
    signature_fig.savefig('signature_H0')
