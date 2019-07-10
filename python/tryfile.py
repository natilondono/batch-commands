import numpy as np
import pandas as pd
print ("blah")
import matplotlib.pyplot as plt
from ripser import ripser
from persim import plot_diagrams
data = pd.read_csv("graphs/facebook_mess_norm.txt", sep=" ")
dgms = ripser(data)['dgms']
plot_diagrams(dgms, show=True)
