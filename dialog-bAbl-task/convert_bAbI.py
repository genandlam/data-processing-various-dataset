#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 12:36:57 2018

@author: genevieve
"""


from numpy import array
import os

location='./raw_data/dialog-babi-task6-dstc2-dev.txt'
#location='/Users/genevieve/Documents/movie_dialog_dataset/task3_qarecs/task3_qarecs_dev.txt'
file_read = open(location, 'r') # open the file for reading


data = []
#count number of sessions
counter=0

for row_num, line in enumerate(file_read):
    
    values = line.strip().split('\t')
    if values ==['']:
        counter+=1
        
    
    # Remove the new line at the end and then split the string based on
    # newline. This creates a python list of the values.
    values = line.strip().split('\t')
#    if row_num == 0: # first line is the header
#         header = values
   
    data.append([str(v) for v in values])
        
 #basic_data = array(data)       
                    
        
file_read.close() # close the filer       



data_file ="dialog-babi-task6-dstc2-tst"+".txt"    
#data_file = "task3_qarecs_dev"+".txt"
with open(os.path.join('./dialog-bAbl-task6',data_file), "w") as file_write:
    for  row_num,line in enumerate(data):

                
            
            if len(line)==1 and line[0]!="" :
                file_write.write("system: %s" % line[0])
                
            if len(line)==2:
                speech =line[0].split(' ')
                
                if speech[1] == '<SILENCE>':
                    file_write.write("system: %s %s \n" % (line[0],line[1]))
                    
                   
                if speech[1] != '<SILENCE>':
                    
                    file_write.write("speaker: %s \nsystem: %s \n" % (line[0],line[1]))
                    
            else:
                file_write.write("\n")
            
    file_write.close()
    
    
 


    
    