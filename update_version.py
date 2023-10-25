#!/usr/bin/env python3
import copy
import os

def update_version():
  py_file = open('version.py', 'r')  
  #get the list of line
  line_list = py_file.readlines()
  #increment minor version
  minor_version = int(line_list[3].split()[2].split('.')[1]) + 1
  py_file.close()

  py_file = open('version.py.tmp', 'x')
  py_file.close()

  py_file = open('version.py.tmp', 'w')
  line_list[3] = '  version = "0.{}.0"\n'.format(minor_version)
  py_file.writelines(line_list)
  py_file.close()

  os.remove('version.py')
  os.rename('version.py.tmp', 'version.py')

if __name__ == '__main__':
  update_version()
