from mpl_toolkits.mplot3d import Axes3D
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

def graph_generator(des_file_path):
    # Remove \n
    des_file_path = des_file_path+ '.des'
    des_file = open(des_file_path,'rb')
    # Remove '\n'
    header = des_file.readline()[:-1]
    content = des_file.readline()[1:-1]
    content_list = np.array([float(x) for x in content.split(' ')])
    if len(content_list) != 544:
        print "Error: Descriptor size error."
        return
    # All descriptors should be under the shape: (32,17)
    content_list = np.reshape(content_list,(32,17))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x_data, y_data = np.meshgrid( np.arange(content_list.shape[1]),
                              np.arange(content_list.shape[0]))
    x_data = x_data.flatten()
    y_data = y_data.flatten()
    z_data = content_list.flatten()
    ax.bar3d( x_data,y_data,np.zeros(len(z_data)),1, 1, z_data )
    des_image_path = des_file_path + '_des_figure.png'
    fig.savefig(des_image_path)
    plt.close(fig)
    return

def generate_descriptors_from_list(list_path):
  file = open(list_path,'rb')
  while True:
    oneline = file.readline()
    if not oneline: break
    print oneline
    graph_generator(oneline[:-1])
  return

generate_descriptors_from_list('./dir_list.txt')
#graph_generator('../data_in/MS_stl_files_83_Lesions_Guo/MS_stl_files_83_Lesions_Guo/3D13_STL/3D13_ROI_1')