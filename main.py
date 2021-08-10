
import math, os, sys, subprocess
import numpy as np
import matplotlib.pyplot as plt

min_height = 1000
max_height = 3000
steps_to_height = 300
gaussian_parameter = 500


def gauss(a, b, c, x):
    return a * math.exp((-(x - b) * (x - b)) / (2 * c * c))


def topo(a, c, start, end):
    X = list(np.arange((start - end) / 2, int(end - start) / 2, 1))
    y = list(map(lambda x: gauss(a, 0, c, x), X))
    topography = [10000 for i in range(10000)]
    for i in range(start, end, 1):
        topography[i] += y[i - start]
    return topography


x = [i for i in range(10000)]  # X cordinate of topo


def plot_topo():
    fig_topos, axs_topos = plt.subplots(1)
    for i in range(min_height, max_height, steps_to_height):
        axs_topos.plot(x, topo(i, gaussian_parameter, 0, 10000), 'black', linewidth=1)
        axs_topos.set_ylim(ymin=0, ymax=15000)
        plt.savefig('Topography_Plot')


# plot_topo()

filename = 'specfem2d/EXAMPLES' \
           '/simple_topography_and_also_a_simple_fluid_layer/DATA/topo.dat'  # topography file in specfem2d

def delete_all_directories():
    for i in range(min_height,max_height,steps_to_height):
        cmd_to_delete='rm -r ' + 'height_' + str(i)
        os.system(cmd_to_delete)
# delete_all_directories()

def run_simulations_with_topo():
    for j in range(min_height, max_height,steps_to_height):  # min to max topography range
        y = topo(j, gaussian_parameter, 0, 10000)
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
        cmd_to_make_new_dir = 'mkdir ' + 'height_' + str(j)
        cmd_to_copy_files = 'cp ./specfem2d/EXAMPLES/simple_topography_and_also_a_simple_fluid_layer/OUTPUT_FILES/*.semd ./height_' + str(
            j)
        # Running the simulations on linux terminal
        os.system('''
        cd ./specfem2d/EXAMPLES/simple_topography_and_also_a_simple_fluid_layer
        ./run_this_example.sh
        cd ..
        cd ..
        cd ..
        ''')
        os.system(cmd_to_make_new_dir)
        os.system(cmd_to_copy_files)
# run_simulations_with_topo()
#reading files
for i in range(1000, 3000, 300):  # max_height_range
    folder_name = 'height_' + str(i)
    data_X = []
    data_Z = []
    for j in range(1, 11):
        receiver_number = j
        if receiver_number >= 10:
            receiver_number = str(receiver_number)
        else:
            receiver_number = '0' + str(receiver_number)
        seismogram = 'AA.S00PP.BXX.semd'
        seismogram = seismogram[0:6] + receiver_number + seismogram[8:]
        seismogram2 = seismogram
        seismogram2 = list(seismogram)
        seismogram2[11] = 'Z'
        seismogram2 = ''.join(seismogram2)
        seismogram = folder_name + '/' + seismogram
        seismogram2 = folder_name + '/' + seismogram2
        # print(seismogram, seismogram2)
        with open(seismogram) as f:
            line_x=[]
            line_y=[]
            for line in f:
                a,b=line.split()
                line_x.append(float(a))
                line_y.append(float(b))
            data_X.append([line_x,line_y])
        f.close()
        with open(seismogram2) as f:
            line_x=[]
            line_y=[]
            for line in f:
                a,b=line.split()
                line_x.append(float(a))
                line_y.append(float(b))
            data_Z.append([line_x,line_y])
        f.close()
    fig_plot,axs_plots=plt.subplots(10,sharex=True,gridspec_kw={'hspace':0})
    for k in range(10):
        axs_plots[k].plot(data_X[k][0],data_X[k][1],color='b',linewidth=.5)
        axs_plots[k].set_ylabel(str(k+1),fontsize=6)
        axs_plots[k].spines["top"].set_visible(False)
        axs_plots[k].spines["bottom"].set_visible(False)
        axs_plots[k].set_yticks([])
    plt.xlabel("Time")
    plt.savefig(str(i)+'_X_'+'.png')
    plt.cla()
    plt.clf()
    for k in range(10):
        axs_plots[k].plot(data_Z[k][0], data_Z[k][1], color='b', linewidth=.5)
        axs_plots[k].set_ylabel(str(k + 1), fontsize=6)
        axs_plots[k].spines["top"].set_visible(False)
        axs_plots[k].spines["bottom"].set_visible(False)
        axs_plots[k].set_yticks([])
    plt.xlabel("Time")
    plt.savefig(str(i) + '_Z_' + '.png')


