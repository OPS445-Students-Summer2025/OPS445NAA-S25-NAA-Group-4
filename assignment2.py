#!/usr/bin/env python3

'''
OPS445 Assignment 2
Program: assignment2.py 
The python code in this file is original work written by 
"OPS445 NAA GROUP 4". No code in this file is used without reference
from any other source except those provided by on-line resources 
where sources are documented. We have not shared this python script
with anyone or anything except for submission for grading. We 
understand that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.

Authors: <OPS445 NAA GROUP 4 Group Members:
          Charles Shin
          Kang Kang
          Tsz Him Ko>
Semester: <Summer> <2025>
Description: <Script will perform backup and restore capabilities.
              Backup can be done manually through the commandline
              interface or through a user guided process. Autobackup
              can also be set up as well to regularly backup a certain
              file/dir using crontab as the scheduling program. The
              same goes for the restore functionaility. This
              program assumes the user is using a Linux based OS with
              the following modules/python scripts downloaded and in
              the same directory:
              
              assignment2.py
              autobackup.py
              backup.py
              restore.py
              
              This script and it's import modules also utilize
              python libraries and Linux tools listed below:
              
              os
              sys
              subprocess
              datetime
              re
              glob
              argparse
              tarfile
              
              cron
              
              This program assumes that if the user did not backup
              files using this program that when running the restore
              program they have compressed their files using tar.>
'''
import backup
import restore
import os

#Run Main Code here as the menu
if __name__ == '__main__':

    #Menu Dialog to user to gain their input/choice to see if they would like to backup or restore
    choice = input("Welcome to the Backup and Restore Program!\nWhat would you like to do?\nPlease type in your choice according to the number and press ENTER\n1. Backup\n2. Restore\n3. Exit\n")
    
    if choice == '1':
        #The backup.py main function is run. It works alongside the autobackup.py module
        os.system("clear")
        backup.main()
        exit()
    
    if choice == '2':
        #do Restore code
        os.system("clear")
        restore.main()
        exit()

    if choice == '3':
        print("Exiting...")
        exit()
    
    print("An incorrect option was inputted, Exiting...")
    exit()
    