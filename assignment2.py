#!/usr/bin/env python3

'''
OPS445 Assignment 2
Program: assignment2.py 
The python code in this file is original work written by
"OPS445 NAA GROUP 4". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. We have not shared this python script
with anyone or anything except for submission for grading. We understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.

Author: <OPS445 NAA GROUP 4>
Semester: <Summer> <2025>
Description: <Script will perform backup and restore capabilities
              sometime in the near future.>
'''
import backup
import os

#Run Main Code here as the menu
if __name__ == '__main__':

    #Menu Dialog to user to gain their input/choice
    choice = input("Welcome to the Backup and Restore Program!\nWhat would you like to do?\nPlease type in your choice according to the number and press ENTER\n1. Backup\n2. Restore\n3. Exit\n")
    
    if choice == '1':
        #Do Backup code and prompts here
        #Right now, still trying to figure out how to pass in cmd line arguments from this program to backup.main()
        os.system("clear")
        backup.main()
    
    if choice == '2':
        #do Restore code
        pass

    if choice == '3':
        exit()

    
    exit()
    