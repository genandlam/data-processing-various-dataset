#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 10:42:22 2018

@author: genevieve
"""

import os


doc=['1','3','6','7','9','10','11','13','14a','14b','15a','15b','16','17','18','20','21']
for i in doc:
    
    f=open('./data/raw/amex'+ i+'.txt','r')
    location=os.path.join('./data/process/','amex'+i+'.txt')
    f_write=open(location,'w')
    read_line=f.readlines()
    amex = [line.rstrip('\n') for line in read_line]
    amex= list(filter(None, amex))
    del amex[0]
    del amex[-1]
    
    for row_num,item in enumerate(amex):
        
       if item.find('xx')!=-1 and item.find('xx [')==-1:
               
           agent=" ".join([word for word in (item.lower().split()) if not word=="xx"])
    #       print("Agent: %s" % agent )
           f_write.write("Agent: %s\n" % agent )
       
       if item.find('xx')==-1 and item.find('xx [')==-1 and item!=" ":
            
    #        print("speaker: %s" % item )
            f_write.write("speaker: %s\n" % item )
            
       
       
    f_write.close()
       
  