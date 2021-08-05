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
# y=topo(100,500,0,10000)
filename='specfem2d/EXAMPLES' \
         '/simple_topography_and_also_a_simple_fluid_layer/DATA/topo.dat'
fig, axs = plt.subplots(1)
for j in range(1000, 1400, 300):
    # axs.plot(x, topo(i, 500, 0, 10000), 'black',linewidth=1)
    y=topo(j, 500, 0, 10000)
    f = open(filename, 'w')
    f.truncate(0)
    f.write("3 \n")
    f.write("10000\n")
    for i in range(10000):
        f.write(str(i) + " " + str(0) + '\n')
    f.write("10000\n")
    for i in range(10000):
        f.write(str(i) + " " + str(9000) + '\n')
    f.write("10000\n")
    for i in range(10000):
        f.write(str(i) + " " + str(y[i]) + '\n')
    f.write("200\n40")
    f.close()
    cmd2='mkdir '+'height_'+str(j)
    cmd3='cp ./specfem2d/EXAMPLES/simple_topography_and_also_a_simple_fluid_layer/OUTPUT_FILES/*.semd ./height_'+str(j)
    print(cmd2)
    print(cmd3)
    # Running the simulations
    os.system('''
    cd ./specfem2d/EXAMPLES/simple_topography_and_also_a_simple_fluid_layer
    ./run_this_example.sh
    cd ..
    cd ..
    cd ..
    ''')
    os.system(cmd2)
    os.system(cmd3)

# axs.set_ylim(ymin=0, ymax=15000)
# plt.show()


sys.exit()
# print(max(y))
f=open(filename,'w')
f.truncate(0)
f.write("3 \n")
f.write("10000\n")
for i in range(10000):
    f.write(str(i)+" "+str(0)+'\n')
f.write("10000\n")
for i in range(10000):
    f.write(str(i)+" "+str(9000)+'\n')
f.write("10000\n")
for i in range(10000):
    f.write(str(i) + " " + str(y[i]) + '\n')
f.write("200\n40")
f.close()
#Running the simulations
os.system('''
cd ./specfem2d/EXAMPLES/simple_topography_and_also_a_simple_fluid_layer
./run_this_example.sh
cd ..
cd ..
cd ..
mkdir height
cp ./specfem2d/EXAMPLES/simple_topography_and_also_a_simple_fluid_layer/OUTPUT_FILES/*.semd ./height_100
''')
#fft after plotting
