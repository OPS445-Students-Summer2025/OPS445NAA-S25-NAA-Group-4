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
              rsync
              
              This program assumes that if the user did not backup
              files using this program that when running the restore
              program they have compressed their files using tar.>

Instructions when wanting to restore:
If you would like to run this program from the Command Line, the usage is as follows:
./assignment2.py --source_path OR -s source_filepath --dest_path OR -d destination_filepath.

If you would like to extract certain files/dirs, you may optionally include:
--specific OR -c filepath_of_file/dir_in_tarfile. 

You may add as many filepaths for the above option. 

Optionally, you may also just simply run the assignment2.py program to guide you through the process.
