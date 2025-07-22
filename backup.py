
#!/usr/bin/env python3

import subprocess
import sys
import os
import datetime

def main():
    # If the user did not enter correct arguments, ask user to choose backup mode
    try:
        if len(sys.argv) != 4:
            mode = int(input(f"Welcome to use BackupG4 to back up your files.\nRun the file as \"{sys.argv[0]} target_path destination_path backup_name\" to do manual backup\nPlease choose backup mode(1/2):\n1, Auto backup\n2, Manual backup\n"))
            if mode == 1:
                target_path = input("Entering auto backup...\nPlease enter the path you want to back up:")
                dest_path = input("Please enter the path you want to store the backup:")
                auto_result = auto_backup(target_path, dest_path)
                if auto_result == 0:
                    print("Auto backup enabled, a schedule has been added to the crontab.")
                else:
                    print("Enable auto backup failed, unable to add the crontab.")
                return
            # If the user chose 2 manual backup, run manual backup. All the user's inputs are from the input function
            

        # If the user entered correct arguments, run manual backup. All the user's inputs are from the arguments
        if len(sys.argv) == 4: 
            print("Welcome to use BackupG4. Entering Manual backup...")
            target_path = sys.argv[1]
            # source: https://docs.python.org/3/library/datetime.html#datetime.datetime.strftime
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            dest_path = f"{sys.argv[2]}"
            backup_name = f"{sys.argv[3]}_{timestamp}"
                
            # Call manual_backup function
            manual_backup(target_path, dest_path, backup_name)
            return

        if mode == 2:
            print("Welcome to use BackupG4. Entering Manual backup...")
            target_path = input("Please enter the path you want to back up:")
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            dest_path = input("Please enter the path of the backup destination(include \"/\")")
            backup_name = input("Please enter a name of your backup:") + f"_{timestamp}"

            manual_backup(target_path, dest_path, backup_name)
            return
    
    except:
        print("You did not provide the correct addresses as the arguments and choose a correct mode. Aborting...")
        return
    print("You did not provide the correct addresses as the arguments and choose a correct mode. Aborting...")
    return

# Auto backup. Only back up changed files. Paths are from user's input
def auto_backup(target, destination):
    # Appending scripts to crontab, source: https://stackoverflow.com/questions/8579330/appending-to-crontab-with-a-shell-script-on-ubuntu
    # rsync from OPS345
    # -a is archive mode (preserves permissions, timestamps, symlinks, etc.)
    # -c is to check file hash to back up only changed files (default only check timestamps and sizes)
    # 0 0 * * 6 means every Saturday at 00:00 AM
    crontab_cmd = f"(crontab -l 2>/dev/null; echo '0 0 * * 6 rsync -avc {target} {destination}') | crontab -"
    # Execute Linux command in python. exact syntax from the lab.
    process = subprocess.Popen(crontab_cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    process.wait()
    return process.returncode

# Manual backup. Paths and file name are from user's input
def manual_backup(target, destination, backup_name):
    target = target.rsplit("/",1)
    target = " ".join(target)
    target = "-C "+target
    try:
        # source: https://www.w3schools.com/python/ref_os_makedirs.asp
        # exist_ok set to True means if the file already exists, continue without raising an exception
        os.makedirs(destination, exist_ok=True)
    # Incorrect permission of the destination folder could cause this problem 
    except IOError:
        print("The folder cannot be created. Aborting...\nPlease check the permissions of the related folder.")
        exit()
    exclude_or_not = input("Do you want to exclude any files or folders?(y/n)")
    if exclude_or_not == "y":
        exclude = input("Enter the files or folders you want to exclude(separate them by space):")
        exclude_list = exclude.split(" ")
        for x in exclude_list:
            target = f"--exclude {x} " + target

    print("Backing up...")
    # Use tar to archive and compress folder to another location in the system
    tar_cmd = f"tar cvzf {destination}{backup_name}.tar.gz {target}"
    process = subprocess.Popen(tar_cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    # Wait till the backup process is complete
    process.wait()

    # check exit code
    if process.returncode == 0:
        print("Successful! Your files has been backed up.")
    else:
        print("Backup failed, aborting...")
    



if __name__ == "__main__":
    main()