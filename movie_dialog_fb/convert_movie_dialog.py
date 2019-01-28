#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 12:36:57 2018

@author: genevieve

"""
from numpy import array
import os

class convert_text(object):
    
    
    def __init__(self, rootdir):    
        self.rootdir = rootdir
#        self.data=[]
        self.location=[]
        #file_name="babi2_p0.5_rl10_ask_for_sf_train.txt"
        #location=os.path.join('/Users/genevieve/Documents/dbll/babi',file_name)
        #location='/Users/genevieve/Documents/movie_dialog_dataset/task4_reddit_download/task4_reddit_test.txt'

    def search_directory(self):
        for subdir, dirs, files in os.walk(rootdir):
            for file in files:
                if file.endswith("dev.txt") or file.endswith("test.txt") or file.endswith("train.txt"): 
                    location= os.path.join(subdir, file)
                    print (os.path.join(subdir, file))
                    self.location.append(location)
                    self.open_loc(location)

        
                
    
    def open_loc(self,location):
        
 #       location='/Users/genevieve/Documents/GitHub/data_processing_xml_movie/movie_dialog_fb/task1_qa/task1_qa_test.txt'

        f = open(location, 'r') # open the file for reading
        data=[]
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

        
        self.create_clean(data,location)
    
    def create_clean(self,data,location):
        #data_file="babi2_p0.5_rl10_ask_for_sf_train"+".txt"
 #       location="/Users/genevieve/Documents/GitHub/data_processing_xml_movie/movie_dialog_fb/task1_qa/task1_qa_test.txt"
        dirname1 = os.path.basename(location) 
        file_name=dirname1.split(".")[0]
        location=os.path.join('/Users/genevieve/Documents/data',dirname1)
        
        
        
        
            
        word_count=0
        extra=0
        thefile=open(location,'w')
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
                 word_count+=len(line[0].split())
                 word_count+=len(line[1].split())
                 thefile.write("speaker1: %s \nspeaker2: %s \n" % (line[0],line[1]))
                 
             if word_count >= 1000:
                  word_count=0
                  extra+=1
                  thefile.close()
                  location=os.path.join('/Users/genevieve/Documents/data',file_name+'_extra'+str(extra)+'.txt')    
                  thefile=open(location,'w')  
                   
        
        thefile.close() 
        print(word_count)
    


rootdir = './data_processing_xml_movie/movie_dialog_fb'                
f1=convert_text(rootdir)
f1.search_directory()


   


        






 


  
