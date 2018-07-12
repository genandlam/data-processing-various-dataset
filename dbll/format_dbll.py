# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 11:09:06 2018

@author: Zi Kun
"""

from numpy import array
import os


class convert_text(object):
    
    
    def __init__(self, rootdir):    
        self.rootdir = rootdir
#        self.data=[]
        self.location=[]
       


    def search_directory(self):
        
        for file in os.listdir(self.rootdir):
            if  file.endswith("train.txt"):
#               print(os.path.abspath(os.path.join(rootdir, '..')))
                location= rootdir+'/'+file
                print(file)
                self.open_loc(location)
                
        
             
                
    
    def open_loc(self,location):
        
 #       location='/Users/genevieve/Documents/GitHub/data_processing_xml_movie/movie_dialog_fb/task1_qa/task1_qa_test.txt'

        f = open(location,'r', encoding="utf8" ) # open the file for reading
       
        data=[]
        
        for row_num, line in enumerate(f):
#           
            # Remove the new line at the end and then split the string based on
            # tabs. This creates a python list of the values.
            values = line.strip().split('\t')
            
            data.append([str(v) for v in values])
           
            

        f.close() # close the file  
        self.create_clean(data,location)
    
    def create_clean(self,data,location):
      
# location=os.path.join('/Users/genevieve/Documents/data',dirname1)
        dirname1 = os.path.basename(location) 
        file_name=dirname1.split(".")[0]+dirname1.split(".")[1]
        location = 'C:/Users/Zi Kun/Documents/dbll_movie_data/'+file_name+'.txt'
    
            
        word_count=0
        extra=0
        file_write=open(location,'w', encoding="utf-8")
        if len(data[0])==2:
        
            for col_0, col_1 in data: 
                
              file_write.write("speaker1: %s\nspeaker2: %s \n" % (col_0, col_1))
              word_count+=len(col_0.split())
              word_count+=len(col_1.split())
              
              if word_count>=1000:
                    word_count=0
                    extra+=1
                    file_write.close()
#                  location=os.path.join('/Users/genevieve/Documents/data_dialog',file_name+'_extra'+str(extra)+'.txt')    
                    location='C:/Users/Zi Kun/Documents/dbll_movie_data/'+file_name+'_extra'+str(extra)+'.txt' 
                    file_write=open(location,'w', encoding="utf8") 
                    
        else:
            
            for col_0, col_1,col_2 in data:
       
              if col_0.split(' ')[0]=='1' and col_0 !=data[0][0]:
                  
                       file_write.write("\n") 
              
              if word_count>=1000:
                        word_count=0
                        extra+=1
                        file_write.close()
    #                  location=os.path.join('/Users/genevieve/Documents/data_dialog',file_name+'_extra'+str(extra)+'.txt')    
                        location='C:/Users/Zi Kun/Documents/dbll_movie_data/'+file_name+'_extra'+str(extra)+'.txt' 
                        file_write=open(location,'w', encoding="utf8") 
                        
              elif col_1=='':
                  
                  file_write.write("speaker1: %s\t%s\n" % (col_0, col_2))
                  word_count+=len(col_0.split())
               
              else:
                  
                  file_write.write("speaker1: %s\nspeaker2: %s\t%s\n" % (col_0, col_1, col_2))
                  word_count+=len(col_0.split())
                  word_count+=len(col_1.split())
              

                
        file_write.close()
        print(word_count)
        
        
    
#rootdir=r'C:\Users\Zi Kun\Documents\GitHub\data_processing_xml_movie\dbll\babi'

rootdir=r'C:\Users\Zi Kun\Documents\GitHub\data_processing_xml_movie\dbll\movieqa-dbll'         
f1=convert_text(rootdir)
f1.search_directory()




