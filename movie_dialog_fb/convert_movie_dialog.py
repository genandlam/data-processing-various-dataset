#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 12:36:57 2018

@author: genevieve
"""


from numpy import array
import os


#file_name="babi2_p0.5_rl10_ask_for_sf_train.txt"
#location=os.path.join('/Users/genevieve/Documents/dbll/babi',file_name)

rootdir = './movie_dialog_dataset'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        print (os.path.join(subdir, file))
        
location='/Users/genevieve/Documents/movie_dialog_dataset/task4_reddit_download/task4_reddit_test.txt'
f = open(location, 'r') # open the file for reading
data = []
for row_num, line in enumerate(f):
    # Remove the new line at the end and then split the string based on
    # tabs. This creates a python list of the values.
    values = line.strip().split('\t')
#    values = line.strip().split('\n')
#    if row_num == 0: # first line is the header
#         header = values
    
    data.append([str(v) for v in values])
    
#basic_data = array(data)
f.close() # close the file




#data_file="babi2_p0.5_rl10_ask_for_sf_train"+".txt"
data_file ="task4_reddit_test.txt"
with open(os.path.join('/Users/genevieve/Documents/movie_dialog_dataset/task4/',data_file), "w") as thefile:
#    for col_0, col_1,col_2 in data:
##    for col_0, col_1 in data: 
##      thefile.write("speaker1: %s\nspeaker2: %s \n" % (col_0, col_1))
#        
#      if col_1=='':
#          thefile.write("speaker1: %s\t%s\n" % (col_0, col_2))
#           thefile.write('\n')
#      else:
#          thefile.write("speaker1: %s\nspeaker2: %s\t%s\n" % (col_0, col_1, col_2))
#          
     for  row_num,line in enumerate(data): 
         
         if len(line)==1 and line[0]=="" :
             
                thefile.write('\n')
                
         if len(line)==2 :
             
             thefile.write("speaker1: %s \nspeaker2: %s \n" % (line[0],line[1]))
                    

thefile.close()  


    
    