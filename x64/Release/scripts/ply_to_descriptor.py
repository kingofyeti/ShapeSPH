from mpl_toolkits.mplot3d import Axes3D
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

# input path with format: ./abc
# followed by abc.ply abc.des abc.stl etc.
def generate_descriptor(input_path):
  # Remove \n
  input_path = input_path[:-1]
  in_ply_path = input_path + '.ply'
  out_descriptor_path = input_path + '.des'
  command = '..\ShapeDescriptor.exe --in ' + in_ply_path +  ' --out ' + out_descriptor_path
  print command
  os.system(command)
  return

# list path(.txt) is a list of input_path: ./abc
# followed by ./abc.ply ./abc.des ./abc.stl etc.

def generate_descriptors_from_list(list_path):
  file = open(list_path,'rb')
  while True:
    oneline = file.readline()
    if not oneline: break
    generate_descriptor(oneline)
  return

generate_descriptors_from_list('./dir_list.txt')
