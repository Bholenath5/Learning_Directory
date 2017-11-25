#findObject
#python setup.py install
#easyinstall
#setuptool is the basic package of installation we can install other packages
#site packages is the place in python 27 folder which contains all the packages.
#Any new package has to be copied to site pakages. setoptool is the package we need to instal which are not by default
#waitForObject
#raise Exception
#Alt+3 comment block in IDLE
# 1) Write a program to get filename from given path with desired extensions

import os
#from fnmatch import fnmatch
extension = "*.txt"
stPath = "D:\DriverAssist\APA\Config4"

for path, directories, filnames in os.walk(stPath):
    print str(filnames)
    for name in filnames:
        #if fnmatch(name, extension):
        if '.txt' in name:
            print name

#Functions learnt fnmatch,os and os.walk(it creates dictionaries with

#2)Write a program to get filename from given path with desired extensions but
#at runtime user must be asked to enter the path and extension

import os
from fnmatch import fnmatch
#extension = "*.txt"
extension = raw_input("Select the extension")
stPath = raw_input("Select the path")

#stPath = "D:\DriverAssist\APA\Config4"

for path, directories, filnames in os.walk(stPath):
    print str(filnames)
    for name in filnames:
        if fnmatch(name, extension):
        #if extension in name:
            print name


#Function learnt raw_input
#fnmatch takes input as *.txt  while if condition takes as .txt



#3) Usage of for loop
#Print below pattern
#    *
#   * *
#  * * *
# * * * *
#i = input("Enter a number:")
i = 6
char = " *"
char1 = " "
for j in range(6):  
    print char1*(i-j)+char*j
#in last line 5 stars

#i = input("Enter a number:")
i = 6
char = " *"
char1 = " "
for j in range(i+1):
    print char1*(i-j)+char*j   #char1*(j)+char*(i-j)  reverse pattern

#in last line 6 stars

# char*i it prints the char or string i times and + will help concatenating
#Function learnt input(to enter integer and raw_input is to enter string values)

#Usage of elif loop
i = input("Enter a number:")
#i = 3 #for example 3
char = " *"
char1 = " "
for j in range(1,i+i):
    if j<i:
        print char1*(i-j)+char*j
    elif j == i:
        print char1*(i-j)+char*j
    elif j>i:
        print char1*(j-i)+char*(2*i-j)



#list
stan = list("sanchita")
>>> stan
['s', 'a', 'n', 'c', 'h', 'i', 't', 'a']
>>> stan[1]= "A"
>>> stan
['s', 'A', 'n', 'c', 'h', 'i', 't', 'a']
saat = ['1','2']
#append
>> saat.append("4")
>>> saat
['1', '2', '4']
>>> saaat
['1', '2', '@', '3']
>>> saaat[2] = "d"
>>> saaat
['1', '2', 'd', '3']
#join
>> "".join(saaat)
'12d3'
>>> ''.join(saaat)
'12d3'
#reverse : reverse() takes no arguments
>>> saat
['a', 't', 'i', 'h', 'c', 'n', 'a', 's']
#tuple
atas = tuple("atsa")
>>> atas
('a', 't', 's', 'a')
>>> atas[1]
't'

#To create a directory with bcar name
#\\ should be given whereas generally we use \
import os
path = "D:\\DriverAssist\\APA\\bcar3"
if not os.path.isdir(path):
   os.makedirs(path)
#Create a file 
file = open("D:\\DriverAssist\\APA\\bcar3\\new3.txt", "w")

#file object = open(file_name [, access_mode][, buffering])
import os
import shutil
path = "D:\\DriverAssist\\APA\\bcar3\\new1.txt"
if not os.path.isdir(path):
   os.makedirs(path)
#Create a file 
file = open("D:\\DriverAssist\\APA\\bcar3\\new3.txt", "w")
file.close()# #"D:\\DriverAssist\\APA\\bcar3\\new4.txt")
print "Closed or not : ", file.closed #Closed or not :  False(Will tell if the file is closed or not)
print "File name: ",file.name #File name: new.txt
print "Opening mode : ", file.mode #Opening mode :  w
shutil.rmtree(path)
os.remove(path) #will remove a file.
os.rmdir(path) #will remove an empty directory.
shutil.rmtree(path) #will delete a directory and all its contents.


#Check if in a path directory exists
#delete all the files along with directory
#Create the dir in same path
#Go to the path and list the content from directory
#Check the files with .bmp extension
#Copy the files from destination to source:created dictionary:
#shutil.move , shutil.copy
import os
import shutil
from fnmatch import fnmatch

pathDir = "C:\\Ford_Automation_Gen3\\Shared\\Log\\HMIScreenShots\\images"
for path, directories, src_file_name in os.walk(pathDir):
    print str(src_file_name)
    print str(directories)
    print str(path)
    shutil.rmtree(pathDir)
    if not os.path.isdir(pathDir):
        os.makedirs(pathDir)
        extension = "*.bmp"
        extension = "*BT*"
        pathCopyFiles = "C:\\Ford_Automation_Gen3\\Shared\\Log\\HMIScreenShots\\Audio\\suite_AUDIO\\tst_AM"
        for path, directories, src_file_name in os.walk(pathCopyFiles):
            print str(src_file_name)
            print "Files in pathCopyFiles"
            for name in src_file_name:
                if fnmatch(name, extension):
                #if '.bmp' in name:
                    print str(name)
                    full_file_name_path = os.path.join(pathCopyFiles, name)
                    shutil.copy(full_file_name_path, pathDir)
                    #shutil.move(full_file_name_path, pathDir)
					
#To check whether a word is palandrome or not
