# -*- coding: utf-8 -*-
"""
This Python code is to collect quantifications from Sara's Gui (2022 GitHub version) output .csv,
then save into a new csv file

Run this file in the folder of the quantification folder,
which contains '.tif' image and the related output folder

20231213 SHY
"""
import os, csv

def make_csv_file_name(filename):
    csvend1 = r'Result/'
    csvend2 = r'_PCA_Average_Polarity_Magnitude.csv'
    
    resultname = csvend1 + filename + csvend2
    csvpath = os.path.join(filename,resultname) #now we have a full path of the csv file
    return csvpath

def collect_csvs(filename,csvfile,final_list):
    reader = list(csv.reader(csvfile))      #open the output csv file
    reader[1][0] = filename                 #put the name ahead of data
    if final_list[0] != '':                 #check if it's the first data point
        final_list.append(reader[1])
    else:
        final_list = reader                 #if so, add a heading

    return final_list

def read_csvs(filepath,final_list):
    draftlist = []      # initialise a list
    for dir in os.listdir(filepath):    # for all the file in this folder
        draftlist.append(dir)  # get their full path, put into draft list
    draftlist.sort()
    
    #read, and check if a tif file have the same name, to avoid processing this .py file
    for filename in draftlist:
        fm = filename + '.tif'
        if fm in draftlist:
            csvpath = make_csv_file_name(filename)   #now we have a full path of the csv file
            csvfile = open(csvpath)
            final_list = collect_csvs(filename,csvfile,final_list)

    return final_list

def write_csvs(final_list):
#write into a new csv file
    f = open('polarity.csv','w')
    writer = csv.writer(f)
    for i in final_list:
        writer.writerow(i)
    f.close()




filepath = os.getcwd()  #import folder path
final_list = ['']
final_list = read_csvs(filepath,final_list)
write_csvs(final_list)
