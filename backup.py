#!/usr/bin/env python3

import subprocess
import sys
import os
import datetime
import re
import argparse

def main():
    
    # If the user entered correct arguments, run manual backup. All the user's inputs are from the arguments
    try:
        # use parser module instead of sys.argv. source https://docs.python.org/3/library/argparse.html#module-argparse
        parser = argparse.ArgumentParser() #create argparse object
        parser.add_argument("target_path", nargs="?") #add a positional argument target_path into the python script
        parser.add_argument("dest_path", nargs="?") #add dest_path positional argument
        parser.add_argument("backup_name", nargs="?") #add backup_name positional argument
        args = parser.parse_args() #make a object that contain all the argument entered
        if args.target_path and args.dest_path and args.backup_name: #check if all argument are here

            print("Welcome to BackupG4. Entering Manual backup...")

            target_path = args.target_path
            # support home directory expansion "~". source https://docs.python.org/3/library/os.path.html#os.path.expanduser
            target_path = os.path.expanduser(target_path)
            # check if the file or folder exists. source https://docs.python.org/3/library/os.path.html#os.path.exists
            if not os.path.exists(target_path):
                print(f"{target_path} does not exist.")
                return
            if not re.findall("^/[^/]*$", target_path): # for edge case of file starting from root for example: /etc
                target_path = target_path.rsplit("/",1)
                target_path = " ".join(target_path)
                target_path = "-C "+target_path #the target path ends like this: "-C /home/thko1/ops445/a2 filename" this is for the tar command later
                

            dest_path = args.dest_path
            dest_path = os.path.expanduser(dest_path)
            if not re.findall(r'/$',dest_path): #check if the path ends with a / if not then add / to the end
                dest_path = dest_path + "/" #add / to the end
            backup_name = args.backup_name
            
             
            # Call manual_backup function
            manual_backup(target_path, dest_path, backup_name) #call backup function
            return
        
    # If the user did not enter correct arguments, ask user to choose backup mode
        else:
                  
            mode = int(input(f"Welcome to BackupG4, a program to back up your files.\nYou have 2 options:\nRerun the file as \"{sys.argv[0]} target_path destination_path backup_name\" to do a manual backup\nOR\nChoose a backup mode:\n1, Auto backup\n2, Manual backup\n"))
    
            target_path = input("Please enter the path you want to back up:")
            target_path = os.path.expanduser(target_path) #this will exapnd the ~ for example ~/ops445/a2 into /home/thko1/ops445/a2
            if not os.path.exists(target_path): #this will check if a directory exisit
                print(f"{target_path} does not exist.")
                return
            if not re.findall("^/[^/]*$", target_path): # for edge case of file starting from root for example: /etc
                target_path = target_path.rsplit("/",1)
                target_path = " ".join(target_path)
                target_path = "-C "+target_path #the target path ends like this: "-C /home/thko1/ops445/a2 filename" this is for the tar command later
            
            dest_path = input("Please enter the path you want to store the backup:") 
            dest_path = os.path.expanduser(dest_path)
            #source https://docs.python.org/3/library/re.html
            if not re.findall(r'/$',dest_path): #check if the path ends with a / if not then add / to the end
                dest_path = dest_path + "/"  #add / to the end

            backup_name = input("Please enter a name of your backup:")

            exclude_or_not = input("Do you want to exclude any files or folders?(y/n)") #chose exclude file or not
            if exclude_or_not == "y":
                exclude = input("Enter the files or folders you want to exclude(separate them by space):")
                exclude_list = exclude.split(" ") #split each file in a list
                for x in exclude_list: 
                    target_path = f"--exclude {x} " + target_path #end prodcut will be like: "--exclude test1 test2 -C /home/thko1/ops445/a2 filename"

            
           
            
            if mode == 1:
                print("Entering auto backup...")
                auto_result = auto_backup(target_path, dest_path, backup_name) #call auto backup function and get the result of successful or not
                if auto_result == 0:
                    print("Auto backup enabled, a schedule has been added to the crontab.")
                else:
                    print("Enable auto backup failed, unable to add the crontab.")
                return
            # If the user chose 2 manual backup, run manual backup. All the user's inputs are from the input function
            
            if mode == 2:
                print("Entering Manual backup...")
                manual_backup(target_path, dest_path, backup_name) #call manual backup
                return
    
    except:
        print("You did not provide the correct addresses as the arguments and choose a correct mode. Aborting...") #if any unhandled error happend this message print
        return
    print("You did not provide the correct addresses as the arguments and choose a correct mode. Aborting...") #if user enter wrong mode number this message print
    return

# Auto backup. Only back up changed files. Paths are from user's input
def auto_backup(target, destination, name):
    # Appending scripts to crontab, source: https://stackoverflow.com/questions/8579330/appending-to-crontab-with-a-shell-script-on-ubuntu
    # rsync from OPS345
    # -a is archive mode (preserves permissions, timestamps, symlinks, etc.)
    # -c is to check file hash to back up only changed files (default only check timestamps and sizes)
    # 0 0 * * 6 means every Saturday at 00:00 AM
    #source: https://docs.python.org/3/library/re.html
    autoscriptpath = re.sub(r'\/[^/]*$',"/autobackup.py",sys.argv[0]) #replace the end of current path to /autobackup.py
    crontab_cmd = f'(crontab -l 2>/dev/null; echo \'0 0 * * 6 {autoscriptpath} "{target}" {destination} {name}\') | crontab -' #the cronjob will be like: 0 0 * * 6 /home/thko1/ops445/a2/autobackup.py "--exclude test1 test2 -C /home/thko1/ops445/a2 filename" /home/thko1/ops445/a2/backup/ test 
    # Execute Linux command in python. exact syntax from the lab.
    process = subprocess.Popen(crontab_cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    # Wait till the backup process is complete. source https://docs.python.org/3/library/subprocess.html#subprocess.Popen.wait
    process.wait()
    return process.returncode #return 0 if successful

# Manual backup. Paths and file name are from user's input
def manual_backup(target, destination, backup_name):
    # source: https://docs.python.org/3/library/datetime.html#datetime.datetime.strftime
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_name = f"{backup_name}_{timestamp}" #add timestamp to backup name

    try:
        # source: https://www.w3schools.com/python/ref_os_makedirs.asp
        # exist_ok set to True means if the file already exists, continue without raising an exception
        os.makedirs(destination, exist_ok=True)
    # Incorrect permission of the destination folder could cause this problem 
    except IOError:
        print("The folder cannot be created. Aborting...\nPlease check the permissions of the related folder.")
        exit()

    print("Backing up...")
    # Use tar to archive and compress folder to another location in the system
    #print(f"Target: {target}")
    #print(f"Destination: {destination}{backup_name}.tar.gz")
    #print(f"Running as UID: {os.geteuid()}")

    tar_cmd = f"tar cvzf {destination}{backup_name}.tar.gz {target}" #the tar command will be like: tar cvzf /home/thko1/ops445/a2/backup/test2025-07-26_13-22-21.tar.gz --exclude test1 test2 -C /home/thko1/ops445/a2 filename
    process = subprocess.Popen(tar_cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    
    process.wait()

    # check exit code
    if process.returncode == 0: #if tar command run sucessfully it five code 0 
        print("Successful! Your files has been backed up.") 
    else:
        print("Backup failed, aborting...")
    
if __name__ == "__main__":
    main()
