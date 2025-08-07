# SUMMER 2025 OPS445NAA GROUP 4 PROJECT

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

Instructions when wanting to backup:
You have 2 options:

Run the file as ./assignment2.py target_path destination_path backup_name to do a manual backup

OR

Choose a backup mode when you run the script without arguments. This will let you use autobackup


Instructions when wanting to restore:
If you would like to run this program from the Command Line, the usage is as follows:
./assignment2.py --source_path OR -s source_filepath --dest_path OR -d destination_filepath.

If you would like to extract certain files/dirs, you may optionally include:
--specific OR -c filepath_of_file/dir_in_tarfile. 

You may add as many filepaths for the above option. 

Optionally, you may also just simply run the assignment2.py program to guide you through the process.


Research:

All references to websites used to help create the project are listed below, more verbose documenation
can be found in their corresponding modules:

https://docs.python.org/3/library/re.html documentation on python libraray re used for <autobackup.py and backup.py>
https://www.commandlinux.com/man-page/man1/tar.1.html documentation on linux command tar used for <backup.py>
https://docs.python.org/3/library/argparse.html#module-argparse documentation on python libraray argparse used for <autobackup.py, restore.py, and backup.py>
https://docs.python.org/3/library/os.path.html#os.path.expanduser documentation for os.path.expanduser for ~ expansion used for <backup.py>
https://docs.python.org/3/library/os.path.html#os.path.exists documentation for os.path.exists to check if a file or folder exists used for <backup.py>
https://stackoverflow.com/questions/8579330/appending-to-crontab-with-a-shell-script-on-ubuntu stackoverflow forum referenced for appending scripts to crontab used for <backup.py>
https://docs.python.org/3/library/subprocess.html#subprocess.Popen.wait documentation for subprocess.Popen.wait used for waiting until a backup process if finishied used in <backup.py>
https://docs.python.org/3/library/datetime.html#datetime.datetime.strftime documentation referenced for making timestamps used in <backup.py>
https://www.w3schools.com/python/ref_os_makedirs.asp documentation for os.makedirs used in <backup.py>
https://askubuntu.com/questions/408611/how-to-remove-or-delete-single-cron-job-using-linux-command used in <autobackup.py>
https://docs.python.org/3/library/glob.html documentation for glob used in <autobackup.py>
https://docs.python.org/3/library/tarfile.html#command-line-options documentation for tarfile used in <restore.py>
https://docs.python.org/3/library/os.path.html documentation for error checking used in <restore.py>


Assignment 2 Proposal Questions:
What are will be your Backup and Restore minimum viable product?

The user can enter arguments for the target file to backup and their backup destination. After implementing this feature, automatic backup will be implemented so that it will backup a certain file after a static amount of time.

**Additional Professor Comments:
backup: directories
MVP:

    hardcoded 1/week scheduling
    exclude a directory
    compression

What arguments or options will be included?
scheduling auto backup in specific time interval

generate backup log

use timestamp to delete older backup

restore backup from user specified time

tar and gzip backup compression


What are the steps to complete this assignment?
    1. create a prompt that asks the user for an argument to target the file for backup and copy it to the destination
    2. create the auto backup system that will automatically backup a certain file after a static amount of time passes.
    3. create the date and time feature which details where the backup will happen and generate a log
    4. do the tar and gzip compression on the backup
    5. schedule a auto backup cronjob
    6. delete older backup
    7. option to restore backup

How will your team divide up the work? How will you communicate? How will you decide when each step is complete?
division of work:

Kang Kang will focuses on backup section
Tsz Him Ko will focuses on restore section
Charles Shin will focuses on assignment2.py section

We meet in person during OPS class time every week and on Microsoft Teams regularly.

We will test each step to decide if it is complete.
