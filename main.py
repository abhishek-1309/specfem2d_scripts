import math
import os
import sys

import numpy as np
import matplotlib.pyplot as plt
import subprocess


def gauss(a, b, c, x):
    return a * math.exp((-(x - b) * (x - b)) / (2 * c * c))


def topo(a, c, start, end):
    X = list(np.arange((start - end) / 2, int(end - start) / 2, 1))
    y = list(map(lambda x: gauss(a, 0, c, x), X))
    topography = [10000 for i in range(10000)]
    for i in range(start, end, 1):
        topography[i] += y[i - start]
    return topography


x = [i for i in range(10000)]
# y=topo(100,50,3000,7000)
fig, axs = plt.subplots(1)
# for i in range(100, 2000, 300):
    # axs.plot(x, topo(i, 500, 0, 10000), 'black',linewidth=1)
# axs.set_ylim(ymin=0, ymax=15000)
# plt.show()
filename='specfem2d/EXAMPLES' \
         '/simple_topography_and_also_a_simple_fluid_layer/DATA/interfaces_simple_topo_curved.dat '

f=open(filename,'w')
print(f)

sys.exit()
#Running the simulations
os.system('''
cd ./specfem2d/EXAMPLES/simple_topography_and_also_a_simple_fluid_layer
./run_this_example.sh
cp 
''')
