#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 11:02:02 2018

@author: genevieve
"""

import xml.etree.ElementTree as ET
import os
from vulgar_dic import vulgar_collection


#printing child attrib movie

def print_child(root):
    for child in root:
        print(child.tag, child.attrib)



def create_movie_txt(root,vulgar_words):
    count =1
    while(count<616):
        file_name='movie'+str(count)+'.txt'
        location=os.path.join('./data/tmp/',file_name)
        # open a file for writing
        f = open(location, 'wr')

        for dialogue in root.findall('./movie[@id="'+str(count)+'"]/dialogue'):
    #    for dialogue in root.findall('./movie[@id="'+'615'+'"]/dialogue'):
            speaker=dialogue.findall('speaker')

            utterance=dialogue.findall('utterance')
            speaker_list=[]

            for row_num in range(0,len(speaker)):

               check=''
               utter=[]
               utter=[word for word in (utterance[row_num].text.lower().split()) if not word in vulgar_words]
               utter = ' '.join((utter)).encode('utf-8').strip()

               if  row_num==0:

                   speaker_list.append(speaker[row_num].text)
                   f.write("speaker1: %s \n" % (utter))
    #               print("speaker1: %s %s " % (speaker_list[0],utter))

               if row_num!=0:

                   for row in range(0,len(speaker_list)):

                       if speaker[row_num].text ==speaker_list[row]:
                           check='yes'
                           f.write("speaker%d: %s\n"%(row+1,utter))
    #                       print("speaker%d: %s %s"%(row+1,speaker_list[row],utter))

                   if  row==(len(speaker_list)-1) and speaker_list[row]!=speaker[row_num].text and check=='':

                       speaker_list.append(speaker[row_num].text)
                       f.write("speaker%d: %s\n"%(row+2,utter))
     #                  print("speaker%d: %s %s"%(row+2,speaker[row_num].text,utter))

            f.write('\n')
      #      print('\n')
        f.close()
        count+=1


#    for speaker in speaker1:
#        speakers.append(speaker.text)
#    for utter in utterance:
#        utters.append(utter.text)

#    speaker1=dialogue.findall('speaker').text
#    speaker.append(speaker1)
#    utterance=dialogue.find('utterance').text
#    speaker.append(utterance)

if __name__ == '__main__':

    vulgar_words=vulgar_collection()

    tree = ET.parse("./data/MovieDiC_V2.xml")
    root = tree.getroot()
    #print child attrib movie
#    print_child(root)

    if not os.path.exists('./data/tmp/'):
        os.makedirs('./data/tmp/')

    create_movie_txt(root,vulgar_words)







