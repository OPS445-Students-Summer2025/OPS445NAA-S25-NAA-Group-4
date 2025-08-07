#!/usr/bin/env python3

import os
import tarfile
import argparse

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

    restore_parser.add_argument('-s', '--source_path', type=str, help="string filepath source of your backup")
    restore_parser.add_argument('-d', '--dest_path', type=str, help="string filepath destination to restore backup")
    restore_parser.add_argument('-c', '--specific', nargs='*', help="filepaths of specific files/directories"
                                " you would like to extract from inside the tarfile.")

    args = restore_parser.parse_args()
    
    #Only run the commandline arguments to restore if the acceptable arguments
    #are user assigned when they run the program. Extract the file assuming it is zipped using tar. 
    #https://docs.python.org/3/library/tarfile.html#command-line-options << Source for the usage of tarfile 
    #Another similar command appears later that reflects from user input in the
    #script instead of through the command line.  
    if args.source_path and args.dest_path:

        #Function that checks if provided source tarfile is actually a tarfile to
        #prevent crashing.
        check_if_tarfile(args.source_path)

        with tarfile.open(args.source_path, 'r') as tar:
            extract_specific(tar, args.dest_path, args.specific)
            return None

    #Run the program with a user friendly restore experience in the case the proper
    #arguments are not met. Instructions are given in this program greeting.
    else:
        print("Welcome to the Restore Program!\nIf you would like to run this program from the Command Line, "
             f"the usage is as follows:\n{restore_parser.prog} --source_path OR -s source_filepath --dest_path" 
             " OR -d destination_filepath.\nIf you would like to extract certain files/dirs, you may optionally"
             " include --specific OR -c filepath_of_file/dir_in_tarfile.\nYou may add as many filepaths for the"
             " above option.\n")
        print("Optionally, you may also continue to follow this program to guide you through the process.")

        source_path = input("Please type in the filepath of the file/dir backup you would like to restore:")
        dest_path = input("Please type in the filepath destination where you would like to restore your backup:")
        
        restore(source_path, dest_path)

def restore(source_path, dest_path):
    '''
    Function will run restore program, will use tarfile module to do so by retrieving user wanted source 
    backup file and unzipping it to a new directory
    '''
    try:
        check_if_tarfile(source_path)
        
        #Extract the file assuming it is zipped using tar. 
        #https://docs.python.org/3/library/tarfile.html#command-line-options << Source for the usage of tarfile        
        with tarfile.open(source_path, 'r') as tar:
            extract_specific(tar, dest_path)
        
        #Tell the user that the extraction was successful and close the program to give user relief of mind
        print(f"Extraction from {source_path} to {dest_path} complete. Shutting down program...")
        return None

    #Exception handling in the case that the user attempts to restore a file they do not have permissions for,
    #if the file/dir does not exist, or if some copying error occurred.
    except IOError:
        print("The inputted paths are not valid, please check permissions of files/dirs and if the filepath "
        "exists and rerun the program")
    #Exception handling if the user did not input any filepaths in either the source path or destination path
    #prompts.
    except ValueError:
        print("You did not input any values, please rerun the program and try again")
        
def extract_specific(tar_file, dest_path, specific_list_arg=None):
    '''
    Function will ask the user if they would like to extract specific files/dirs and 
    will restore all user specified files/dirs if they exist. Will extract all otherwise.
    '''

    #Code will run if user specified the flag for --specific or -c for certain files/dirs
    #to be extracted from the tarfile. Will skip to the user guided one if any of the 
    #filepaths are incorrect.
    if specific_list_arg:
        check = True

        #Function that checks if any of the filepaths are incorrect and will
        #not return a value if so. Otherwise, returns False meaning all 
        #file paths are correct
        check = error_check_specific(tar_file, specific_list_arg, dest_path)
        
        if check == False:
            #Tell the user that the extraction was successful and close the program to give user relief of mind
            print("Extraction complete. Shutting down program...")
            return None
        else:
            print("Defaulting to user guided choices...")
    
    #Ask user if they would like to extract all or specific files/dirs for use in later if statement
    choice = input("Would you like to extract only specific files/directories from the tar file? (y/n) ")

    #Code runs if user wants to extract specific files, runs a while loop if user
    #makes any errors when inputting any filepaths.
    if choice == 'y' or choice == 'Y':
        key = True #creates infinite loop unless user inputs correct filepaths

        while(key == True):

            os.system('clear')

            #Showcase all files/dirs in tar file and ask user for which specific
            #ones they would like indicated by spaces for multiple ones.
            print(tar_file.getnames())
            specific = input("Which specific file(s)/dir(s) would you like to extract from the tar file?\n"
                             "If typing in multiple files/dirs, seperate each file/dir with a space\n"
                             "You must type the exact filepath to the specific file/dir as shown above.\n")
            list_of_specific = specific.split(" ")

            key = error_check_specific(tar_file, list_of_specific, dest_path)
    
    #Extract all files/dirs from tar file from user specified source path if
    #user correctly typed in "N" option.
    elif choice == 'n' or choice == 'N':   
        print("Proceeding with full extraction...")         
        tar_file.extractall(path=dest_path)
    
    #Acts as user error catch to default into extract all behaviour if anything
    #besides y or n was inputted.
    else:
        print("Invalid option, defaulting to extraction of all files...")
        tar_file.extractall(path=dest_path)

    return None

def check_if_tarfile(source_path):
    '''
    #Test if the source file is actually a tarfile to prevent crashing/errors in program. Exit program
    #and inform user if that is the case. https://docs.python.org/3/library/os.path.html << source for 
    #os.path.isfile() method.
    '''
    if os.path.isfile(source_path) is False or tarfile.is_tarfile(source_path) is False:
        print("The source file is either not a tar archive or is a regular file/dir. Please archive"
        "/compress the file using tar and rerun the restore program.")
        exit()

def error_check_specific(tar_file, list_of_specific, dest_path, error=0):
    '''
    Function that ensures the list of specific filepaths are correct
    to prevent crashing.
    '''
    error = 0

    #Error checker, will force the while loop to keep running if one
    #of the user inputted values is not exactly the filepaths shown
    #from before.
    for files_dirs in list_of_specific:
        if files_dirs not in tar_file.getnames():
            print(f"{files_dirs} does not exist in the tar file")
            temp = input("\nPress ENTER to continue")
            error += 1
    
    #If no errors were detected from previous if statement, this
    #code will run extracting specific user files/dirs to the
    #user specified path.
    if error == 0:
        print("Extracting all specified files/dirs:\n")
        for files_dirs in list_of_specific:
            print(f"{files_dirs}\n")
            tar_file.extract(files_dirs, path=dest_path)
        return False

#Main function for testing
if __name__ == "__main__":
    main()