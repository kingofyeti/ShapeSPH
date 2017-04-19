from pyassimp import *
import sys
import os
import numpy as np

def stl_to_ply(stl_file_name,ply_file_name):
  scene = load(stl_file_name) 
  out_file = open(ply_file_name,'wb')
  header_str = 'ply\nformat ascii 1.0\n'

  vertices_num = 0;
  for idx,mesh in enumerate(scene.meshes):
    vertices_num += len(mesh.vertices)
  header_str += 'element vertex {}\n'.format(vertices_num)
  property_str_suffix = ['x','y','z','nx','ny','nz']
  property_str = '';
  for one_suffix in property_str_suffix:
    header_str += 'property float {}\n'.format(one_suffix);
  face_num = vertices_num / 3
  header_str += 'element face {}\n'.format(face_num)
  header_str += 'property list uint uint vertex_indices\n'
  header_str += 'end_header\n'
  out_file.write(header_str)
  
  # Vertices part
  for mesh in scene.meshes:
    if (len(mesh.vertices) != len(mesh.normals)):
      print 'Error: Mesh!'
      return False
    out_vertex_array = np.append(mesh.vertices,mesh.normals,axis=1)
    for i in xrange(len(out_vertex_array)):
      oneline_str = ' '.join(map(str,out_vertex_array[i])) + '\n'
      out_file.write(oneline_str)

  for i in xrange(face_num):
    oneline_str = '3 {} {} {}\n'.format(i*3,i*3+1,i*3+2)
    out_file.write(oneline_str)
  
  out_file.close
  release(scene)
  return True


def get_dir_path(dir_path,os_list):
  file_list = os.listdir(dir_path)
  for file_name in file_list:
    file_path = os.path.join(dir_path,file_name)
    if os.path.isdir(file_path):
      get_dir_path(file_path,os_list)
    else: 
      file_prefix_name = os.path.splitext(file_name)[0]
      file_type = os.path.splitext(file_name)[1]
      if (file_type == '.stl'):
        os_list.append(file_path[:-4])  
  return

def all_stl_to_ply(dir_path):
  dir_list = []
  # Save all file path
  dir_list_path = './dir_list.txt'
  out_dir_list_file = open(dir_list_path,'wb')
  get_dir_path(dir_path,dir_list)
  for x in dir_list:
    out_dir_list_file.write(x + '\n')
    if(not stl_to_ply(x + '.stl',x + '.ply')):
      print 'Error'
  out_dir_list_file.close 
  print 'Success!'
  return
  
all_stl_to_ply('../data_in')
