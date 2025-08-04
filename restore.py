#!/usr/bin/env python3

import subprocess
import sys
import os
import datetime
import re
import tarfile

#note will need to add autoback up stuff and also account for uncompressed/compressed files
#add a restore log for later

def main():
    '''
    Code will run the main Restore Module below, this restore program assumes that the
    user zipped or compressed their backup files beforehand to save space in archiving
    '''

    #Try statement will attempt to run the Restore program and check and break off
    #with reasonable error statement to user to explain their mistake
    try:

        os.system("clear")
        choice = input("Welcome to the Restore Program! What would you like to do?\n1. Manually Restore\n2. Setup Auto Restore\n")
        
        #Redirects user choice to functions that will run users wanted option
        if choice == '1':
            manual_restore()
        if choice == '2':
            pass

    except:
        print("An incorrect option was entered. Please rerun the program and try again")


def manual_restore():
    '''
    Code will run manual restore program, will use either copy or rsync to do so by 
    retrieving user wanted source backup file/dir and unzipping it to a new directory
    '''
    try:
        os.system("clear")
        
        source_path = input("You have chosen Manual Restore Mode. Please type in the filepath of the file/dir backup you would like to restore:")
        dest_path = input("Please type in the filepath where you would like to send your backup:")

        #Extract the file/dir assuming it is zipped using tarfile module, will have to make a program later that accounts for both
        #https://docs.python.org/3/library/tarfile.html#command-line-options << Source for the usage of tarfile        
        with tarfile.open(source_path, 'r') as tar:
            tar.extractall(path=dest_path)

        #Tell the user that the extraction was successful and close the program to give user relief of mind
        print(f"Full extraction from {source_path} to {dest_path} complete. Shutting down program...")
        return None

    except IOError:
        print("The inputted paths are not valid, please check permissions of files/dirs and if the filepath exists and rerun the program")

if __name__ == "__main__":
    main()