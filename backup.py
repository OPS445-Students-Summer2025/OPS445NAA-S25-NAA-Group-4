#!/usr/bin/env python3

import subprocess
import sys
import os
import datetime

# Auto backup, only back up changed files
def auto_backup(target, destination):
    # Appending scripts to crontab, source: https://stackoverflow.com/questions/8579330/appending-to-crontab-with-a-shell-script-on-ubuntu
    # rsync from OPS345
    # -a is archive mode (preserves permissions, timestamps, symlinks, etc.)
    # -c is to check file hash to back up only changed files (default only check timestamps and sizes)
    cronjob = f"(crontab -l 2>/dev/null; echo '* * * * * rsync -avc {target} {destination}') | crontab -"
    subprocess.Popen(cronjob, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

# Manual backup, based on user's input
def manual_backup(target, destination, backup_name):
    backup = f"tar cvzf {destination}{backup_name}.tar.gz {target}"
    process = subprocess.Popen(backup, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    process.wait()
    return process.returncode


if __name__ == "__main__":
    if len(sys.argv) != 4:
        mode = int(input("Welcome to use BackupG4 to back up your files. Please choose backup mode(1/2):\n1, Auto backup\n2, Manual backup"))
        if mode == 1:
            target_path = input("Entering auto backup...\nPlease enter the path you want to back up:")
            dest_path = input("Please enter the path you want to store:")
            auto_backup(target_path, dest_path)

    if len(sys.argv) == 4 or mode == 2:
        print("Welcome to use BackupG4. Entering Manual backup...")
        if len(sys.argv) == 4: 
            target_path = sys.argv[1]
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            dest_path = f"{sys.argv[2]}"
            backup_name = f"{sys.argv[3]}_{timestamp}"
            try:
                os.makedirs(dest_path, exist_ok=True)
            except IOError:
                print("The folder cannot be created. Aborting...\nPlease check the permissions of the related folder.")
                exit()
            
            print("Backing up...")
            result = manual_backup(target_path, dest_path, backup_name)
            if result == 0:
                print("Successful! Your files has been backed up.")
            else:
                print("Backup failed, aborting...")

        elif mode == 2:
            target_path = input("Please enter the path you want to back up:")
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            dest_path = input("Please enter the path of the backup destination(include \"/\")")
            backup_name = input("Please enter a name of your backup:") + f"_{timestamp}"
            try:
                os.makedirs(dest_path, exist_ok=True)
            except IOError:
                print("The folder cannot be created. Aborting...\nPlease check the permissions of the related folder.")
                exit()
            
            print("Backing up...")
            result = manual_backup(target_path, dest_path, backup_name)
            if result == 0:
                print("Successful! Your files has been backed up.")
            else:
                print("Backup failed, aborting...")

        else:
            print("You did not provide the currect addresses as the arguments or choose a currect mode. Aborting...")