#!/usr/bin/env python3

import os
import tarfile
import argparse
import sys

#note will need to account for uncompressed/compressed files
#add a restore log for later
#fix up the wacky argparse stuff
#allow the user to pick which files/dirs they would like to restore
#checker to see if the area where the restore program is trying to restore to has enough space?

def main():
    '''
    Code will run the main Restore Module below, this restore program assumes that the
    user zipped or compressed their backup files beforehand to save space in archiving.
    The user can also run this program from the command line with arguments to
    take advantage of automation.
    '''

    #Clean up the screen
    os.system("clear")

    #Create argparse parser to extract source and destination filepaths from user if 
    #they choose to run program from commandline to make it faster and for automation
    restore_parser = argparse.ArgumentParser()

    restore_parser.add_argument('--source_path', type=str, help="filepath source of your backup")
    restore_parser.add_argument('--dest_path', type=str, help="filepath destination to restore backup")
    
    args = restore_parser.parse_args()

    #Only run the commandline arguments to restore if the acceptable amount of arguments
    #are met to prevent crashing. This includes the flags and the filename.
    if len(sys.argv) == 5:
        restore(args.source_path, args.dest_path)

    #Run the program with a user friendly restore experience in the case the proper
    #arugements are not met.
    else:
        #prob don't need the help...
        print("Welcome to the Restore Program!\nIf you would like to run this program from the Command Line, "
             f"the usage is as follows:\n{restore_parser.prog} --source_path source_filepath --dest_path destination_filepath")
        print("Optionally, you may also continue to follow this program to guide you through the process.")

        source_path = input("Please type in the filepath of the file/dir backup you would like to restore:")
        dest_path = input("Please type in the filepath destination where you would like to restore your backup:")
        
        restore(source_path, dest_path)


def restore(source_path, dest_path):
    '''
    Code will run user guided restore program, will use tarfile module to do so by 
    retrieving user wanted source backup file/dir and unzipping it to a new directory
    '''
    try:

        #Extract the file assuming it is zipped using tar, will have to make a program later that accounts for regular files/dirs
        #https://docs.python.org/3/library/tarfile.html#command-line-options << Source for the usage of tarfile        
        with tarfile.open(source_path, 'r') as tar:
            tar.extractall(path=dest_path)

        #Tell the user that the extraction was successful and close the program to give user relief of mind
        print(f"Full extraction from {source_path} to {dest_path} complete. Shutting down program...")
        return None

    except IOError:
        print("The inputted paths are not valid, please check permissions of files/dirs and if the filepath exists and rerun the program")
    except ValueError:
        print("You did not input any values, please rerun the program and try again")

if __name__ == "__main__":
    main()